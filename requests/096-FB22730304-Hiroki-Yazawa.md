# FB22730304 — Hiroki Yazawa

| Field | Value |
| --- | --- |
| Developer | Hiroki Yazawa |
| Request ID | FB22730304 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb22730304/](https://developer.apple.com/eu-interoperability-request/fb22730304/) |
| Date Received | May 8, 2026 |
| Current Status | Closed |

## Descriptive Title

Public API for _UINavigationBarPalette — a UIKit primitive for attaching a search-filter palette underneath a UINavigationBar / UISearchBar

## Request Type

Interoperability Request

## Feature Requested

UIKit / \_UINavigationBarPalette (private; declared in UIKitCore.framework/\_UINavigationBarPalette.h)

## Reason for Request

\_UINavigationBarPalette is a private UIKit class shipped in UIKitCore.framework on iOS and iPadOS. It is a UIView subclass that participates in the navigation bar’s private layout protocol \_UINavigationBarLayoutParticipating, owned by a UINavigationItem, and configured through properties such as:

* contentView (the developer-supplied content view)
* preferredHeight, minimumHeight
* isPinned / setPinned: (whether the palette stays attached to the bar’s chrome under scroll)
* \_displaysWhenSearchActive / \_setDisplaysWhenSearchActive: (whether the palette stays visible while a UISearchController is active — i.e. whether it functions as a search filter palette)
* \_layoutPriority, \_contentViewMarginType (how the palette is sized within the bar layout)
* transitioning (whether the bar is currently animating the palette in / out)
* owningNavigationItem (the UINavigationItem that hosts the palette)

UINavigationItem exposes private setters / getters for top and bottom palettes (\_topPalette, \_bottomPalette, \_setTopPalette:, \_setBottomPalette:) so a host view controller can attach a palette and have it rendered as part of the bar’s chrome. The bar then coordinates appearance, scroll-edge transitions, animations, and safe-area insets with the palette automatically.

The very existence of \_displaysWhenSearchActive on this class makes the intent explicit: the primitive was built specifically to host filter / chip rows underneath a search bar, and Apple uses it for exactly that purpose in its first-party apps:

* **Photos.app:** Search screen with category tabs below the search field.
* **Mail.app:** Search screen with mailbox / time-range filter chips.
* **Fitness.app:** day-of-week selector bar (S M T W T F S) attached to the navigation bar at the top of the Summary tab, with the bar’s appearance and scroll-edge transitions coordinated with the palette.

Because \_UINavigationBarPalette is private, third-party apps cannot achieve the same search-filter UX, even though the underlying primitive is shipped in every copy of iOS / iPadOS and is referenced from public symbols (UINavigationItem, UINavigationBar, \_UINavigationBarLayoutParticipating).

Per Article 6(7) of the Digital Markets Act (Regulation 2022/1925), Apple must provide free and effective interoperability with software features that are accessed or controlled via iOS / iPadOS and that are used by Apple’s own services. \_UINavigationBarPalette clearly meets that test:

* It is a software feature accessed and controlled via iOS / iPadOS (a UIKitCore class).
* It is used by equivalent Apple services (Music, Notes, Photos, Mail — Music in particular competes directly with third-party music / catalogue apps).
* No public API provides the same functionality (see Other Frameworks Evaluated below).

We therefore request that Apple expose \_UINavigationBarPalette as UINavigationBarPalette (or a functionally equivalent public class) so that third-party developers can attach a palette under a navigation / search bar with the same behavior Apple’s apps enjoy. The set of properties and methods we need is exactly the subset already present in the private class:

* - initWithContentView:
* contentView
* preferredHeight, minimumHeight
* isPinned / setPinned:
* displaysWhenSearchActive / setDisplaysWhenSearchActive: (most important for the search-filter use case)
* UINavigationItem.topPalette / bottomPalette

We are not requesting any new behavior — only access to behavior that already ships in iOS / iPadOS.

## Product Description

VinoGuesser — an upcoming iOS / iPadOS application that we are preparing to release on the App Store. The app’s primary navigation idiom relies on a navigation bar with an attached auxiliary palette directly beneath it.

(App Store URL will be provided once the app is approved for sale.)

## How the Feature Will Be Used

VinoGuesser — an upcoming iOS / iPadOS app that we are preparing to release on the App Store. The app’s primary discovery surface is a search screen with a UISearchController-style search field.

The core interaction in VinoGuesser is searching with attached filters. We want users to be able to:

* Tap the search field at the top of the screen.
* While the search is active, refine the query via a row of filter chips (or a segmented control) directly underneath the search field — exactly the way Apple Music, Notes, Photos, and Mail render their own search-filter rows.
* Continue scrolling the result list while both the search field and the filter palette stay attached to the bar’s chrome (or animate together with it).

Concretely, with a public UINavigationBarPalette we would:

* Create the palette: let palette = UINavigationBarPalette(contentView: filterChipRow)
* Attach it: navigationItem.bottomPalette = palette (or topPalette depending on the design)
* Mark it as a search-filter palette: palette.displaysWhenSearchActive = true
* Optionally pin: palette.pinned = true if we want the filter row to stay visible regardless of scroll position.
* Let UIKit handle the rest — appearance transitions, safe-area insets, scroll-edge boundary, animation coordination with UISearchController.

This is exactly the integration model the private API already supports.

## Where Offered

Worldwide

## Evaluation of Alternatives

Yes. The following public alternatives have been evaluated and are not effective substitutes for the search-filter use case:

* **UINavigationItem.searchController (UISearchController) alone:** exposes only the search field. There is no public API to attach a filter / chip row underneath it, even though Apple’s own apps clearly do exactly that (visible in Music, Notes, Photos, Mail) and the underlying class (\_UINavigationBarPalette) carries a dedicated \_displaysWhenSearchActive flag for this very purpose.
* **UISearchBar.scopeButtonTitles / showsScopeBar:** provides only a narrow segmented-control of scope titles. It cannot host arbitrary chips / sort options / custom controls, has no API for non-segmented layouts, and is visually distinct from the modern filter-chip pattern Apple uses in Music and Notes.
* **UISearchController.searchResultsController returning a results view that includes the filter row:** places the filter inside the results content, not attached to the search bar’s chrome. The filter scrolls away with content, fails to align with scrollEdgeAppearance, and does not match the visual fidelity of Apple’s apps where the filter palette stays attached to the bar.
* **Manually placing a UIView underneath the navigation bar / search bar in the view-controller’s view hierarchy:** does not coordinate with scrollEdgeAppearance, the material / blur boundary, or the \_UINavigationBarLayoutParticipating protocol that drives bar layout. It also forces us to compute and maintain additionalSafeAreaInsets ourselves, which conflicts with UIScrollView.contentInsetAdjustmentBehavior = .automatic, large-title collapse, refresh-control placement, and keyboard avoidance. The custom view does not animate with the navigation bar / search bar on push / pop, hide / show, or search activation.
* **Container view controllers wrapping content in a UIStackView-style layout:** break large-title behavior, require us to reimplement the scroll-edge transition manually, and cause layout reflow on rotation / size class changes.
* **UIToolbar via UIViewController.toolbarItems:** anchored to the bottom of the screen, not under the search bar; does not satisfy the same UI pattern.

In every case, the manual workarounds either fail to match the visual fidelity of Apple’s first-party search screens (scroll-edge transition, material continuity, \_displaysWhenSearchActive semantics) or require us to reimplement the private \_UINavigationBarLayoutParticipating protocol that drives the bar’s layout. The only effective solution is access to the same primitive Apple’s own apps use.

## Confidentiality

Fully available to other developers

## Communications

##### May 13, 2026 — Apple to Developer

Thank you for your interoperability request. It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request. If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.

##### June 10, 2026 — Apple to Developer

We have reviewed your submission and determined that effective interoperability under Article 6(7) DMA exists. Specifically, Apple’s developer tools for iOS and iPadOS — including [SwiftUI](https://developer.apple.com/documentation/swiftui) and [UIKit](https://developer.apple.com/documentation/uikit) — provide the APIs (e.g., UIScrollEdgeElementContainerInteraction) necessary to implement your requested use case.

For this reason, we are closing your request and not moving it to the next phase of our interoperability process.

This concludes our review under Article 6(7) DMA.

If you have additional questions, you may reach out to us through [Apple Developer Forums](https://developer.apple.com/forums/), [Feedback Assistant](https://developer.apple.com/bug-reporting/), or a [code-level support request](https://developer.apple.com/contact/request/code-level-support/).

##### June 18, 2026 — Developer to Apple

I tested Apple’s suggested approach using UIScrollEdgeElementContainerInteraction.

The attached sample places a custom segmented control in a container view above a collection view, then adds UIScrollEdgeElementContainerInteraction to that container:

edgeInteraction.scrollView = listViewController.collectionView  
edgeInteraction.edge = .top  
containerView.addInteraction(edgeInteraction)

This allows the custom container to participate in the scroll edge effect. However, it does not make the container part of the UINavigationBar or UINavigationItem layout lifecycle.

In the sample, the custom container must be manually positioned relative to the view controller’s safe area:

containerView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor).isActive = true

As a result, when prefersLargeTitles is enabled, the custom view does not automatically follow the large-title expansion and collapse behavior. It remains a normal overlay view in the view controller’s hierarchy, rather than a navigation bar palette owned and laid out by the navigation item.

The sample also has to manually adjust the collection view’s content inset and scroll indicator inset:

let inset = containerView.frame.height  
collectionView?.contentInset.top = inset  
collectionView?.verticalScrollIndicatorInsets.top = inset

This demonstrates that UIScrollEdgeElementContainerInteraction only addresses scroll edge effect participation. It does not provide the behavior requested in FB22730304: a first-class navigation item palette that participates in large-title layout, search bar positioning, scroll-edge appearance transitions, safe-area/content-inset management, and navigation push/pop animations.

Could Apple clarify how UIScrollEdgeElementContainerInteraction is intended to make the custom view automatically follow large-title expansion and collapse in the same way as \_UINavigationBarPalette, without manually reimplementing navigation bar layout behavior?
