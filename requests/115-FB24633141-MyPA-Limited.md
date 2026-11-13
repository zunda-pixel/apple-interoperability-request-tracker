# FB24633141 — MyPA Limited

| Field | Value |
| --- | --- |
| Developer | MyPA Limited |
| Request ID | FB24633141 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb24633141/](https://developer.apple.com/eu-interoperability-request/fb24633141/) |
| Date Received | September 3, 2026 |
| Current Status | Closed |

## Descriptive Title

Third-party AI assistant interoperability with iOS

## Request Type

Interoperability Request

## Feature Requested

System assistant functionality, including user selection and invocation of a third-party AI assistant, side-button access, cross-application actions, on-screen context and lock-screen assistant access.

## Reason for Request

MyPA is a voice-based and text-based personal AI assistant. Users can ask MyPA questions and ask it to perform actions on their behalf.

On iOS, MyPA can provide assistant functionality within the MyPA application and expose its own actions using Apple’s available developer frameworks. However, a user cannot currently select MyPA as their preferred system assistant and allow it to perform the same types of system-level assistant tasks across iOS and other compatible applications.

Ideally, a user should be able to choose MyPA as their preferred assistant and invoke it directly through an iOS-supported assistant interaction, such as the iPhone side button. When invoked, MyPA should be able to receive relevant context from iOS and, with the user’s consent, perform compatible actions exposed by other applications.

For example, a user could say, “MyPA, message Richard and tell him I’ll be 20 minutes late.” MyPA would interpret the request and use an iOS-provided mechanism to perform the appropriate messaging action.

A user viewing a restaurant could similarly invoke MyPA and say, “Book this restaurant for 7:30 tomorrow.” iOS could provide the relevant context to MyPA and allow MyPA to use an available application action to complete the request.

We need Apple’s help because these capabilities depend on operating-system functionality that a third-party application cannot implement independently. We are not requesting unrestricted access to other applications, screen contents, hardware or user information. We would expect iOS to continue to control permissions, authentication and access to sensitive information and actions.

## Product Description

MyPA is an existing personal AI assistant available on iOS, Android and the web. MyPA allows users to interact using voice or text and can understand requests, answer questions and perform actions using services and applications available to the user. The MyPA iOS application currently operates within the capabilities available to third-party iOS applications.

## How the Feature Will Be Used

We would like users to be able to deliberately select MyPA as their preferred assistant on iPhone. Once selected, we would like MyPA to receive assistant requests through an iOS-supported invocation mechanism, including an equivalent of the side-button assistant access Apple currently provides to eligible voice-based conversational applications in Japan.

When a user invokes MyPA, we would also like MyPA to be able to receive relevant structured context from iOS and perform compatible actions exposed by other applications through App Intents, App Schemas or an equivalent Apple-controlled framework.

We would also like appropriate assistant requests to be available while the device is locked where iOS permits this.

We expect this functionality to remain subject to iOS security and privacy controls. iOS could determine when user permission or device authentication is required, what contextual information is provided, and which actions are available to MyPA.

## Where Offered

Worldwide — European Union

## Evaluation of Alternatives

We have evaluated the iOS frameworks currently available to third-party applications, including App Intents and App Schemas.

These frameworks allow MyPA to expose its own actions and content to iOS and Siri, but they do not appear to allow a user to select MyPA as their system assistant or allow MyPA to orchestrate compatible actions exposed by other applications.

We have also evaluated invoking MyPA through mechanisms such as Shortcuts and other application launch methods. These can make it easier for a user to open or invoke MyPA, but they do not provide effective interoperability because MyPA remains an individual application rather than a user-selected assistant capable of receiving system context and performing authorised cross-application actions.

We are also aware that Apple provides Side Button Access for eligible third-party voice-based conversational applications in Japan. This appears to provide part of the interoperability we require, but it is not currently available to our users in the European Union.

We have not identified an existing framework or technology that provides an effective alternative for the functionality described in this request.

## Confidentiality

Fully available to other developers

## Additional Information

We are not requesting access to private Siri APIs, unrestricted access to iOS, or unrestricted access to other applications or user data.

Our preferred outcome is an Apple-controlled interoperability mechanism through which a user can deliberately select MyPA as their assistant and grant the permissions required for assistant functionality.

We would be happy for iOS to continue controlling authentication, privacy permissions, access to sensitive information, lock-screen restrictions and which application actions are available to MyPA.

We are aware that Apple already provides Side Button Access for eligible third-party voice-based conversational applications in Japan. We believe this demonstrates one possible approach to part of the requested interoperability and would welcome Apple’s guidance on whether this mechanism could be made available to MyPA users in the European Union.

We are also open to an alternative implementation proposed by Apple if it provides effective interoperability with the system assistant capabilities described in this request while maintaining iOS security, privacy and user control.

## Communications

##### September 4, 2026 — Apple to Developer

Thank you for your interoperability request. It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request. If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.

##### October 1, 2026 — Apple to Developer

Due to the DMA, Apple has not yet been able to ship Siri AI in the EU. Accordingly, we have assessed your request based on the Siri experience currently available in the EU.

We have reviewed your submission and determined that your request falls outside the scope of Article 6(7) DMA because the functionality to which you seek access — the ability to be selected as a default voice assistant — is not a feature of iOS.

We have further determined that your request falls outside the scope of Article 6(7) DMA in respect of side button invocation, contextual information from the device, and the execution of actions exposed by other apps, because the functionality to which you seek access is not available to, or used by, any service or hardware provided by Apple.

For these reasons, we are closing your request and not moving it to the next phase of our interoperability process.

As this determination is based on a non-technical consideration (i.e., whether what is requested constitutes, or is part of, a feature within the meaning of Article 6(7) DMA, or whether it is available to or used by Apple within the meaning of Recital 57 of that Regulation), it is not eligible for the dispute resolution mechanism.

This concludes our Article 6(7) DMA review.

If you have additional questions, you may reach out to us through [Apple Developer Forums](https://developer.apple.com/forums/), [Feedback Assistant](https://developer.apple.com/feedback-assistant/), or a [code-level support request](https://developer.apple.com/support/technical/).
