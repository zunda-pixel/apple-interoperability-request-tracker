# FB22766958 — European Commission - DG DIGIT

| Field | Value |
| --- | --- |
| Developer | European Commission - DG DIGIT |
| Request ID | FB22766958 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb22766958/](https://developer.apple.com/eu-interoperability-request/fb22766958/) |
| Date Received | May 12, 2026 |
| Current Status | Closed |

## Descriptive Title

Request for Interoperability with System Diagnostic and Telemetry Frameworks Equivalent to
the Apple Service Toolkit 2 (AST 2) for Managed Security Operations.

## Request Type

Interoperability Request

## Feature Name

iOS Service Toolkit 3

## Reason for Request

The current mobile threat landscape is characterised by a proliferation of sophisticated, non-
persistent, and zero-click exploit chains, as evidenced by documented
campaigns such as "Darksword" and "Coruna". These attacks frequently bypass standard
operating system protections to achieve kernel-level execution or high-privilege
persistence. Effective defence against such threats requires real-time visibility into system state
and hardware integrity—capabilities that Apple currently reserves for its
internal diagnostic workflows via the Apple Service Toolkit 2 (AST 2) and the Global Service
Exchange (GSX).
Under the Digital Markets Act (DMA), Apple is required to offer interoperability with features
used by or available to Apple’s services or hardware.
Apple currently utilises AST 2, to wirelessly initiate diagnostics and retrieves granular system
health data to verify device status and facilitate the process of supporting
users with problems they may be encountering with their devices (iOS and macOS). Apple
makes available AST 2 to device repair technicians, including technicians that are
not working for Apple, but are working for an authorised repair service provider.
AST2 to is not available to business users, such as enterprises or government agencies that
manage their own fleet of devices, to the same level of features as Apple has.
Current mechanisms provided to third parties, such as the Apple Diagnostics for Self Service
Repair, Mobile Device Management (MDM) queries and manual sysdiagnose
collection, are insufficient for detecting advanced persistent threats (APTs). These methods are
either too high-level, requiring significant manual intervention, or fail to
provide the continuous, scalable data streams necessary to identify indicators of compromise
(IoCs) before data exfiltration occurs. Access to the underlying diagnostic
and telemetry frameworks that power AST 2 is essential to restore the balance between
attacker capabilities and defensive requirements.

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

The interoperability request seeks access to a programmatic interface, integrated with existing
Supervised device frameworks or MDM protocols, that replicates the
diagnostic reach of AST 2. Specifically, the feature would enable:
- The remote, automated initiation of system integrity checks and diagnostic suites without
requiring physical button sequences or user-initiated "Diagnostics Mode".
- Retrieval of operating system telemetry, including active process metadata, network socket
transitions, kernel exception logs, diagnostic logs, and filesystem integrity
markers.
- Access to low-level hardware identifiers and sensor logs to detect hardware-level tampering
or persistence.
- A server-to-server API model allowing an organisation's security operations centre (SOC) to
request and ingest these logs directly into an analysis pipeline, mirroring the
functionality of the GSX diagnostic console.

## Where the Product Is/Will Be Offered

European Union

## Other Frameworks Evaluated

Existing Apple-provided mechanisms have been thoroughly evaluated and deemed technically
insufficient for the requirements of high-assurance security operations:
- Apple Diagnostics for Self Service Repair: The complexity of the process to enter the
diagnostics environment as part of the self-service model requires complex
interaction with physical buttons and power cable making this operationally non-viable for an
organisation managing many devices and supporting users that are not
technical experts.
- Mobile Device Management (MDM): Current MDM commands are restricted to high-level
configuration and basic inventory queries. They provide no visibility into volatile
memory, kernel state, or the fine-grained process telemetry required to detect a zero-day
exploit.
- sysdiagnose: While comprehensive, sysdiagnose is an ad-hoc tool. It does not contain the
same level of detail regarding hardware information and requires complex
physical user interaction to trigger and lacks a remote, automated invocation path for managed
devices.
- Backups: Analysis of iTunes or iCloud backups does not permit to find the same information.
- Apple Support/Retail Diagnostics: Requiring routine security verification for 10,000+ devices
to only be performed by the OS vendor staff with their proprietary AST 2
interface is operationally non-viable and not interoperable.
No reasonable workaround exists within the current public API surface that provides the depth
of system-level visibility available to Apple’s internal diagnostic tools.

## Confidential Treatment

Fully available to other developers
