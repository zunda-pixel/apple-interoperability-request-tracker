# FB22730304 — Hiroki Yazawa

| Field | Value |
| --- | --- |
| Developer | Hiroki Yazawa |
| Request ID | FB22730304 |
| Date Received | May 8, 2026 |
| Current Status | Phase I |

## Descriptive Title

Public API for _UINavigationBarPalette — a UIKit primitive for attaching a search-filter palette
underneath a UINavigationBar / UISearchBar

## Request Type

Interoperability Request

## Feature Name

UIKit / _UINavigationBarPalette (private; declared in UIKitCore.framework/
_UINavigationBarPalette.h)

## Reason for Request

_UINavigationBarPalette is a private UIKit class shipped in UIKitCore.framework on iOS and
iPadOS. It is a UIView subclass that participates in the navigation bar's private layout protocol
_UINavigationBarLayoutParticipating, owned by a UINavigationItem, and configured through
properties such as:
- contentView (the developer-supplied content view)
- preferredHeight, minimumHeight
- isPinned / setPinned: (whether the palette stays attached to the bar's chrome under scroll)
- _displaysWhenSearchActive / _setDisplaysWhenSearchActive: (whether the palette stays
visible while a UISearchController is active — i.e. whether it functions as a search filter palette)
- _layoutPriority, _contentViewMarginType (how the palette is sized within the bar layout)
- transitioning (whether the bar is currently animating the palette in / out)
- owningNavigationItem (the UINavigationItem that hosts the palette)
UINavigationItem exposes private setters / getters for top and bottom palettes (_topPalette,
_bottomPalette, _setTopPalette:, _setBottomPalette:) so a host view controller can attach a
palette and have it rendered as part of the bar's chrome. The bar then coordinates appearance,
scroll-edge transitions, animations, and safe-area insets with the palette automatically.
The very existence of _displaysWhenSearchActive on this class makes the intent explicit: the
primitive was built specifically to host filter / chip rows underneath a search bar, and Apple
uses it for exactly that purpose in its first-party apps:
- Photos.app — Search screen with category tabs below the search field.
- Mail.app — Search screen with mailbox / time-range filter chips.
- Fitness.app — day-of-week selector bar (S M T W T F S) attached to the navigation bar at the
top of the Summary tab, with the bar's appearance and scroll-edge transitions coordinated
with the palette.
Because _UINavigationBarPalette is private, third-party apps cannot achieve the same search-
filter UX, even though the underlying primitive is shipped in every copy of iOS / iPadOS and is
referenced from public symbols (UINavigationItem, UINavigationBar,
_UINavigationBarLayoutParticipating).
Per Article 6(7) of the Digital Markets Act (Regulation 2022/1925), Apple must provide free and
effective interoperability with software features that are accessed or controlled via iOS /
iPadOS and that are used by Apple's own services. _UINavigationBarPalette clearly meets that
test:
- It is a software feature accessed and controlled via iOS / iPadOS (a UIKitCore class).
- It is used by equivalent Apple services (Music, Notes, Photos, Mail — Music in particular
competes directly with third-party music / catalogue apps).
- No public API provides the same functionality (see Other Frameworks Evaluated below).
We therefore request that Apple expose _UINavigationBarPalette as UINavigationBarPalette (or
a functionally equivalent public class) so that third-party developers can attach a palette under
a navigation / search bar with the same behavior Apple's apps enjoy. The set of properties and
methods we need is exactly the subset already present in the private class:
- - initWithContentView:
- contentView
- preferredHeight, minimumHeight
- isPinned / setPinned:
- displaysWhenSearchActive / setDisplaysWhenSearchActive: (most important for the search-
filter use case)
- UINavigationItem.topPalette / bottomPalette
We are not requesting any new behavior — only access to behavior that already ships in iOS /
iPadOS.

## Product Description

VinoGuesser — an upcoming iOS / iPadOS application that we are preparing to release on the
App Store. The app's primary navigation idiom relies on a navigation bar with an attached
auxiliary palette directly beneath it.
(App Store URL will be provided once the app is approved for sale.)

## How the Product Will Use the Feature

VinoGuesser — an upcoming iOS / iPadOS app that we are preparing to release on the App
Store. The app's primary discovery surface is a search screen with a UISearchController-style
search field.
## How the Product Will Use the Feature
The core interaction in VinoGuesser is searching with attached filters. We want users to be able
to:
1. Tap the search field at the top of the screen.
2. While the search is active, refine the query via a row of filter chips (or a segmented control)
directly underneath the search field — exactly the way Apple Music, Notes, Photos, and Mail
render their own search-filter rows.
3. Continue scrolling the result list while both the search field and the filter palette stay
attached to the bar's chrome (or animate together with it).
Concretely, with a public UINavigationBarPalette we would:
1. Create the palette: let palette = UINavigationBarPalette(contentView: filterChipRow)
2. Attach it: navigationItem.bottomPalette = palette (or topPalette depending on the design)
3. Mark it as a search-filter palette: palette.displaysWhenSearchActive = true
4. Optionally pin: palette.pinned = true if we want the filter row to stay visible regardless of
scroll position.
5. Let UIKit handle the rest — appearance transitions, safe-area insets, scroll-edge boundary,
animation coordination with UISearchController.
This is exactly the integration model the private API already supports.

## Where the Product Is/Will Be Offered

Worldwide

## Other Frameworks Evaluated

Yes. The following public alternatives have been evaluated and are not effective substitutes for
the search-filter use case:
- UINavigationItem.searchController (UISearchController) alone — exposes only the search
field. There is no public API to attach a filter / chip row underneath it, even though Apple's own
apps clearly do exactly that (visible in Music, Notes, Photos, Mail) and the underlying class
(_UINavigationBarPalette) carries a dedicated _displaysWhenSearchActive flag for this very
purpose.
- UISearchBar.scopeButtonTitles / showsScopeBar — provides only a narrow segmented-
control of scope titles. It cannot host arbitrary chips / sort options / custom controls, has no
API for non-segmented layouts, and is visually distinct from the modern filter-chip pattern
Apple uses in Music and Notes.
- UISearchController.searchResultsController returning a results view that includes the filter row
— places the filter inside the results content, not attached to the search bar's chrome. The filter
scrolls away with content, fails to align with scrollEdgeAppearance, and does not match the
visual fidelity of Apple's apps where the filter palette stays attached to the bar.
- Manually placing a UIView underneath the navigation bar / search bar in the view-controller's
view hierarchy — does not coordinate with scrollEdgeAppearance, the material / blur boundary,
or the _UINavigationBarLayoutParticipating protocol that drives bar layout. It also forces us to
compute and maintain additionalSafeAreaInsets ourselves, which conflicts with
UIScrollView.contentInsetAdjustmentBehavior = .automatic, large-title collapse, refresh-control
placement, and keyboard avoidance. The custom view does not animate with the navigation
bar / search bar on push / pop, hide / show, or search activation.
- Container view controllers wrapping content in a UIStackView-style layout — break large-title
behavior, require us to reimplement the scroll-edge transition manually, and cause layout reflow
on rotation / size class changes.
- UIToolbar via UIViewController.toolbarItems — anchored to the bottom of the screen, not
under the search bar; does not satisfy the same UI pattern.
In every case, the manual workarounds either fail to match the visual fidelity of Apple's first-
party search screens (scroll-edge transition, material continuity, _displaysWhenSearchActive
semantics) or require us to reimplement the private _UINavigationBarLayoutParticipating
protocol that drives the bar's layout. The only effective solution is access to the same primitive
Apple's own apps use.

## Confidential Treatment

Fully available to other developers

## Additional Information

Attachments
Fitness.jpg
Mail.jpg
Photo.jpg

## Communications with Developer

May 13, 2026, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
