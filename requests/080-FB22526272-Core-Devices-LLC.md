# FB22526272 — Core Devices LLC

| Field | Value |
| --- | --- |
| Developer | Core Devices LLC |
| Request ID | FB22526272 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb22526272/](https://developer.apple.com/eu-interoperability-request/fb22526272/) |
| Date Received | April 16, 2026 |
| Current Status | Closed |

## Descriptive Title

Allow 3rd party apps for Bluetooth accessories to start up automatically and stay alive in
background without being killed

## Request Type

Interoperability Request

## Feature Name

iOS app lifecycle

## Reason for Request

Currently, the Pebble iOS app frequently will be killed by iOS while running in the background.
When our app is killed, it can no longer communicate over Bluetooth to a
paired Pebble device. This means that functionality on the watch (like checking the weather,
interacting with an AI assistant, or any other function that requires a
connection to the Pebble Core iOS app) ceases to function until the user unlocks their phone
and manually opens the Pebble app.
We have experimented with various ways of attempting to keep the Pebble app alive in the
background, but inevitably, iOS continues to frequently kill our app. There is
nothing in iOS that will allow the app to permanently be registered to stay alive in the
background.
Apple Watch does not have this problem. It maintains a persistent connection even if the user
force closes the Apple Watch app on iOS. It also starts up in the background
automatically when iOS starts. iOS gives preferential treatment to Apple Watch versus other
third-party connected devices like Pebble.
Additionally, if the user disables Bluetooth in iOS, the Apple Watch can continue to
communicate with the iPhone, even though third-party Bluetooth accessories like Pebble
have their connections severed.

## Product Description

Pebble watches
Pebble Index 01

## How the Product Will Use the Feature

We request that the Pebble app may be treated equally to the Apple Watch app and
connectivity in iOS. It must be able to start in the background when the user starts up
their phone. It should not be possible to kill the Pebble app in the background. The Pebble app
must always be allowed to send and receive data over Bluetooth to a
connected Pebble device.
Also, if the user disables Bluetooth in iOS, we request that third-party accessories like Pebble
continue to function just like Apple Watch and other Apple devices continue
to function with Bluetooth disabled.

## Where the Product Is/Will Be Offered

Worldwide
European Union

## Other Frameworks Evaluated

Yes, we have considered and tried many different approaches to keeping our app alive in the
background. Nothing is 100% reliable, iOS continues to kill our app in the
background at seemingly random times.

## Confidential Treatment

Fully available to other developers
