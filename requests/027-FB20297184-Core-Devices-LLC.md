# FB20297184 — Core Devices LLC

| Field | Value |
| --- | --- |
| Developer | Core Devices LLC |
| Request ID | FB20297184 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb20297184/](https://developer.apple.com/eu-interoperability-request/fb20297184/) |
| Date Received | September 18, 2025 |
| Current Status | Phase III |

## Descriptive Title

Ability for 4rd party apps to communicate with 3rd party smartwatches via IPC

## Request Type

Interoperability Request

## Feature Name

Inter-process communication between apps

## Reason for Request

Currently, iOS developers can create an iOS app that connects with a companion Apple watch
app via the iOS WatchConnectivity framework. For example, Strava has an iOS app and an
Apple watch app. The iOS app uses IPC to communicate with the WatchConnectivity
framework, which in turn routes messages over Bluetooth, Wifi or cellular connection to the
companion app running on the user's Apple watch. This works even when the user's iPhone is
locked and the Strava app is backgrounded.
We make Pebble smartwatches. We want to offer the same functionality to iOS developers who
want to make iOS applications that connect to companion apps running on Pebble.
There is no equivalent IPC method available for us to use.

## Product Description

Pebble smartwatches

## How the Product Will Use the Feature

We want to enable iOS app developers to create companion Pebble smartwatch applications
and communicate with them via IPC in the background.

## Where the Product Is/Will Be Offered

United States
European Union
Worldwide

## Other Frameworks Evaluated

Yes, in the past Pebble era, we had implemented a 'PebbleKit iOS' library which enabled apps
to implement Pebble's BLE protocol, each app was a separate GATT server and create a
connection over BLE to a connected Pebble. This had numerous problems:
- it was hard to keep the iOS app in sync with the Pebble companion app because
communication was not routed through the main Pebble app, instead each app had to create a
separate GATT connection. Unlike the Apple watch solution, which enables apps to use native
iOS apis to talk to WatchConnectivity framework, which intelligently routes data over the best
connectivity method (wifi, bluetooth, cellular) automatically.
- 4th party developers were forced to include a large complex library in their apps, which was
impossible for them to test in their existing CI pipelines/etc because it required hardware in the
loop.
- background processing was very fragile, iOS apps would regularly get killed in background
and not continue communicating with connected Pebbles.
Another option would be to route IPC from a over the internet and then back to our primary
Pebble app via APNS. But this does not work without an internet connection.

## Confidential Treatment

Fully available to other developers

## Additional Information

https://github.com/pebble/pebble-ios-sdk
https://developer.rebble.io/guides/communication/using-pebblekit-ios
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
background execution technologies that are subject to the European Commission’s
specification proceeding in case DMA.100203, focusing on iOS connectivity features and
functionalities. On March 19, 2025, the European Commission issued a decision in those
proceedings. You can find the measures specified by the European Commission here, https://
ec.europa.eu/commission/presscorner/detail/en/ip_25_816.
Apple is moving your request to Phase III of the interoperability request process. We believe
Apple’s work implementing the European Commission’s decision will address the
functionalities concerned by your request. As required by that decision, we expect to complete
that work by the end of 2026, which is a significant engineering effort, and will proceed on the
timeframes set forth in the EC decision for shipping the solution.
We will update you once we have shipped these solutions in a beta release.
October 29, 2025, from Developer to Apple:
I don't think my request is specifically around the background execution. It's more around IPC
between iOS apps. Are you 100% sure that this functionality is going to be released in case
DMA.100203?
I don't think it's valid for us to wait more than a year for this functionality, unless we are certain
that it will be included. Otherwise we will need to push for it to be investigated and potentially
built separately.
November 27, 2025, from Developer to Apple:
Any response to this question?
December 11, 2025, from Apple to Developer:
We re-reviewed your request and confirm that your request is subject to the European
Commission’s specification proceeding in case DMA.100203. The relevant section of the
proceeding decision that covers Apple’s work is the section on Background Execution,
particularly paragraph 34 of the proceeding decision as it relates to functionalities for iOS sister
apps and iOS companion apps. As previously noted we expect to complete that work by the
end of 2026.
