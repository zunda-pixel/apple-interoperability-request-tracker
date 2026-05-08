# FB20296905 — Core Devices LLC

| Field | Value |
| --- | --- |
| Developer | Core Devices LLC |
| Request ID | FB20296905 |
| Date Received | September 18, 2025 |
| Current Status | Phase III |

## Descriptive Title

Ability for 3rd party smartwatches to reply to notifications

## Request Type

Interoperability Request

## Feature Name

Notifications

## Reason for Request

Currently, iOS allows Apple watch users to reply to incoming notifications (https://
support.apple.com/guide/watch/read-messages-apdcf848d29e/watchos). That same
functionality is not exposed to 3rd party smartwatches over ANCS or through any other
method that we know of.

## Product Description

We make Pebble smartwatches.

## How the Product Will Use the Feature

This will enable Pebble users who have an iOS device to be able to reply to notifications from
their Pebble watches, similar to how Apple watch users can reply to notifications.

## Where the Product Is/Will Be Offered

United States
European Union
Worldwide

## Other Frameworks Evaluated

Yes, we use ANCS but it does not expose this functionality.

## Confidential Treatment

Fully available to other developers

## Additional Information

Attachments

## Communications with Developer

September 19, 2025, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
October 15, 2025, from Apple to Developer:
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
We will update you once we have shipped these solutions in a beta release.
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
