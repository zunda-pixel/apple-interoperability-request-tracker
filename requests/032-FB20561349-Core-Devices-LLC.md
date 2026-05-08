# FB20561349 — Core Devices LLC

| Field | Value |
| --- | --- |
| Developer | Core Devices LLC |
| Request ID | FB20561349 |
| Date Received | October 7, 2025 |
| Current Status | Phase III |

## Descriptive Title

Allow 3rd party smartwatches to receive full ANCS messages, regardless of homescreen
preview setting

## Request Type

Interoperability Request

## Feature Name

ANCS

## Reason for Request

Currently, ANCS notification messages are only sent to third-party connected devices like
smartwatches if the user has selected Show Previews on lock screen. Apple watch is able to
receive all notifications, regardless of the lock screen setting.
We need Apple to adjust the ANCS feature to always send notifications.

## Product Description

Pebble smartwatch

## How the Product Will Use the Feature

We would use this feature to give users better options about when and whether they would like
to see notifications on their Pebble or not.

## Where the Product Is/Will Be Offered

European Union
United States
Worldwide

## Other Frameworks Evaluated

No other options are available, from what we can see

## Confidential Treatment

Fully available to other developers

## Additional Information

Attachments

## Communications with Developer

October 7, 2025, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
October 27, 2025, from Apple to Developer:
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
October 29, 2025, from Developer to Apple:
Ok please let me know if you have any updates as you proceed with case DMA.100203,
specifically if this feature will not be covered by that case.
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
January 12, 2026, from Developer to Apple:
Will this enable showing notification content even if the user has disabled home screen
previews? Thanks.
January 15, 2026, from Apple to Developer:
Yes, the solution will enable third-party accessories to access notification content regardless of
the setting the user has selected for “Show Previews” on the iPhone.
