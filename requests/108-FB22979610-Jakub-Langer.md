# FB22979610 — Jakub Langer

| Field | Value |
| --- | --- |
| Developer | Jakub Langer |
| Request ID | FB22979610 |
| Date Received | June 8, 2026 |
| Current Status | Phase I |

## Descriptive Title

Access to host card emulation (HCE) with a persistent, platform-assigned card identifier
readable at the contactless interface — functional parity with the China T-Union transit
credential provisioning in Apple Wallet.

## Request Type

Interoperability Request

## Feature Name

NFC HCE

## Reason for Request

KeVea is developing KeVea Wallet, an iOS application that lets users hold and use contactless
credentials — initially transit cards and access-control cards — on their iPhone. These
credentials work with an existing, deployed base of contactless readers operated by transit
operators and access-control systems, which identify a card by a persistent, stable identifier
presented at the contactless interface. KeVea does not control this reader infrastructure and
cannot modify it.
Standard iOS HCE does not enable an effective solution for this use case: when an iOS app
emulates a card via HCE, the identifier presented to the terminal at the anti-collision/
identification layer is randomized or otherwise not stable per instance, so readers that identify a
card by a persistent identifier cannot recognize the emulated card. We have observed that a
China T-Union credential provisioned into Apple Wallet does present a stable, persistent, per-
instance identifier that such readers recognize, whereas a card emulated through the standard
HCE path does not. This demonstrates the capability exists on the platform but is not available
to developers on equal terms.
KeVea is not requesting the ability to set an arbitrary developer-supplied identifier, and is not
seeking to clone any existing physical card. We request only that the identifier be persistent
and unique per emulated card instance, and we accept that the identifier may be assigned and
managed by Apple/the platform. The KeVea backend will adapt to whatever identifier Apple
assigns.
We need Apple's help because the mechanism that makes this work for T-Union is controlled
by iOS and is not exposed through any public API or documentation available to us.

## Product Description

KeVea Wallet — an iOS application providing a wallet-style interface in which users hold and
manage one or more contactless credentials. The initial supported credential types are:
Transit cards issued by public-transport operators; and
Access-control cards used for physical access (e.g. building/site entry).
Each credential corresponds to a card instance recognized by the existing reader infrastructure
described above.

## How the Product Will Use the Feature

KeVea Wallet will emulate, via HCE, a card instance that presents a persistent, per-instance
identifier to the existing contactless readers, so that a user can tap their iPhone in place of a
physical transit or access card. Each provisioned credential in the app would carry its own
stable identifier, assigned by the platform, allowing the existing readers to identify the instance
exactly as they identify a physical card today — without any change to the reader
infrastructure.

## Where the Product Is/Will Be Offered

European Union

## Other Frameworks Evaluated

KeVea has evaluated the available alternatives and none provides an effective solution:
Standard iOS HCE (CoreNFC / card emulation): Does not allow an emulated card to present a
persistent, stable identifier per instance at the identification layer. The identifier presented to
the terminal is not stable in the way the existing transit and access-control readers require, so
those readers do not recognize the emulated card. This is the central reason standard HCE is
not an effective solution for our use case.
Apple Wallet transit/access program: The capability we need is demonstrably present for China
T-Union credentials in Apple Wallet (a card instance presenting a stable, persistent identifier
recognized by terminals). However, this provisioning path is not available to KeVea as a
developer on equal terms, and there is no public documentation or API that lets us obtain
equivalent functionality.
Modifying the reader infrastructure to identify cards via an application-layer dialog (APDU / ISO
7816-4) instead of a persistent identifier: Not feasible. KeVea does not own or control the
deployed transit and access-control readers and cannot require operators to reconfigure or
replace them.
Issuing physical NFC media to users: This defeats the purpose of a software wallet and does
not provide the software-based interoperability we are seeking; it is a workaround, not an
effective interoperable solution.
Because an equivalent capability already exists on the platform for a third party (T-Union) but is
unavailable to KeVea, and because no public alternative achieves the same effect, we are
requesting effective interoperability under Article 6(7) of the DMA.

## Confidential Treatment

Fully available to other developers

## Additional Information

Request by KeVea for HCE to support emulation of a card instance presenting a persistent,
platform-assigned identifier readable by existing contactless terminals, in parity with existing
Apple Wallet transit credentials.
Attachments

## Communications with Developer

June 10, 2026, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
