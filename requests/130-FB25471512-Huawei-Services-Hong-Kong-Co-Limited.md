# FB25471512 — Huawei Services (Hong Kong) Co., Limited

| Field | Value |
| --- | --- |
| Developer | Huawei Services (Hong Kong) Co., Limited |
| Request ID | FB25471512 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb25471512/](https://developer.apple.com/eu-interoperability-request/fb25471512/) |
| Date Received | November 6, 2026 |
| Current Status | Phase I |

## Descriptive Title

Request for OS-Version-Based Adoption of AccessorySetupKit Without Disabling Legacy CoreBluetooth Discovery

## Request Type

Interoperability Request

## Feature Requested

Request for OS-Version-Based Adoption of AccessorySetupKit Without Disabling Legacy CoreBluetooth Discovery

## Reason for Request

Hello Apple Engineering Team,

We are developing an iOS application that connects to wearable devices, including smartwatches and fitness trackers, using Bluetooth Low Energy (BLE).

We would like to adopt AccessorySetupKit on iOS 26.1 and later, particularly its new filterDiscoveryResults capability, while preserving our existing CoreBluetooth discovery and pairing flow on earlier iOS versions.

However, we have encountered a backward-compatibility concern.

According to Apple’s AccessorySetupKit documentation and WWDC24 guidance, once an app declares Bluetooth support through NSAccessorySetupKitSupports in Info.plist, CoreBluetooth discovery becomes restricted to accessories authorized through AccessorySetupKit.

Since Info.plist is statically configured at the application level, developers cannot selectively enable this behavior based on the running iOS version.

Our Desired Behavior:

* **iOS 18 through iOS 26.0:** Continue using the existing CoreBluetooth discovery and pairing flow, including discovery of accessories not yet authorized through AccessorySetupKit.
* **iOS 26.1 and later:** Use AccessorySetupKit with filterDiscoveryResults to discover, filter, and authorize Bluetooth accessories.
* **After pairing:** Continue using CoreBluetooth for BLE communication on all supported iOS versions.

Current Limitation:

Even if AccessorySetupKit APIs are invoked conditionally using #available(iOS 26.1, \*), the static Info.plist declaration affects Bluetooth authorization and discovery behavior on earlier iOS versions.

This makes it difficult for existing applications with a large installed user base to adopt newer AccessorySetupKit features incrementally without changing the established pairing experience for users on older iOS versions.

Feature Request:

Could Apple provide a mechanism that allows developers to selectively enable AccessorySetupKit Bluetooth authorization based on the iOS version?

For example:

* Introduce an OS-version-specific opt-in mechanism for AccessorySetupKit.
* Allow developers to activate AccessorySetupKit Bluetooth authorization at runtime on supported iOS versions.
* Alternatively, preserve legacy CoreBluetooth discovery behavior on older iOS versions while enabling AccessorySetupKit on newer versions.

We fully understand and support Apple’s privacy model, and we are not requesting a way to bypass Bluetooth authorization requirements. Our goal is to maintain the existing permission-based CoreBluetooth workflow on older systems while adopting the newer accessory-specific authorization model on supported systems.

Questions:

* Is there currently any officially supported way to achieve this OS-version-based migration within a single application?
* If not, would Apple consider introducing such a capability in a future iOS release?

This improvement would make it much easier for established wearable-device applications to adopt AccessorySetupKit without disrupting the experience of existing users.

Thank you for your consideration.

## Product Description

N/A

## How the Feature Will Be Used

N/A

## Where Offered

Worldwide — European Union

## Evaluation of Alternatives

N/A

## Confidentiality

Fully available to other developers

## Communications

##### November 11, 2026 — Apple to Developer

Thank you for your interoperability request.

It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request.

If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.
