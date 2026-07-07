# FB22766949 — European Commission - DG DIGIT

| Field | Value |
| --- | --- |
| Developer | European Commission - DG DIGIT |
| Request ID | FB22766949 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb22766949/](https://developer.apple.com/eu-interoperability-request/fb22766949/) |
| Date Received | May 12, 2026 |
| Current Status | Closed |

## Descriptive Title

Request for the availability of private entitlements.

## Request Type

Interoperability Request

## Feature Name

Private entitlements

## Reason for Request

The current mobile threat landscape is characterised by a proliferation of sophisticated, non-
persistent, and zero/one-click exploit chains, such as those identified in the
"Darksword" and "Coruna" frameworks. These attacks operate with high levels of stealth,
frequently cleaning up filesystem artifacts to evade detection. To protect highvalue
enterprise and sovereign environments, defenders require near real-time visibility into system
logging, process behaviour, process crashes, and kernel panics—
indicators that often precede or accompany successful exploitation.
On iOS, every app runs inside a sandbox: an isolated environment that limits its access to the
system, user data, hardware, and other apps. This sandbox is a core part of
Apple’s security model, helping to contain compromise and enforce privacy by default.
Entitlements are signed capabilities embedded in an app’s code signature that
selectively grant access to specific services or privileged behaviours beyond the default
sandbox restrictions. Together, the sandbox and entitlements define what an app is
allowed to do and what parts of the operating system it may interact with.
Third-party developers can request certain entitlements through Apple’s developer provisioning
and code-signing process, typically by enabling supported capabilities in
Xcode or through the Apple Developer portal. However, only a limited subset of entitlements is
available to external developers. Private entitlements are generally reserved
for Apple’s own apps, system components. Apple also has the ability to ship first-party
applications and system components with private entitlements such as
com.apple.private.logging.* or com.apple.private.security.*, which are not generally available to
third-party developers. From a security perspective, this reflects Apple’s
layered trust model, in which the platform owner reserves certain capabilities for code it signs
and controls directly.

## Product Description

The requested interoperability will support a Mobile Threat Detection and Response (MTDR)
Platform designed for large-scale enterprise and government deployments
(10,000+ mobile devices). This platform centralizes system stability, diagnostics, and security
telemetry to identify indicators of compromise (IoCs) across a fleet of
Corporate Owned (Apple supervised devices) and BYOD (user-consented) devices. The
platform serves as centralised defensive hub for Security Operations Centres
(SOCs) (1) to identify hardware and software problems, (2) to detect sophisticated indicators of
compromise (IoC) —such as network activity, application crashes,
unauthorized binary execution, privilege escalation, and lateral movement, (3) to automate the
triage of suspected compromises without requiring the physical recovery of
the device or user intervention and (4) to provide a capability for organizations with high-
security requirements sovereign control over their data, precluding the
transmission of sensitive diagnostic information to external third parties, including the OS
vendor.

## How the Product Will Use the Feature

The product would require to be able to be granted any entitlement, including those starting
with “com.apple.private” :
An unexhaustive list with examples of multiple crucial and relevant entitlements and their
planned use is:
- com.apple.private.logging.*: Grants access to diagnostic logging streams and the unified
logging system, enabling the ingestion of real-time telemetry and system-wide
activity logs.
- com.apple.private.diagnostics : Grants access to diagnostic logging streams and the unified
logging system, enabling the ingestion of real-time telemetry and systemwide
activity logs.
- com.apple.private.xpc.launchd.event-monitor: Permits the monitoring of events managed by
launchd. This is critical for detecting process execution, service activation,
and potential persistence mechanisms.
- com.apple.private.security.storage.DiagnosticReports.*: Enables access to diagnostic
reports. This is critical for knowing why applications may have crashed.
- com.apple.private.audit.*: Enables interaction with the kernel-level audit subsystem (BSM),
providing a record of security-relevant events such as system calls and
authentication attempts.
- com.apple.private.security.*: Provides the capability to access and inspect system-owned
containers and directories typically restricted by the sandbox, essential for file
integrity monitoring.
- com.apple.private.network.*: Allows monitoring of network sockets, providing visibility into
outbound and inbound network metadata and process attribution.
- com.apple.private.xpc.*: Facilitates the management and inspection of launchd jobs, enabling
an EDR agent to verify the integrity of running daemons and background
tasks.

## Where the Product Is/Will Be Offered

European Union

## Other Frameworks Evaluated

Apple provides no alternatives for solving problems caused by entitlement restrictions, as the
platform is architected to enforce these specific limitations. Gaining
unauthorized access would require exploiting system vulnerabilities to root the operating
system; a process that is entirely unsupported and introduces severe risks to
device integrity. Because these methods fundamentally compromise security, there are no
workable options that preserve the stability and protection of the ecosystem.

## Confidential Treatment

Fully available to other developers

## Additional Information

Security and Privacy Safeguards:
- Data Minimization: This request does not seek access entitlements giving access to user
content (emails, photos, messages). It seeks access only to the system-level
diagnostic telemetry that Apple can collect using Apple-only entitlements.
- Enhanced Privacy: By monitoring and therefore better protecting the devices against
sophisticated threat actors the organization ensures that sensitive corporate and
user information is not transmitted to the attackers, thereby also improving privacy of the
people.
- Consent Framework: For supervised devices the consent is implicit by definition. For BYOD
devices, the app possessing these entitlements would only be delivered on
MDM managed devices. The user-consent would therefore be explicit during user enrolment in
the MDM platform, ensuring transparency and compliance with
GDPR/national privacy laws.
Attachments

## Communications with Developer

May 13, 2026, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
June 12, 2026, from Apple to Developer:
Thank you for your request. We understand that you represent the Directorate-General for
Digital Services of the European Commission (DG DIGIT) responsible for digital services that
support other Commission departments and EU institutions. We also understand that your
request seeks interoperability for purposes of providing a Mobile Threat Detection and
Response (MTDR) Platform for a fleet of corporate-owned and BYOD devices of EU staff
working at various Commission departments and EU institutions. Against this background, we
understand that you are not a business user or a provider of services on Apple's platforms and
are therefore ineligible to seek interoperability with hardware and software features controlled
by Apple's operating systems under Article 6(7) of the DMA.
Notwithstanding the above, we have reviewed your submission and determined that your
request would, in any case, fall outside the scope of Article 6(7) DMA because the functionality
to which you seek access — entitlements — is not a feature of iOS or iPadOS.
For these reasons, we are not moving your request to the next phase of our interoperability
process.
As these determinations are based on non-technical considerations (i.e., whether the requestor
is a business user or a provider of services on Apple's platforms; whether what is requested
constitutes, or is part of, a feature within the meaning of Article 6(7) DMA), your request is not
eligible for the dispute resolution mechanism.
This concludes our Article 6(7) DMA review.
Without prejudice to the legal analysis under Article 6(7) DMA set out above, we understand
that our International Business team has been in touch with your organisation to discuss how
we can learn more about and further support where possible your organisation's specific needs
going forward.
If you have additional questions, you may also reach out to us through Apple Developer
Forums, Feedback Assistant, or a code-level support request.
