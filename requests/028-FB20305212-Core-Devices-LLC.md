# FB20305212 — Core Devices LLC

| Field | Value |
| --- | --- |
| Developer | Core Devices LLC |
| Request ID | FB20305212 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb20305212/](https://developer.apple.com/eu-interoperability-request/fb20305212/) |
| Date Received | September 19, 2025 |
| Current Status | Closed |

## Descriptive Title

Enable third-party smartwatches to send SMS, RCS and iMessages

## Request Type

Interoperability Request

## Feature Requested

iOS API to send SMS, RCS and iMessages

## Reason for Request

iOS has an API that allows Apple Watch users to send SMS, RCS and iMessages from their watches.

There is no public iOS API that would enable third-party smartwatches like Pebble to allow their users to send SMS, RCS and iMessages from their watches.

## Product Description

Pebble smartwatch

## How the Feature Will Be Used

We will use this iOS API to enable Pebble smartwatch users to send SMS, RCS and iMessages from their watch.

## Where Offered

Worldwide — European Union, United States

## Evaluation of Alternatives

In the past, Pebble built a hacky solution (<https://www.theverge.com/2015/11/23/9788146/pebble-time-quick-message-reply>) that required iOS users to authenticate with their cell carrier and then used SMS-over-IP APIs to send text messages. The problem was that these sent messages didn’t appear in the Messages app on iOS.

Sounds like Apple has made this hacky solution even more difficult in the interim by requiring users to disable iMessage entirely if they want to use this (as per page 15 of this class action lawsuit against Apple <https://s3.amazonaws.com/jnswire/jns-media/7d/b2/15969695/showtemp_83.pdf>).

## Confidentiality

Fully available to other developers

## Communications

##### September 19, 2025 — Apple to Developer

Thank you for your interoperability request. It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request. If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.

##### October 6, 2025 — Developer to Apple

I see that the status has been changed to ‘Resolution: Investigation complete — Works as currently designed’.

Please share how the current implementation allows for 3rd party smartwatches to have access to the same message sending APIs that 1st party smartwatches have. We would like to use those APIs.

##### October 7, 2025 — Apple to Developer

The status change you received was in error. Your request is still in Phase I — Eligibility review, and we will provide you with an update on that once our review is complete.

##### October 8, 2025 — Developer to Apple

By the way, I am not receiving an email notification when you send me a reply. I have checked my spam folder, I only get an email notification for the initial feedback confirmation. For example, your reply yesterday did not send me an email.

##### October 15, 2025 — Apple to Developer

We have reviewed your submission and determined that your request falls outside the scope of Article 6(7) DMA because the requested feature (sending SMS and RCS messages) is not available to or used by Apple hardware. Your request also seeks access to iMessage, but this is not a feature of iOS or iPadOS within the meaning of Article 6(7).

Though we have determined that your request falls outside the scope of Article 6(7) DMA, we will consider developing a solution outside of the Article 6(7) DMA process to enable third-party hardware to send SMS and RCS messages.

This concludes our DMA Article 6(7) review.
