# FB23814187 — Steffen Groß

| Field | Value |
| --- | --- |
| Developer | Steffen Groß |
| Request ID | FB23814187 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb23814187/](https://developer.apple.com/eu-interoperability-request/fb23814187/) |
| Date Received | July 17, 2026 |
| Current Status | Closed |

## Descriptive Title

System Dictation (Apple Keyboard Dictation) / System Keyboard Voice Input

## Request Type

Interoperability Request

## Feature Requested

System Dictation (Apple Keyboard Dictation) / System Keyboard Voice Input

## Reason for Request

I have developed an advanced speech-to-text solution that provides an alternative to Apple’s built-in dictation service.

My product requires interoperability with the iOS system keyboard dictation feature so that users can choose my speech recognition service instead of Apple’s implementation while keeping the native Apple keyboard experience.

There is currently no documented API or supported mechanism that allows a third-party speech recognition provider to integrate into the system dictation workflow. Without such interoperability, users cannot freely choose an alternative dictation provider.

## Product Description

A cloud-based and on-device speech recognition platform providing high-quality real-time dictation.

The solution is designed for consumers, enterprise customers and accessibility use cases. It supports multiple languages, domain-specific vocabularies, custom language models and privacy-focused processing.

The product is available as APIs and applications and is intended to become an alternative system-wide dictation provider on iOS.

## How the Feature Will Be Used

The product would receive audio captured through the existing system dictation user interface, perform speech recognition using its own speech-to-text engine and return the recognized text back to the active text input field.

The user experience should remain identical to the current Apple keyboard dictation workflow, with the only difference being that the speech recognition backend is provided by a user-selected third-party provider.

Users should be able to configure the preferred dictation provider in iOS settings in the same way they can choose default applications for other supported categories.

## Where Offered

Worldwide — European Union

## Evaluation of Alternatives

Yes. We evaluated alternatives but none of these technologies provides interoperability with the native Apple keyboard dictation function or allows users to replace the built-in dictation provider while preserving the system keyboard experience.

Therefore, an interoperability solution under Article 6(7) DMA is required.

## Confidentiality

Fully available to other developers

## Additional Information

The dictation feature will use our own speech recognition and transcription backend. We only require access to the system dictation integration points so that users can invoke our service through the native Apple keyboard dictation button instead of Apple’s speech recognition service. The Apple keyboard, text input system, and overall user experience would remain unchanged; only the speech-to-text provider would be user-selectable. This interoperability is requested pursuant to Article 6(7) of Regulation (EU) 2022/1925 (Digital Markets Act).

## Communications

##### July 22, 2026 — Apple to Developer

Thank you for your interoperability request.

It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request.

If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.

##### August 13, 2026 — Apple to Developer

We have reviewed your request and determined that it falls outside the scope of Article 6(7) DMA because the functionality to which you seek access — the iOS system keyboard’s dictation entry point — is not a feature of iOS. For this reason, we are closing your request and not moving it to the next phase of our interoperability process.

As this determination is based on a non-technical consideration (i.e., whether what is requested constitutes, or is part of, a feature within the meaning of Article 6(7) DMA), it is not eligible for the dispute resolution mechanism.

This concludes our Article 6(7) DMA review.

We would like to add some context that may be helpful. Apple already provides a means for developers to deliver speech recognition experiences to users, including in ways that allow developers to use their own recognition backend:

* Use Apple’s public Speech framework to perform speech-to-text transcription on live or prerecorded audio within your app (<https://developer.apple.com/documentation/speech/>).
* An app can request permission to capture audio directly from the device microphone and route it to its own on-device or cloud-based speech recognition engine (<https://developer.apple.com/documentation/avfoundation/requesting-authorization-to-capture-and-save-media>).
* An app can build a custom keyboard extension to provide system-wide, customized text input. This allows an app to integrate its own dictation button and route voice input directly to its own speech recognition service (<https://developer.apple.com/documentation/uikit/creating-a-custom-keyboard>). Additionally, when providing its own dictation interface, an app can configure its custom keyboard to hide the system keyboard’s dictation button to prevent a duplicate user experience (<https://developer.apple.com/documentation/uikit/configuring-a-custom-keyboard-interface>).

If you have additional questions, you may reach out to us through [Apple Developer Forums](https://developer.apple.com/forums/), [Feedback Assistant](https://developer.apple.com/feedback-assistant/), or a [code-level support request](https://developer.apple.com/support/technical/).
