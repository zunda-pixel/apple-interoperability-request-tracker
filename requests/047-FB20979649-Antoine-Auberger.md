# FB20979649 — Antoine Auberger

| Field | Value |
| --- | --- |
| Developer | Antoine Auberger |
| Request ID | FB20979649 |
| Date Received | November 10, 2025 |
| Current Status | Closed |

## Descriptive Title

Open access to iOS mail push notifications

## Request Type

Interoperability Request

## Feature Name

Open access to iOS mail push notifications

## Reason for Request

Our request concerns interoperability with Apple’s iOS Mail application, specifically regarding
push email delivery via the Apple Push Notification Service (APNS).
Currently, the ability to deliver real-time push notifications to the native iOS Mail app is
restricted to a small number of email service providers (e.g., iCloud, Microsoft Exchange,
Yahoo, etc.) who possess valid APNS certificates with the topic
com.apple.mobilemail.push.xxx.
Other independent or self-hosted mail providers — even those operating fully standards-
compliant IMAP/SMTP infrastructure (such as Dovecot and Postfix) — are unable to obtain
such certificates or integrate via any documented public API.
This restriction effectively prevents fair competition and blocks users from receiving timely mail
notifications when using iOS Mail with independent mail servers, which were previously
supported through the legacy Apple Mail push API inherited from macOS Server.
Since this internal API was discontinued and no public replacement is available, interoperability
with iOS Mail has become technically impossible for third-party or self-hosted email services.
We therefore request Apple’s assistance to develop a compliant, transparent, and non-
discriminatory interoperability solution that allows independent mail providers to implement
push email notifications for iOS Mail under equal technical conditions.

## Product Description

Our product is a standards-compliant email service based on open-source mail technologies
such as:
Dovecot (IMAP/POP3 server)
Postfix (SMTP server)
Let’s Encrypt / Lego (TLS certificate management)
The service is self-hosted under private domain and is used by end users on various platforms,
including macOS and iOS Mail clients.
The same infrastructure already provides IMAP IDLE and SMTP Submission capabilities
consistent with open standards (RFC 3501, RFC 2177, RFC 6409).
However, IMAP IDLE alone cannot offer equivalent push efficiency on iOS due to the system’s
strict background execution limitations — making APNS integration the only viable way to
achieve real-time mail notifications.

## How the Product Will Use the Feature

Our mail service seeks to:
- Obtain or generate valid APNS certificates for the topic
com.apple.mobilemail.push.<domain> to enable secure push notifications for our mail users on
iOS Mail.
- Send push notifications via APNS when new mail arrives on the IMAP server, following the
same protocol and security standards used by other authorized providers.
- Provide an open and interoperable solution for iOS users who wish to use their self-hosted or
independent mail accounts with native mail push functionality, in compliance with the
principles of the EU Digital Markets Act (DMA).
This functionality directly impacts user choice, energy efficiency, and service parity with major
providers who already enjoy privileged access.

## Where the Product Is/Will Be Offered

Worldwide
European Union

## Other Frameworks Evaluated

N/A

## Confidential Treatment

Fully available to other developers

## Additional Information

Access has recently been granted to other developers on an ad-hoc basis with manual issuing
of push certificates.
We request a full self-service certificate signing platform equivalent to what was available
before with MacOS Server, or/and to provide technical documentation or an application
process to obtain ad-hoc valid APNS Mail push certificates for those who need it (e.g contact
form/email) while such platform is being developed.
Attachments

## Communications with Developer

November 10, 2025, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
November 21, 2025, from Apple to Developer
Thank you again for your request.
We have reviewed your submission and determined that your request falls outside the scope of
Article 6(7) DMA because it does not seek access to or interoperability with a feature of iOS or
iPadOS. Rather, the requested functionality (iOS Mail push notifications) involves integration
with the iOS Mail app. For this reason, we are not moving your request to the next phase of our
interoperability process.
Separately, we would like to follow up with you about the functionality you are seeking outside
of the Article 6(7) DMA process, so our teams can discuss existing capabilities available to
developers, and explore potential enhancements. A member of our Developer Relations team
will reach out to your team.
As this determination is based on a non-technical consideration (i.e., whether what is
requested constitutes a feature within the meaning of Article 6(7) DMA), it is not eligible for the
dispute resolution mechanism.
This concludes our review under Article 6(7) DMA.
