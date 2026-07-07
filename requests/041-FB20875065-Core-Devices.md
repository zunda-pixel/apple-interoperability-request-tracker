# FB20875065 — Core Devices

| Field | Value |
| --- | --- |
| Developer | Core Devices |
| Request ID | FB20875065 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb20875065/](https://developer.apple.com/eu-interoperability-request/fb20875065/) |
| Date Received | October 30, 2025 |
| Current Status | Phase III |

## Descriptive Title

Allow third-party apps to see and change which focus mode is currently activated

## Request Type

Interoperability Request

## Feature Name

Focus Mode

## Reason for Request

As far as we can tell, there is no API for seeing which focus mode is currently active or
programmatically modifying which focus mode is active.

## Product Description

We're building a smart watch called Pebble.

## How the Product Will Use the Feature

Our users would like to have different settings configured on their Pebble depending on which
Focus mode is currently active on their iPhone. For example, users may want certain app
notifications to be displayed if they're in work focus mode, and other notifications might be
displayed if they're not.
We'd also like to allow the user to change the focus mode on their watch, similar to what users
can do with their Apple Watch. Apple Watch.

## Where the Product Is/Will Be Offered

Worldwide
European Union
United States

## Other Frameworks Evaluated

Yes, nothing is available

## Confidential Treatment

Fully available to other developers

## Additional Information

Attachments

## Communications with Developer

November 3, 2025, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
November 26, 2025, from Apple to Developer:
Thank you again for your request.
Following an initial assessment of your request, we are moving your request to the next phase
of our interoperability process. In this phase, the relevant teams will assess whether we are
able to provide an effective interoperability solution and, if so, develop a tentative project plan.
It may be that, despite our best efforts, it will ultimately not be feasible or appropriate to
provide an interoperability solution, including if providing effective interoperability would
compromise the integrity of the operating system. We have also not yet conducted an
assessment of the impact this request would have on Apple’s intellectual property rights. We
will inform you should it not be feasible or appropriate to implement your request.
We expect to have an update for you on this phase by February 2, 2026. In the meantime,
please let us know if you have additional questions.
February 2, 2026, from Apple to Developer:
Thank you again for your request. We are moving your request forward to the next phase of our
interoperability process.
We will expand our APIs to allow for your accessory to render a representation of the focus list,
allow your accessory to change the active focus mode, and allow your accessory to receive
updates when the active focus mode changes.
This is a significant engineering effort as it relies upon the infrastructure we are building in
relation to the iOS notifications technologies that are subject to the European Commission’s
specification proceeding in case DMA.100203. (On March 19, 2025, the European Commission
issued a decision in those proceedings. You can find the measures specified by the European
Commission here, https://ec.europa.eu/commission/presscorner/detail/en/ip_25_816.) We plan
to complete development of this solution by spring 2027, and ship it shortly thereafter. We will
update you once we have shipped it in a beta release.
Please let us know within 5 working days if you have any feedback on the proposed plan.
Should you choose to provide feedback and, based on Apple’s response to your feedback, you
believe that the Project Plan would not provide a solution equally effective compared to the
feature (including any of its functionalities) used by Apple, you will have the opportunity to
initiate a dispute resolution mechanism.
We hope this addresses your request. If we do not hear from you within 5 business days, we
will begin development work in accordance with the plan described above.
February 2, 2026, from Developer to Apple:
I looked through those measures but don't see anything specific to focus modes. Could you
explain more about how the focus mode API would work? Thanks
February 4, 2026, from Apple to Developer:
Apple intends to build the focus mode API in a manner similar to how we are architecting the
Notification Forwarding API, which we communicated to you about on January 7, 2026, in
relation to FB20561349. To the extent Apple will design the focus mode API in a meaningfully
different way, we will provide you with those details in a future communication.
