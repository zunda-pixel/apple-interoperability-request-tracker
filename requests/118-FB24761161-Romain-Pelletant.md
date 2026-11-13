# FB24761161 — Romain Pelletant

| Field | Value |
| --- | --- |
| Developer | Romain Pelletant |
| Request ID | FB24761161 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb24761161/](https://developer.apple.com/eu-interoperability-request/fb24761161/) |
| Date Received | September 12, 2026 |
| Current Status | Phase I |

## Descriptive Title

Third party continuity app

## Request Type

Interoperability Request

## Feature Requested

Continuity service

## Reason for Request

Interoperability with iPhone cellular call relay functionality currently available to Apple devices through Continuity.

We are developing a non-Apple personal computer operating system and would like users to be able to answer and place cellular calls from their computer when their iPhone is nearby, using a local Wi-Fi connection.

We request an API allowing an explicitly paired and user-authorized third-party device to act as an audio and call-control endpoint for an ongoing cellular call, with functionality equivalent to the call relay capability available between iPhone and Mac/iPad.

We do not require unrestricted access to audio telephony by the iOS application. An OS-mediated encrypted audio endpoint that preserves iOS privacy and security controls would satisfy the interoperability requirement.

## Product Description

Linux app

## How the Feature Will Be Used

Continuity on Linux for calls

## Where Offered

European Union

## Evaluation of Alternatives

No other way to implement continuity calls with privacy and security without a dedicated API and register third part as allowed device for continuity.

## Confidentiality

Fully available to other developers

## Communications

##### September 28, 2026 — Apple to Developer

Thank you for your interoperability request. It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request. If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.

##### October 13, 2026 — Apple to Developer

Thank you for your request FB24761161 regarding continuity call relay. We are working to complete our review of your submission.

We require additional information from you to complete our assessment. We would be grateful therefore if you could please further expand on:

1. Whether you currently offer a product or service with which you intend to use the requested functionality and, if so, how it is made available to users.
2. The current stage of development of this product or service.
3. Whether, and if so when, you plan to offer this product or service commercially, including in the European Union.
4. Any additional information that supports the above positions, such as a website, distribution channels or number of users.

Once this information is provided, we will continue with the review of your submission. As set out in the European Commission’s decision of 19 March 2025 on the process for interoperability requests (case DMA.100204), if we do not receive a response within 3 working days, the period for Apple to conclude the eligibility assessment of your interoperability request and communicate the outcome to you will be suspended accordingly.

##### October 28, 2026 — Apple to Developer

We are following up on our communication that you received on 13 October requesting additional information in order to evaluate your request.

If we do not hear back from you by 3 November, we will close your request as abandoned without any determination as to its eligibility.To adopt this solution, you will need to adopt AccessorySetupKit in order for the user to consent to the necessary permissions allowing the pasteboard to be shared with your accessory.
