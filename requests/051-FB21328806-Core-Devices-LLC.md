# FB21328806 — Core Devices LLC

| Field | Value |
| --- | --- |
| Developer | Core Devices LLC |
| Request ID | FB21328806 |
| Date Received | December 12, 2025 |
| Current Status | Fulfilled |

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
June 4, 2026, from Apple to Developer:
In January 2026, we informed you that a solution to your interoperability request regarding iOS
Notifications shipped on December 15, 2025, in an iOS 26.3 beta release in the EU for
developer testing.
We write to update you that we have shipped the final iOS Notifications solution on May 11,
2026, in the EU as part of iOS 26.5. The final solution allows developers to request notification
forwarding from users, forward iOS content from any iOS app that has notifications enabled to
their third-party accessories, and receive notification replies or actions back from the accessory.
Accessories can enable this functionality once they are paired to an iOS device via
AccessorySetupKit (“ASK”).
The AccessoryNotifications framework is based on three extensions that you will need to include
in your accessory’s companion app. More information on the three extensions is available at:
•
https://developer.apple.com/documentation/accessorytransportextension/
accessorydataprovider;
•
https://developer.apple.com/documentation/AccessoryTransportExtension; and
•
https://developer.apple.com/documentation/accessorytransportextension/
accessorytransportsecurity.
The framework enables bidirectional communication for actionable notifications and systemwide
dismissal, and communication to the accessory for Priority Notifications and Notification
Summaries. You will be able to choose which transport technology (Bluetooth, LAN, or internet)
you wish to support to deliver iOS Notifications from your companion app’s extension to your
relevant connected physical device. If you choose to support multiple transport technologies,
then iOS will select the most appropriate available transport to use for delivering the notification.
Once a user has paired their accessory using ASK, you can decide when your companion app
will present a permission prompt and on-boarding UI by calling the
AccessoryNotificationCenter.requestForwarding(for:) API. The user will then have the ability to
select which iOS Notifications are shown on your connected physical device from within your
companion app. Users can also choose to forward iOS Notifications to your accessory within a
menu in the Settings app.
The AccessoryNotifications framework supports forwarding to multiple accessories, including to
multiple paired third-party accessories.
Apple has published technical specifications and documentation for the iOS Notifications
solution, available at:
•
https://developer.apple.com/documentation/accessorynotifications
This concludes our work on your interoperability request, and we will close your request out as
complete.
If you have any questions on the solution we shipped, please reach out to us through Apple
Developer Forums, Feedback Assistant, or a code-level support request, or reply to this
communication and we will direct your request to the appropriate team.
