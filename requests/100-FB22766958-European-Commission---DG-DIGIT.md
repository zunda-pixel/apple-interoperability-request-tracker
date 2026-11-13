# FB22766958 — European Commission — DG DIGIT

| Field | Value |
| --- | --- |
| Developer | European Commission — DG DIGIT |
| Request ID | FB22766958 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb22766958/](https://developer.apple.com/eu-interoperability-request/fb22766958/) |
| Date Received | May 12, 2026 |
| Current Status | Closed |

## Descriptive Title

Request for Interoperability with System Diagnostic and Telemetry Frameworks Equivalent to the Apple Service Toolkit 2 (AST 2) for Managed Security Operations

## Request Type

Interoperability Request

## Feature Requested

iOS Service Toolkit 3

## Reason for Request

The current mobile threat landscape is characterised by a proliferation of sophisticated, non-persistent, and zero-click exploit chains, as evidenced by documented campaigns such as “Darksword” and “Coruna”. These attacks frequently bypass standard operating system protections to achieve kernel-level execution or high-privilege persistence. Effective defence against such threats requires real-time visibility into system state and hardware integrity—capabilities that Apple currently reserves for its internal diagnostic workflows via the Apple Service Toolkit 2 (AST 2) and the Global Service Exchange (GSX).

Under the Digital Markets Act (DMA), Apple is required to offer interoperability with features used by or available to Apple’s services or hardware.

Apple currently utilises AST 2 to wirelessly initiate diagnostics and retrieves granular system health data to verify device status and facilitate the process of supporting users with problems they may be encountering with their devices (iOS and macOS). Apple makes available AST 2 to device repair technicians, including technicians that are not working for Apple, but are working for an authorised repair service provider.

AST 2 is not available to business users, such as enterprises or government agencies that manage their own fleet of devices, to the same level of features as Apple has.

Current mechanisms provided to third parties, such as the Apple Diagnostics for Self Service Repair, Mobile Device Management (MDM) queries and manual sysdiagnose collection, are insufficient for detecting advanced persistent threats (APTs). These methods are either too high-level, requiring significant manual intervention, or fail to provide the continuous, scalable data streams necessary to identify indicators of compromise (IoCs) before data exfiltration occurs. Access to the underlying diagnostic and telemetry frameworks that power AST 2 is essential to restore the balance between attacker capabilities and defensive requirements.

## Product Description

The requested interoperability will support a Mobile Threat Detection and Response (MTDR) Platform designed for large-scale enterprise and government deployments (10,000+ mobile devices). This platform centralizes system stability, diagnostics, and security telemetry to identify indicators of compromise (IoCs) across a fleet of Corporate Owned (Apple supervised devices) and BYOD (user-consented) devices. The platform serves as centralised defensive hub for Security Operations Centres (SOCs) (1) to identify hardware and software problems, (2) to detect sophisticated indicators of compromise (IoC) —such as network activity, application crashes, unauthorized binary execution, privilege escalation, and lateral movement, (3) to automate the triage of suspected compromises without requiring the physical recovery of the device or user intervention and (4) to provide a capability for organizations with high-security requirements sovereign control over their data, precluding the transmission of sensitive diagnostic information to external third parties, including the OS vendor.

## How the Feature Will Be Used

The interoperability request seeks access to a programmatic interface, integrated with existing Supervised device frameworks or MDM protocols, that replicates the diagnostic reach of AST 2. Specifically, the feature would enable:

* The remote, automated initiation of system integrity checks and diagnostic suites without requiring physical button sequences or user-initiated “Diagnostics Mode”.
* Retrieval of operating system telemetry, including active process metadata, network socket transitions, kernel exception logs, diagnostic logs, and filesystem integrity markers.
* Access to low-level hardware identifiers and sensor logs to detect hardware-level tampering or persistence.
* A server-to-server API model allowing an organisation’s security operations centre (SOC) to request and ingest these logs directly into an analysis pipeline, mirroring the functionality of the GSX diagnostic console.

## Where Offered

European Union

## Evaluation of Alternatives

Existing Apple-provided mechanisms have been thoroughly evaluated and deemed technically insufficient for the requirements of high-assurance security operations:

* **Apple Diagnostics for Self Service Repair:** The complexity of the process to enter the diagnostics environment as part of the self-service model requires complex interaction with physical buttons and power cable making this operationally non-viable for an organisation managing many devices and supporting users that are not technical experts.
* **Mobile Device Management (MDM):** Current MDM commands are restricted to high-level configuration and basic inventory queries. They provide no visibility into volatile memory, kernel state, or the fine-grained process telemetry required to detect a zero-day exploit.
* **sysdiagnose:** While comprehensive, sysdiagnose is an ad-hoc tool. It does not contain the same level of detail regarding hardware information and requires complex physical user interaction to trigger and lacks a remote, automated invocation path for managed devices.
* **Backups:** Analysis of iTunes or iCloud backups does not permit to find the same information.
* **Apple Support/Retail Diagnostics:** Requiring routine security verification for 10,000+ devices to only be performed by the OS vendor staff with their proprietary AST 2 interface is operationally non-viable and not interoperable.

No reasonable workaround exists within the current public API surface that provides the depth of system-level visibility available to Apple’s internal diagnostic tools.

## Confidentiality

Fully available to other developers

## Additional Information

Security and Privacy Safeguards:

* **Data Minimization:** This request does not seek access to user content (emails, photos, messages). It seeks access only to the system-level diagnostic telemetry that Apple already has access to or collects.
* **Enhanced Privacy:** By allowing managing diagnostic and telemetry to a private corporate server, the organization ensures that sensitive metadata about their internal device usage is not transmitted to the OS vendor (Apple), thereby also reducing the external attack surface through a 3rd party and enhancing privacy and data sovereignty.
* **Consent Framework:** For supervised devices the consent is implicit by definition. For BYOD devices, this telemetry redirection would only be active upon explicit user enrolment in the MDM platform, ensuring transparency and compliance with GDPR/national privacy laws.

## Communications

##### May 13, 2026 — Apple to Developer

Thank you for your interoperability request. It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request. If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.

##### June 12, 2026 — Apple to Developer

Thank you for your request. We understand that you represent the Directorate-General for Digital Services of the European Commission (DG DIGIT) responsible for digital services that support other Commission departments and EU institutions. We also understand that your request seeks interoperability for purposes of providing a Mobile Threat Detection and Response (MTDR) Platform for a fleet of corporate-owned and BYOD devices of EU staff working at various Commission departments and EU institutions. Against this background, we understand that you are not a business user or a provider of services on Apple’s platforms and are therefore ineligible to seek interoperability with hardware and software features controlled by Apple’s operating systems under Article 6(7) of the DMA.

Notwithstanding the above, we have reviewed your submission and determined that your request would, in any case, fall outside the scope of Article 6(7) DMA. Specifically, your request seeks to require Apple to create a new functionality on iOS that is not accessed by any Apple services or hardware (i.e., the ability to remotely and without user interaction initiate system integrity checks and diagnostic suites, and access system telemetry, low-level hardware identifiers and sensor logs). For completeness, the Apple Service Toolkit 2 is a cloud-based diagnostic system that requires manual enrollment and does not offer the type of access requested.

For these reasons, we are not moving your request to the next phase of our interoperability process.

As these determinations are based on non-technical considerations (i.e., whether the requestor is a business user or a provider of services on Apple’s platforms; whether what is requested is available to or used by Apple services or hardware), your request is not eligible for the dispute resolution mechanism.

This concludes our Article 6(7) DMA review.

Without prejudice to the legal analysis under Article 6(7) DMA set out above, we understand that our International Business team has been in touch with your organisation to discuss how we can learn more about and further support where possible your organisation’s specific needs going forward.

If you have additional questions, you may also reach out to us through Apple Developer Forums, Feedback Assistant, or a code-level support request.
