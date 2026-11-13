import sys
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import update_tracker as tracker

FIXTURES = Path(__file__).parent / 'fixtures'
DETAIL = (FIXTURES / 'detail.html').read_text()
LIST = (FIXTURES / 'list.html').read_text()
RID = 'FB23287576'


class TrackerTests(unittest.TestCase):
    def test_actual_detail(self):
        meta, sections = tracker.parse_detail(DETAIL, RID)
        self.assertEqual(meta['developer'], 'Ömer Güven')
        self.assertEqual(meta['status'], 'Closed')
        output = tracker.render_markdown(meta, sections)
        self.assertIn('confidential and withheld from publication.', output)
        self.assertNotIn('Full list of requests', output)

    @patch.object(tracker, 'MIN_EXPECTED_REQUESTS', 2)
    def test_listing_count_and_unique_ids(self):
        self.assertEqual([r[0] for r in tracker.parse_listing(LIST)], ['FB25276970', 'FB25330811'])
        for bad in (LIST.replace('>2</span>', '>3</span>'),
                    LIST.replace('fb25276970', 'fb25330811'), '<html>Sign in</html>'):
            with self.assertRaises(RuntimeError):
                tracker.parse_listing(bad)

    def test_default_minimum(self):
        with self.assertRaises(RuntimeError):
            tracker.parse_listing(LIST)

    def test_detail_validation(self):
        for bad in (DETAIL.replace(RID, 'FB123'),
                    DETAIL.replace('Status:', 'Unknown:'),
                    DETAIL.replace('<h3>Communications</h3>', ''), '<html>Sign in</html>'):
            with self.assertRaises(RuntimeError):
                tracker.parse_detail(bad, RID)

    def test_rich_communications_and_confidential_developer(self):
        # Synthetic rich content exercises lists, links, paragraphs and new headings.
        rich = DETAIL.replace('Ömer Güven', 'Confidential').replace(
            '<p>Communications with this requestor are confidential and withheld from publication.</p>',
            '<h4>July 1 — Apple to Developer</h4><p>First reply.</p>'
            '<p>See <a href="https://developer.apple.com/documentation/">docs</a>.</p>'
            '<ul><li>First item</li><li>Second item</li></ul>'
            '<h3>New section</h3><p>More information.</p>')
        meta, sections = tracker.parse_detail(rich, RID)
        output = tracker.render_markdown(meta, sections)
        self.assertTrue(meta['confidential'])
        for text in ('July 1 — Apple to Developer', '[docs](https://developer.apple.com/documentation/)',
                     '* First item', '## New section', '| Confidential | Yes |'):
            self.assertIn(text, output)

    def test_stable_names_and_idempotence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            out, index = root / 'requests', root / 'index.md'
            out.mkdir()
            old = '109-FB23287576-Old-Name.md'
            (out / old).write_text('old')
            existing = tracker.existing_filenames(out)
            record = tracker.parse_detail(DETAIL, RID)
            new = tracker.parse_detail(DETAIL.replace(RID, 'FB99999999'), 'FB99999999')
            tracker.write_outputs([new, record], out, index, existing)
            self.assertTrue((out / old).exists())
            self.assertTrue((out / '110-FB99999999-Ömer-Güven.md').exists())
            before = {p.name: p.read_bytes() for p in out.iterdir()}
            index_before = index.read_bytes()
            tracker.write_outputs([record, new], out, index, tracker.existing_filenames(out))
            self.assertEqual(before, {p.name: p.read_bytes() for p in out.iterdir()})
            self.assertEqual(index_before, index.read_bytes())

    def test_failed_detail_does_not_replace_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            out, index = root / 'requests', root / 'index.md'
            out.mkdir()
            old = out / f'109-{RID}-Old.md'
            old.write_text('original')
            index.write_text('original index')
            listing = [(RID, 'first'), ('FB99999999', 'second')]
            with patch.object(tracker, 'parse_listing', return_value=listing), \
                 patch.object(tracker, 'fetch_html', side_effect=['listing', DETAIL, RuntimeError('failed')]):
                with self.assertRaises(RuntimeError):
                    tracker.main(['--out', str(out), '--index', str(index)])
            self.assertEqual(old.read_text(), 'original')
            self.assertEqual(index.read_text(), 'original index')

    def test_missing_existing_request_stops_sync(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / f'109-{RID}-Old.md').write_text('original')
            with patch.object(tracker, 'parse_listing', return_value=[]), \
                 patch.object(tracker, 'fetch_html', return_value='listing'):
                with self.assertRaisesRegex(RuntimeError, 'omits existing'):
                    tracker.main(['--out', str(root)])

    def test_http_500_preserves_existing_and_defers_new_then_recovers(self):
        for staging in (False, True):
            with self.subTest(staging=staging), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                live = root / 'live'
                live.mkdir()
                old_name = f'109-{RID}-Old.md'
                old = tracker.render_markdown(*tracker.parse_detail(DETAIL, RID)).replace(
                    '| Current Status | Closed |', '| Current Status | Phase I |').encode()
                (live / old_name).write_bytes(old)
                out = root / 'staging' if staging else live
                index = root / 'index.md'
                new_id, good_id = 'FB99999998', 'FB99999999'
                listing = [(RID, 'old'), (new_id, 'new'), (good_id, 'good')]
                error = lambda: tracker.urllib.error.HTTPError('url', 500, 'Server Error', {}, None)
                args = ['--existing-dir', str(live), '--out', str(out), '--index', str(index)]
                good = DETAIL.replace(RID, good_id)
                with patch.object(tracker, 'parse_listing', return_value=listing), \
                     patch.object(tracker, 'fetch_html', side_effect=['list', error(), error(), good]), \
                     patch('sys.stderr') as stderr:
                    self.assertEqual(tracker.main(args), 0)
                warnings = ''.join(call.args[0] for call in stderr.write.call_args_list)
                self.assertIn(f'::warning::{RID}', warnings)
                self.assertIn(f'::warning::{new_id}', warnings)
                self.assertEqual((out / old_name).read_bytes(), old)
                self.assertIn('| Phase I |', index.read_text())
                self.assertNotIn(new_id, index.read_text())
                self.assertIn(good_id, index.read_text())
                self.assertEqual(len(list(out.glob('*.md'))), 2)
                # A subsequent successful sync retries the failed entries.
                args[1] = str(out)
                with patch.object(tracker, 'parse_listing', return_value=listing), \
                     patch.object(tracker, 'fetch_html', side_effect=[
                         'list', DETAIL, DETAIL.replace(RID, new_id), good]):
                    tracker.main(args)
                self.assertIn('| Closed |', (out / old_name).read_text())
                self.assertIn(new_id, index.read_text())
                self.assertEqual(len(list(out.glob('*.md'))), 3)

    def test_other_http_errors_and_listing_500_are_fatal(self):
        for code, listing_failure in ((401, False), (403, False), (404, False),
                                      (503, False), (500, True)):
            with self.subTest(code=code, listing=listing_failure), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                old = root / f'109-{RID}-Old.md'
                old.write_text('original')
                error = tracker.urllib.error.HTTPError('url', code, 'error', {}, None)
                responses = [error] if listing_failure else ['list', error]
                with patch.object(tracker, 'parse_listing', return_value=[(RID, 'detail')]), \
                     patch.object(tracker, 'fetch_html', side_effect=responses):
                    with self.assertRaises(tracker.urllib.error.HTTPError):
                        tracker.main(['--out', str(root)])
                self.assertEqual(old.read_text(), 'original')

    def test_http_500_is_retried_before_propagating(self):
        error = tracker.urllib.error.HTTPError('url', 500, 'Server Error', {}, None)
        with patch.object(tracker.urllib.request, 'build_opener') as build, \
             patch.object(tracker.time, 'sleep') as sleep:
            build.return_value.open.side_effect = error
            with self.assertRaises(tracker.urllib.error.HTTPError):
                tracker.fetch_html(tracker.official_request_url(RID))
            self.assertEqual(build.return_value.open.call_count, 3)
            self.assertEqual(sleep.call_count, 2)

    def test_redirect_does_not_forward_cookie(self):
        handler = tracker.TrackerRedirectHandler()
        req = urllib.request.Request(tracker.DEFAULT_SOURCE_URL, headers={'Cookie': 'secret'})
        with self.assertRaisesRegex(RuntimeError, 'APPLE_DEV_COOKIE'):
            handler.redirect_request(req, None, 302, '', {}, 'https://idmsa.apple.com/signin')

    def test_unsafe_output_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'unrelated.txt').write_text('keep')
            with self.assertRaises(RuntimeError):
                tracker.write_outputs([tracker.parse_detail(DETAIL, RID)], root, root / 'index.md', {})
            self.assertEqual((root / 'unrelated.txt').read_text(), 'keep')


if __name__ == '__main__':
    unittest.main()
