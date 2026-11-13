# FB22526272 — Core Devices LLC

| Field | Value |
| --- | --- |
| Developer | Core Devices LLC |
| Request ID | FB22526272 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb22526272/](https://developer.apple.com/eu-interoperability-request/fb22526272/) |
| Date Received | April 16, 2026 |
| Current Status | Closed |

## Descriptive Title

Allow 3rd party apps for Bluetooth accessories to start up automatically and stay alive in background without being killed

## Request Type

Interoperability Request

## Feature Requested

iOS app lifecycle

## Reason for Request

Currently, the Pebble iOS app frequently will be killed by iOS while running in the background. When our app is killed, it can no longer communicate over Bluetooth to a paired Pebble device. This means that functionality on the watch (like checking the weather, interacting with an AI assistant, or any other function that requires a connection to the Pebble Core iOS app) ceases to function until the user unlocks their phone and manually opens the Pebble app.

We have experimented with various ways of attempting to keep the Pebble app alive in the background, but inevitably, iOS continues to frequently kill our app. There is nothing in iOS that will allow the app to permanently be registered to stay alive in the background.

Apple Watch does not have this problem. It maintains a persistent connection even if the user force closes the Apple Watch app on iOS. It also starts up in the background automatically when iOS starts. iOS gives preferential treatment to Apple Watch versus other third-party connected devices like Pebble.

Additionally, if the user disables Bluetooth in iOS, the Apple Watch can continue to communicate with the iPhone, even though third-party Bluetooth accessories like Pebble have their connections severed.

## Product Description

Pebble watches

Pebble Index 01

## How the Feature Will Be Used

We request that the Pebble app may be treated equally to the Apple Watch app and connectivity in iOS. It must be able to start in the background when the user starts up their phone. It should not be possible to kill the Pebble app in the background. The Pebble app must always be allowed to send and receive data over Bluetooth to a connected Pebble device.

Also, if the user disables Bluetooth in iOS, we request that third-party accessories like Pebble continue to function just like Apple Watch and other Apple devices continue to function with Bluetooth disabled.

## Where Offered

Worldwide

European Union

## Evaluation of Alternatives

Yes, we have considered and tried many different approaches to keeping our app alive in the background. Nothing is 100% reliable, iOS continues to kill our app in the background at seemingly random times.

## Confidentiality

Fully available to other developers

## Communications

##### April 20, 2026 — Apple to Developer

Thank you for your interoperability request.

It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request.

If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.

##### May 19, 2026 — Apple to Developer

We have reviewed your submission and determined that effective interoperability exists. Specifically, as part of Apple’s implementation of the European Commission’s specification decision in case DMA.100203, developers using the AccessorySetupKit (ASK) starting in iOS 26 are able to benefit from equally effective access as is available to Apple in relation to the background runtime behaviors you have identified in your request. For more information, please see the relevant developer documentation available at <https://developer.apple.com/documentation/accessorysetupkit/> and <https://developer.apple.com/documentation/technotes/tn3115-bluetooth-state-restoration-app-relaunch-rules>.

For this reason, we are closing your request and not moving it to the next phase of our interoperability process.

For completeness, please also note that by the end of 2026, we also expect to complete additional work implementing the European Commission’s specification decision in case DMA.100203 in relation to background execution technologies and regarding an app’s ability to communicate with accessories set up using ASK.

If you have additional questions, you may reach out to us through [Apple Developer Forums](https://developer.apple.com/forums/), [Feedback Assistant](https://developer.apple.com/feedback-assistant/), or a [code-level support request](https://developer.apple.com/support/technical/).

##### May 19, 2026 — Developer to Apple

Unfortunately, that is not acceptable. Older Pebble watch hardware requires using CBPeripheralManager since the watch acts as the BLE server. This was implemented specifically because iOS does not allow IPC between iOS applications, so the watch acts as a server so multiple iOS applications can create connections to it.

Does Apple have plans to make ASK compatible with CBPeripheralManager? Or alternatively do you have plans to make serving GATT services available via ASK? Either of these options would satisfy our requirement and allow this issue to be closed. Thank you

##### May 19, 2026 — Developer to Apple

sorry my engineer has corrected me ‘It’s the other way around: CBPeripheralManager = phone as GATT server, not watch (point stands about asking for compatibility between ASK and either CBPeripheralManager or a replacement)’

##### October 22, 2026 — Apple to Developer

Thank you for contacting us. We are planning to add support for GATT services in AccessorySetupKit in a future iOS release. We will be able to provide further details closer to the release date. This is without prejudice to Apple’s position as to whether your question relates to interoperability with a feature of iOS/iPadOS.

If you have additional questions, you may reach out to us through [Apple Developer Forums](https://developer.apple.com/forums/), [Feedback Assistant](https://developer.apple.com/feedback-assistant/), or a [code-level support request](https://developer.apple.com/support/technical/).
