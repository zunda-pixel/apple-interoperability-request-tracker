# FB22767011 — European Commission - DG DIGIT

| Field | Value |
| --- | --- |
| Developer | European Commission - DG DIGIT |
| Request ID | FB22767011 |
| Date Received | May 12, 2026 |
| Current Status | Closed |

## Descriptive Title

Configurable remote streaming of filtered Unified Logs.

## Request Type

Interoperability Request

## Feature Name

MDM-integrated configuration and remote streaming of filtered Unified Logs.

## Reason for Request

The current mobile threat landscape is characterised by a proliferation of sophisticated, non-
persistent, and zero/one-click exploit chains, such as those identified in the
"Darksword" and "Coruna" frameworks. These attacks operate with high levels of stealth,
frequently cleaning up filesystem artifacts to evade detection. To protect highvalue
enterprise and sovereign environments, defenders require near real-time visibility into system
logging, process crashes, and kernel panics—indicators that often
precede or accompany successful exploitation.
Under the Digital Markets Act (DMA), Apple must offer interoperability with features used by or
available to Apple’s services or hardware.
The Unified Logging system is a core software feature of iOS. The feature is available to
Apple’s services and used by them:
1. Apple has the means to configure, filter and stream these logs to their own servers. For
example, when users have agreed to share diagnostic data with Apple can also
stream a filtered set of logs to their servers.
2. Apple’s developer tools (Xcode, Console, log CLI) allow developers to stream logs from iOS
or iPadOS devices wirelessly to their Mac with Apple’s developer tools
installed. It allows developers to filter logs and to inspect if their app or iOS handling their app
behave as expected.
3. Feedback assistant has the ability to gather logs to send bug reports to Apple.
A critical security asymmetry exists because Apple’s internal diagnostic and security teams
have the ability to ingest and analyse detailed system telemetry to maintain
platform integrity, a capability currently withheld from third-party security providers. This lack of
interoperability prevents the deployment of Enterprise Detection and
Response (EDR) logic, leaving a structural gap in the defence of European enterprise and
government infrastructure.
Third parties do not have access to the Unified Logging system of iOS in a manner that allwos
them to filter and stream logs in a secure manner to third-party server. This
feature would be essential for achieving "effective interoperability" in the context of
professional cybersecurity operations.

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

The product would integrate it into MDM tooling for:
- Upstream Server Definition: The ability to specify a secure remote endpoint for the
transmission of log dat.
- Local access to logs: A third-party app should be able to access the Unified logs to
preprocess logs or to perform local analysis on the logs.
- Structured Filtering: Support for, centrally managed, client-side filtering logic (analogous to
the functionality found in the macOS Console.app or log CLI.
- Frequency: Capability for near real-time streaming to minimize the detection-to-response
gap.

## Where the Product Is/Will Be Offered

European Union

## Other Frameworks Evaluated

We have evaluated all extant Apple-provided mechanisms and found them lacking:
- Standard MDM: Does not provide granular system activity logs; it is limited to state-based
inventory and configuration.
- Local log collect via CLI: Requires physical tethering or a developer environment, which is
operationally impossible for 10,000+ remote users.
- Sysdiagnose: The 24–48 hour log rotation cycle and complex manual interactions required to
trigger and collect the files makes it operationally impossible at scale.
- idevice and lockdownd pairing: Applications such as Protokolle have implemented creative
ways to live steam the logs locally. However, the complex and manual steps to
reach a working configuration makes this option operationally impossible at scale.
No reasonable workaround exists that provides the necessary continuous, remote, and
scalable visibility required for modern defensive cyber operations.

## Confidential Treatment

Fully available to other developers

## Additional Information

Security and Privacy Safeguards:
- Data Minimization: This request does not seek access to user content (emails, photos,
messages). It seeks access only to the system-level diagnostic telemetry that
Apple already collects. By utilizing complex on-device filters, the organization can strictly limit
data collection to security-relevant events, ensuring that personal user data (e.g., PII in
application logs) is never collected and limiting the bandwidth consumption of the centrally
collected logs.
- Enhanced Privacy: All processing of sensitive telemetry remains under the control of the
organization, not a third party, fulfilling the highest standards of the GDPR’s
intent for user protection.
- Consent Framework: For supervised devices the consent is implicit by definition. For BYOD
devices, this telemetry redirection would only be active upon explicit user
enrolment in the MDM platform, ensuring transparency and compliance with GDPR/national
privacy laws.
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
to which you seek access — the ability to remotely access, preprocess, filter and stream iOS
log data in real time to an external server — does not concern a feature of iOS or iPadOS that
is accessed by Apple services or hardware, within the meaning of Article 6(7) DMA.
For these reasons, we are not moving your request to the next phase of our interoperability
process.
As these determinations are based on non-technical considerations (i.e., whether the requestor
is a business user or a provider of services on Apple's platforms; whether what is requested is
available to or used by Apple services or hardware), your request is not eligible for the dispute
resolution mechanism.
This concludes our Article 6(7) DMA review.
Without prejudice to the legal analysis under Article 6(7) DMA set out above, we understand
that our International Business team has been in touch with your organisation to discuss how
we can learn more about and further support where possible your organisation's specific needs
going forward.
If you have additional questions, you may also reach out to us through Apple Developer
Forums, Feedback Assistant, or a code-level support request.
