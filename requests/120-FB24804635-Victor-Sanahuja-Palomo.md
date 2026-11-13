# FB24804635 — Victor Sanahuja Palomo

| Field | Value |
| --- | --- |
| Developer | Victor Sanahuja Palomo |
| Request ID | FB24804635 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb24804635/](https://developer.apple.com/eu-interoperability-request/fb24804635/) |
| Date Received | September 16, 2026 |
| Current Status | Closed |

## Descriptive Title

Developer testing access to Siri AI (App Intents) on iOS and iPadOS for an EU-based developer serving global markets

## Request Type

Interoperability Request

## Feature Requested

Siri AI on iOS 27 / iPadOS 27 — App Intents integration (App Schemas in the .system domain, onscreen awareness / view annotations, and the Spotlight semantic index)

## Reason for Request

I am an EU-based developer (Spain) of taild, a price-tracking app distributed worldwide through the App Store. I have implemented Siri AI support using Apple’s public App Intents framework: .system.open and .system.search schema intents, custom intents, IndexedEntity conformance with Spotlight donation, and appEntityIdentifier view annotations.

Apple’s 8 June 2026 announcement states that developers in the EU cannot test or use Siri AI in their apps on iOS 27, iPadOS 27 or watchOS 27. My users in the United States, United Kingdom and other supported markets will receive Siri AI with my app, but I have no supported way to validate that experience on the platform where they will use it. I can test on macOS 27, where Siri AI is available in the EU, but Mac is not iPhone: onscreen awareness from Safari on iOS, the Action button, Spotlight on iOS and the iPhone Siri presentation cannot be exercised there.

I am not requesting a bypass of the end-user restriction. I am requesting a compliant, Apple-supported route for an EU developer to validate a feature Apple has made mandatory for Siri integration (SiriKit was deprecated at WWDC26) on the devices where non-EU customers will use it.

A DTS engineer directed me to this form in response to a related developer forum question (thread 841638). Feedback Assistant report FB24276767 has been filed on the same issue.

## Product Description

taild (App Store, bundle ID net.taild.taild) — an iPhone app that tracks product prices across online retailers and notifies users of price drops. Available worldwide, localised in English, Spanish, Italian, Japanese and Thai.

## How the Feature Will Be Used

* “Open my Sony headphones in taild” — .system.open schema intent
* “Search taild for coffee machines” — .system.search schema intent
* “What’s the price of my headphones?” — a custom intent returning a spoken price and a snippet
* “Add this to taild” while viewing a product page in Safari — a custom intent whose URL parameter Siri AI fills from onscreen content
* “Add this to my wishlist” — filing a product into a collection
* Products indexed into the Spotlight semantic index with images, prices and retailer keywords, so Siri can resolve “the Amazon headphones” without the user naming the product

The onscreen-awareness case (Safari → “Add this to taild”) is the primary user benefit and is entirely untestable from the EU on iPhone.

## Where Offered

Worldwide

## Evaluation of Alternatives

I have evaluated every route available to an EU developer:

1. **macOS 27:** Siri AI is available in the EU on Mac, and my iPhone app runs there via TestFlight. This is my current primary test environment. It cannot validate iOS-specific behaviour: Safari onscreen awareness on iPhone, the Action button, Spotlight on iOS, or Siri’s iPhone presentation.
2. **iOS Simulator:** Siri AI availability in the Simulator is undocumented; classic Siri is available but does not exercise Siri AI’s language understanding or onscreen awareness.
3. **App Intents Testing framework:** validates intent execution, entity queries and Spotlight indexing, but by design cannot test Siri’s language interpretation, phrase matching or intent selection.

## Confidentiality

Fully available to other developers

## Communications

##### September 17, 2026 — Apple to Developer

Thank you for your interoperability request. It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request. If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.

##### September 23, 2026 — Apple to Developer

We have reviewed your submission and determined that your request falls outside the scope of Article 6(7) DMA because the functionality to which you seek access — testing of Siri AI on iOS and iPadOS — is not a feature of iOS and iPadOS in the EU. Irrespective of how Siri AI may be classified within the meaning of Article 6(7) DMA, Siri AI is currently not available in the EU on iOS and iPadOS, though Apple has been working hard to find a path forward that preserves users’ privacy and security (<https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/>). For this reason, we are closing your request and not moving it to the next phase of our interoperability process.

As this determination is based on a non-technical consideration (i.e., whether what is requested constitutes, or is part of, a feature within the meaning of Article 6(7) DMA), it is not eligible for the dispute resolution mechanism.

This concludes our Article 6(7) DMA review.

Documentation on how to test and verify the behavior of your App Intents code and integrations with available features of iOS and iPadOS is available at <https://developer.apple.com/documentation/appintents/verifying-your-app-intents-implementation>.

If you have additional questions, you may reach out to us through [Apple Developer Forums](https://developer.apple.com/forums/), [Feedback Assistant](https://developer.apple.com/feedback-assistant/), or a [code-level support request](https://developer.apple.com/support/technical/).
