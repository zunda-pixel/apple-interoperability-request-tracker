# FB21328806 — Core Devices LLC

| Field | Value |
| --- | --- |
| Developer | Core Devices LLC |
| Request ID | FB21328806 |
| Date Received | December 12, 2025 |
| Current Status | Phase III |

## Descriptive Title

API for routing iOS notifications over external network connection

## Request Type

Interoperability Request

## Feature Name

iOS notifications can be routed to an Apple watch over a wifi or cellular internet connection

## Reason for Request

Apple watch takes advantage of an iOS feature that allows iOS devices to send iOS
notifications over a cellular or wifi connection (see https://support.apple.com/en-by/119601) to
an Apple Watch. There is no similar API that allows 3rd party accessories to work the same
way.

## Product Description

We are building Pebble, a smartwatch. We would like to provide similar functionality to our
users who use their Pebble watch with an iOS device.

## How the Product Will Use the Feature

Pebble watch users would be able to connect their watch to a cellular or wifi network, then
connect over that network to their iOS device and receive notifications, similar to if the Pebble
watch was connected over BLE to the iOS device and receiving ANCS notifications.

## Where the Product Is/Will Be Offered

United States
European Union
Worldwide

## Other Frameworks Evaluated

Nothing else is available, as far as we know.

## Confidential Treatment

Fully available to other developers

## Additional Information

Attachments

## Communications with Developer

December 12, 2025, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
December 16, 2025, from Apple to Developer:
We have reviewed your submission and determined that your request appears to be based on
iOS notifications technologies that are subject to the European Commission’s specification
proceeding in case DMA.100203, focusing on iOS connectivity features and functionalities. On
March 19, 2025, the European Commission issued a decision in those proceedings. You can
find the measures specified by the European Commission here, https://ec.europa.eu/
commission/presscorner/detail/en/ip_25_816.
Apple is moving your request to Phase III of the interoperability request process. We believe
Apple’s work implementing the European Commission’s decision will address the
functionalities concerned by your request. As required by that decision, we expect to complete
that work by June 2026, which is a significant engineering effort, and will proceed on the
timeframes set forth in the EC decision for shipping the solution.
As of this week, we have begun to ship these solutions in a beta release. We will continue to
update you as we ship more of the requested functionalities in beta, as well as when these
solutions fully ship.
December 16, 2025, from Developer to Apple:
I saw the news, great timing! Will Accessory notifications SDK route notifications over Wifi/
LTE? In the docs it seems to mention Bluetooth only. Thanks!
January 5, 2026, from Apple to Developer:
While the solution we recently shipped in a beta release provides support for notification
forwarding over Bluetooth, we can confirm that we will ship future releases that provide
support for notification forwarding over other transport technologies (e.g., Wi-Fi, cellular). As
previously noted, we expect to complete that work by June 2026, and will continue to update
you as we ship more of the requested functionalities in beta.
January 7, 2026, from Apple to Developer:
A solution to your interoperability request regarding iOS Notifications shipped on December 15,
2025, in an iOS 26.3 beta release in the EU for developer testing.
The solution will enable a third-party accessory to receive iOS system notifications using the
Accessory Notifications framework. Once you use this framework to opt into notification
forwarding, iOS will identify your accessory through the reference you receive from
AccessorySetupKit, and will then prompt a user using your accessory for permission to forward
notifications to the accessory from all, or just some, of the apps that the user chooses.
For more information on the solution that is available in beta, please visit https://
developer.apple.com/download/all/ and search for “Accessory Notifications SDK 26.3.0.”
We will endeavor to ship the final solution by June 2026. When the solution ships in a final
release, this will conclude our work on your interoperability request, and we will close your
request as complete.
If you have any questions on the solution that shipped in a beta release for developer testing,
please reply to this communication and we will ensure that we direct assistance appropriately.
