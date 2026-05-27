# FB22826381 — Gunp Media di Eloisa Brero & C. S.A.S.

| Field | Value |
| --- | --- |
| Developer | Gunp Media di Eloisa Brero & C. S.A.S. |
| Request ID | FB22826381 |
| Date Received | May 21, 2026 |
| Current Status | Phase I |

## Descriptive Title

User-selectable default app for pcast://, itpc://, and podcast:// URL schemes

## Request Type

Interoperability Request

## Feature Name

System-reserved routing of podcast URL schemes (pcast://, itpc://, podcast://)

## Reason for Request

iOS and iPadOS reserve the URL schemes pcast://, itpc://, and podcast:// for handling
exclusively by first-party Apple software (Podcasts.app). Apple has confirmed this in writing in
response to my technical reference query FB22557022: "The Apple iOS and iPadOS operating
systems reserve the URL schemes for pcast://, itpc://, and podcast:// to be handled by first-
party Apple software, for instance Podcasts.app. This setting is statically defined by the
platform, it is not claimed by the first-party app itself, and cannot be overwritten by a
customer-installed app."
As a result, when a user taps a pcast://, itpc://, or podcast:// link — on the web, in an email, in
a message, in an RSS reader, or in any third-party app — iOS always opens Apple Podcasts,
even if the user has installed and prefers a third-party podcast app, and even if the user has
never opened Apple Podcasts. There is no API, entitlement, or user setting that allows a third-
party podcast app to be selected as the handler for these schemes.
This is a feature controlled by the operating system (it is "statically defined by the platform"),
and it is used exclusively by an Apple service (Apple Podcasts). No effective interoperability
currently exists, because the reservation "cannot be overwritten by a customer-installed app." I
therefore need Apple's help to develop an interoperability solution that allows users in the EU
to route these schemes to the podcast app of their choice.
The natural and most user-friendly solution would be to introduce a "Default Podcast App"
category in iOS/iPadOS Settings, analogous to the user-selectable default app categories
Apple has already implemented for browsers, mail, messaging, translation, password
managers, navigation, and calling apps. When a user selects a third-party podcast app as their
default, the system would route pcast://, itpc://, and podcast:// links to that app. I am, however,
not prescriptive about the implementation: any mechanism that allows users to designate a
non-Apple handler for these schemes would achieve effective interoperability.

## Product Description

Castamatic — an iOS podcast client available on the App Store at https://apps.apple.com/app/
castamatic-podcast-player/id966632553, developed by Gunp Media di Eloisa Brero & C.
S.A.S. The app has been available on iOS since 2015, serves users globally including in the
EU, and supports Podcasting 2.0 standards.

## How the Product Will Use the Feature

Castamatic would register as a candidate handler for the pcast://, itpc://, and podcast:// URL
schemes and, when selected by the user as their default podcast app, would receive and
resolve these links: subscribing the user to the referenced podcast feed, or opening the
referenced episode, directly within Castamatic.
Today, Castamatic can already import and subscribe to podcast feeds, but it cannot be the
target of a pcast://, itpc://, or podcast:// link because the system routes these schemes
exclusively to Apple Podcasts. Users who rely on Castamatic must currently work around this
by manually copying feed URLs, because tapping a native podcast link forces them into Apple
Podcasts. An interoperability solution would let Castamatic provide a seamless "tap a podcast
link → it opens in my chosen app" experience that is currently reserved to Apple's own app.

## Where the Product Is/Will Be Offered

European Union
Worldwide

## Other Frameworks Evaluated

Yes. I evaluated the following, and none provides an effective solution:
- Declaring pcast://, itpc://, and podcast:// in Castamatic's CFBundleURLSchemes (Info.plist):
this is the standard mechanism for custom URL schemes, but Apple has confirmed it does not
work for these schemes, which are "statically defined by the platform" and "cannot be
overwritten by a customer-installed app." The reservation operates at the OS level, not at the
app-registration level.
- Universal Links (https-based associated domains): these allow an app to handle its own web
domains, but cannot capture the proprietary pcast://, itpc://, and podcast:// schemes, nor
Apple's own podcasts.apple.com links.
- Manual feed import: Castamatic supports pasting or importing RSS feed URLs, but this
requires the user to leave the linking context, locate the raw feed URL (often not exposed), and
paste it manually — a poor experience compared to the one-tap routing Apple Podcasts
enjoys.
- The DMA "Default Apps" framework: Apple has implemented user-selectable default
categories for browsers, mail, messaging, translation, password managers, navigation, and
calling. No equivalent category exists for podcast apps, so there is currently no setting through
which a user can redirect these schemes.
I confirmed the absence of any public mechanism through technical reference query
FB22557022. Apple's own reference document "About Apple URL Schemes" (https://
developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/
Introduction/Introduction.html), last updated in 2017, does not even list these three schemes
among the reserved schemes, so a third-party developer cannot discover the existence of this
restriction from public documentation.

## Confidential Treatment

Fully available to other developers

## Additional Information

Apple's public reference document "About Apple URL Schemes" (https://developer.apple.com/
library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html),
last updated in 2017, does not list pcast://, itpc://, or podcast:// among the reserved schemes.
A third-party developer therefore cannot discover the existence of this restriction from public
documentation; it was confirmed only through technical reference query FB22557022
(submitted April 20, 2026).
For convenience, the Article 6(7) eligibility criteria are summarized below:
(ii) Feature controlled by iOS/iPadOS: confirmed by Apple as "statically defined by the
platform" (FB22557022).
(iii) Feature available to or used by an Apple service: the reserved routing is used exclusively by
Apple Podcasts (FB22557022).
No effective interoperability exists: the reservation "cannot be overwritten by a customer-
installed app" (FB22557022).
Attachments

## Communications with Developer

May 22, 2026, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
