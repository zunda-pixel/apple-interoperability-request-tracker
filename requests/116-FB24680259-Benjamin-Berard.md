# FB24680259 — Benjamin Berard

| Field | Value |
| --- | --- |
| Developer | Benjamin Berard |
| Request ID | FB24680259 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb24680259/](https://developer.apple.com/eu-interoperability-request/fb24680259/) |
| Date Received | September 6, 2026 |
| Current Status | Closed |

## Descriptive Title

Effective interoperability with iPhone flashlight beam-width and beam-length controls

## Request Type

Interoperability Request

## Feature Requested

Effective interoperability with iPhone flashlight beam-width and beam-length controls

## Reason for Request

Programmatic access to the flashlight beam-width and beam-length controls available through Apple’s system flashlight interface on supported iPhone models.

The requested interoperability should allow an eligible third-party iOS flashlight application to adjust:

* Beam width, from narrow/spot to wide/flood
* Beam length or throw, to the extent independently supported
* Current beam configuration
* Supported ranges or discrete positions
* Hardware capability and availability
* Changes caused by thermal, power, or system restrictions

We are requesting a documented, supported interoperability solution—not access to undocumented or private APIs.

## Product Description

We provide an iOS flashlight and signaling application named LED. The application uses the rear camera torch for steady illumination, variable brightness, strobe patterns, music-responsive lighting, and Morse signaling.

Standard Torch mode directly competes with or provides an alternative to Apple’s system flashlight service.

If the app is not yet released, change the last paragraph to: The application is currently under development and is intended for distribution to iPhone users, including users in the European Union.

## How the Feature Will Be Used

We intend to add a beam-control interface to standard Torch mode. Users would be able to select a narrow, balanced, or wide beam and adjust the beam continuously where supported.

Example uses include:

* A wide beam for illuminating nearby work areas
* A narrow, longer-reaching beam for walking outdoors
* Reduced spill light when reading signs or locating objects
* Accessibility-oriented lighting configurations
* Saving a preferred beam configuration for later use

The feature would only operate after an explicit user action while the application is active.

## Where Offered

Worldwide

## Evaluation of Alternatives

Existing third-party access

Public AVFoundation currently exposes torch availability, activity, mode, and illumination level through APIs such as:

* hasTorch
* isTorchAvailable
* torchMode
* torchLevel
* setTorchModeOn(level:)

We have not found a documented public API that exposes beam width, beam length, beam shape, or an equivalent control.

Adjusting torchLevel changes illumination intensity but does not provide effective interoperability with Apple’s beam-control feature.

Documentation link: <https://developer.apple.com/documentation/avfoundation/capture-device-lighting>

Why current APIs are insufficient

Brightness and beam geometry solve different user needs. Reducing brightness does not create a wider flood beam, and increasing brightness does not create a narrower, longer-reaching beam. Simulating beam profiles by changing torch intensity would misrepresent the underlying behavior and would not provide functionality equivalent to Apple’s system flashlight.

Camera zoom, focus, exposure, and lens-selection APIs affect image capture and do not provide documented control over the physical flashlight beam.

## Confidentiality

Fully available to other developers

## Additional Information

Requested interoperability solution

We request a supported API or equivalent interoperability mechanism that provides:

1. A capability check indicating whether adjustable beam geometry is supported.
2. The supported beam-width and beam-length ranges or positions.
3. Methods for setting beam width and, if distinct, beam length.
4. Properties or callbacks reporting the effective configuration.
5. Error and availability reporting for thermal, battery, camera-use, or system restrictions.
6. Documentation covering supported devices, thread requirements, configuration locking, application lifecycle, and interaction with AVCaptureDevice.
7. App Store-compatible access for qualifying third-party applications distributed to users in the European Union.

A possible API shape could be associated with AVCaptureDevice, but we are not prescribing Apple’s implementation. An entitlement-controlled API would also be acceptable if eligibility requirements are objective, proportionate, transparent, and nondiscriminatory.

Required level of effectiveness

The solution should permit a third-party flashlight application to offer beam adjustment that is functionally equivalent to Apple’s system flashlight on the same supported hardware.

Effective interoperability requires access to actual beam geometry. Brightness-only access, opening or redirecting users to Control Center, or presenting Apple’s flashlight interface would not allow the third-party service to integrate beam control into its own user experience and workflows.

Supported devices requested

All iPhone models on which Apple’s system flashlight exposes adjustable beam width or beam length.

The application will use runtime capability checks and will hide beam controls on unsupported devices. We do not require the feature to be emulated on unsupported hardware.

Avoid claiming that every Dynamic Island device necessarily has the required flash hardware. Let Apple identify the exact capability matrix.

Platforms and versions

Current and future supported versions of iOS in the European Union, beginning with the earliest maintained iOS version on which Apple provides adjustable flashlight beam functionality.

We request forward-compatible capability detection instead of hard-coding specific device models.

Safety and privacy protections

The application can comply with the same relevant operational safeguards applied to public torch-level control, including:

* Requiring deliberate user activation
* Respecting torch availability and system ownership
* Immediately relinquishing control when backgrounded or interrupted
* Respecting thermal and power restrictions
* Avoiding camera or microphone capture solely to control the torch
* Providing warnings for flashing patterns
* Respecting Reduce/Dimming Flashing Lights accessibility preferences
* Not attempting to exceed system-supported beam or brightness limits

The requested feature does not require collection, retention, or transmission of personal data.

Technical information requested

Please provide a technical reference explaining:

* How iOS determines that adjustable beam control is supported
* Whether width and length are independent parameters
* The units, ranges, or discrete positions used
* How beam settings interact with torch brightness
* How thermal restrictions affect available settings
* Whether beam settings are associated with a particular AVCaptureDevice
* How Apple’s system flashlight obtains and changes these values
* Which lifecycle, entitlement, or exclusive-access requirements apply

This information is relevant to determining and implementing an effective interoperability solution under Article 6(7).

Apple permits a separate technical-reference query, so it may be useful to submit this query alongside the main request.

Expected user benefit

Users would be able to use one flashlight application for brightness, beam geometry, signaling, presets, automation, and accessibility-oriented workflows.

The requested access would allow third-party developers to compete through interface design and specialized flashlight functionality without providing a materially inferior beam-control experience on hardware that already supports the feature.

## Communications

##### September 8, 2026 — Apple to Developer

Thank you for your interoperability request. It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request. If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.

##### October 2, 2026 — Apple to Developer

Thank you for your request.

We have reviewed your submission and determined that your request falls outside the scope of Article 6(7) DMA insofar as it concerns control of the flashlight’s beam width. That functionality is not available to or used by any Apple service or hardware. For this reason, we are closing this part of your request and not moving it to the next phase of our interoperability process.

Although this part of your request falls outside the scope of Article 6(7) DMA, we will nonetheless work towards providing access to the flashlight’s beam width control via [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice). This will allow you to build a solution enabling users to adjust the beam width of the flashlight within your app. Once available, this functionality will be documented in the AVCaptureDevice developer documentation.

As to what you describe as beam length or throw, iOS does not provide a separate beam length or throw control. To the extent your request concerns how far the light reaches, this depends on the flashlight’s brightness. With respect to brightness, we have determined that effective interoperability under Article 6(7) DMA exists. Specifically, apps can set and monitor the torch’s illumination level using AVCaptureDevice. For this reason, we are closing this part of your request and not moving it to the next phase of our interoperability process.

Your submission also includes questions seeking technical information, such as how iOS determines whether adjustable beam control is supported, the parameters and ranges used, and how the system flashlight obtains and changes these values. You can submit these as a technical reference query, which details how iOS enables hardware and software features controlled by iOS, through [Feedback Assistant](http://feedbackassistant.apple.com/new?form=interop).

This concludes our Article 6(7) DMA review.

If you have additional questions, you may reach out to us through [Apple Developer Forums](https://developer.apple.com/forums/), [Feedback Assistant](https://developer.apple.com/feedback-assistant/), or a [code-level support request](https://developer.apple.com/support/technical/).
