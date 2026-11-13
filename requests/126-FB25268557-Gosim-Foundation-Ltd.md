# FB25268557 — Gosim Foundation Ltd

| Field | Value |
| --- | --- |
| Developer | Gosim Foundation Ltd |
| Request ID | FB25268557 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb25268557/](https://developer.apple.com/eu-interoperability-request/fb25268557/) |
| Date Received | October 20, 2026 |
| Current Status | Phase I |

## Descriptive Title

Make JavascriptCore usable for an alternative Web engine

## Request Type

Interoperability Request

## Feature Requested

JavascriptCore

## Reason for Request

In order to develop a competitive alternative Web engine for IOS, one needs to be able to use the on-system Javascript engine in a way that is Web compatible.

Without this feature, one needs to bundle a Javascript engine in the app itself, thereby increasing the size of the app and making it less competitive.

JavascriptCore is a public API on IOS, however it offers only a limited amount of functionality compared to the private API used by Safari. With the current limited public API, it is not possible to use JavascriptCore in a Web compatible way.

I therefore need Apple’s help in the form of an expanded public API that would allow third-party developers like myself to use the system JavascriptCore in a Web compatible way.

## Product Description

I am building a Web engine, and making it usable on IOS is a specific goal of the project.

The project is hosted at <https://github.com/gterzian/formal-web>

## How the Feature Will Be Used

Use JavascriptCore as the Javascript engine in a Web compatible alternative Web engine on IOS.

## Where Offered

European Union

## Evaluation of Alternatives

My engine supports multiple Javascript engine, such as Boa and V8, by using them in a modular way behind a generic interface. Those engines work well because they offer the kinds of API one needs to be Web compatible.

I believe that Webkit’s JSC-only port should work as well, although I haven’t tried yet. The problem with that approach is that it also requires bundling JSC into the app, just like with other engines. My goal is to use the system Javascript engine so as to reduce the binary size of an app using an alternative Web engine.

## Confidentiality

Fully available to other developers

## Additional Information

My findings regarding the system JSC can be found at <https://github.com/gterzian/formal-web/tree/d9fbd7c9b14375ed93843c040cf0e64787b6a2f5/js_engine/src/jsc>

## Communications

##### October 21, 2026 — Apple to Developer

Thank you for your interoperability request.

It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request.

If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.
