import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import call, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import sync_prs

URL = 'https://github.com/example/tracker/pull/123'
MERGE = ['gh', 'pr', 'merge', URL, '--squash', '--delete-branch']


class MergeRetryTests(unittest.TestCase):
    def invoke(self):
        sync_prs.open_and_merge_pr(base='main', branch='auto/test', title='Update', body='Test')

    def test_success_without_retry(self):
        with patch.object(sync_prs, 'run', side_effect=[URL, '']) as run, \
             patch.object(sync_prs.time, 'sleep') as sleep:
            self.invoke()
        self.assertEqual(run.call_count, 2)
        self.assertEqual(run.call_args, call(MERGE, capture=True))
        sleep.assert_not_called()

    def test_same_pr_retried_for_base_change(self):
        for stream in ('stderr', 'output'):
            with self.subTest(stream=stream):
                error = subprocess.CalledProcessError(1, MERGE, **{stream: sync_prs.BASE_MODIFIED_ERROR})
                with patch.object(sync_prs, 'run', side_effect=[URL, error, error, '']) as run, \
                     patch.object(sync_prs.time, 'sleep') as sleep:
                    self.invoke()
                self.assertEqual(run.call_args_list[1:], [call(MERGE, capture=True)] * 3)
                self.assertEqual(sleep.call_args_list, [call(5), call(10)])
                self.assertEqual(sum(c.args[0][2] == 'create' for c in run.call_args_list), 1)

    def test_exhaustion_raises_original_error(self):
        error = subprocess.CalledProcessError(1, MERGE, stderr=sync_prs.BASE_MODIFIED_ERROR)
        with patch.object(sync_prs, 'run', side_effect=[URL, error, error, error]) as run, \
             patch.object(sync_prs.time, 'sleep') as sleep:
            with self.assertRaises(subprocess.CalledProcessError) as raised:
                self.invoke()
        self.assertIs(raised.exception, error)
        self.assertEqual(run.call_count, 4)
        self.assertEqual(sleep.call_count, 2)

    def test_other_merge_errors_are_not_retried(self):
        for message in ('Merge conflict', 'Resource not accessible by integration', None):
            with self.subTest(message=message):
                error = subprocess.CalledProcessError(1, MERGE, stderr=message)
                with patch.object(sync_prs, 'run', side_effect=[URL, error]) as run, \
                     patch.object(sync_prs.time, 'sleep') as sleep:
                    with self.assertRaises(subprocess.CalledProcessError):
                        self.invoke()
                self.assertEqual(run.call_count, 2)
                sleep.assert_not_called()

    def test_matching_unresolved_pr_retries_same_url(self):
        message = 'GraphQL: Could not resolve to a PullRequest with the number of 123. (repository.pullRequest)'
        for stream in ('stderr', 'output'):
            for exhausted in (False, True):
                with self.subTest(stream=stream, exhausted=exhausted):
                    error = subprocess.CalledProcessError(1, MERGE, **{stream: message})
                    results = [URL, error, error, error if exhausted else '']
                    with patch.object(sync_prs, 'run', side_effect=results) as run, \
                         patch.object(sync_prs.time, 'sleep') as sleep:
                        if exhausted:
                            with self.assertRaises(subprocess.CalledProcessError) as raised:
                                self.invoke()
                            self.assertIs(raised.exception, error)
                        else:
                            self.invoke()
                    self.assertEqual(run.call_args_list[1:], [call(MERGE, capture=True)] * 3)
                    self.assertEqual(sleep.call_args_list, [call(5), call(10)])
                    self.assertEqual(run.call_count, 4)

    def test_unresolved_pr_must_match_created_number_exactly(self):
        for number in ('12', '1234', '124'):
            with self.subTest(number=number):
                message = f'GraphQL: Could not resolve to a PullRequest with the number of {number}. (repository.pullRequest)'
                error = subprocess.CalledProcessError(1, MERGE, stderr=message)
                with patch.object(sync_prs, 'run', side_effect=[URL, error]) as run, \
                     patch.object(sync_prs.time, 'sleep') as sleep:
                    with self.assertRaises(subprocess.CalledProcessError):
                        self.invoke()
                self.assertEqual(run.call_count, 2)
                sleep.assert_not_called()

    def test_creation_failure_is_not_retried(self):
        error = subprocess.CalledProcessError(1, ['gh', 'pr', 'create'], stderr=sync_prs.BASE_MODIFIED_ERROR)
        with patch.object(sync_prs, 'run', side_effect=error) as run, \
             patch.object(sync_prs.time, 'sleep') as sleep:
            with self.assertRaises(subprocess.CalledProcessError):
                self.invoke()
        run.assert_called_once()
        sleep.assert_not_called()
