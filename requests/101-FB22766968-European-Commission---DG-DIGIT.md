# FB22766968 — European Commission - DG DIGIT

| Field | Value |
| --- | --- |
| Developer | European Commission - DG DIGIT |
| Request ID | FB22766968 |
| Date Received | May 12, 2026 |
| Current Status | Phase I |

## Descriptive Title

iOS Endpoint Security Framework and System Event Telemetry APIs for Enterprise Threat
Detection and Response.

## Request Type

Interoperability Request

## Feature Name

iOS Endpoint Security Framework and System Event Telemetry APIs.

## Reason for Request

The security model of iOS, while robust against conventional malware, is increasingly bypassed
by Advanced Persistent Threats (APTs) such as the Darksword and Coruna
exploit chains. These threats employ zero-click delivery vectors and reside entirely within the
address space of legitimate processes (e.g., com.apple.WebKit.WebContent
or imagent) using techniques such as Return-Oriented Programming (ROP) and Just-In-Time
(JIT) memory corruption.. Current third-party security agents are confined to
the Sandbox via the Mandatory Access Control Framework (MACF) and lack the necessary
visibility into the kernel and system-level daemons to detect these memoryresident
threats. Without access to low-level system API functions , third-party security tools cannot
identify anomalous behaviours such as unauthorised task_for_pid()
calls, pointer authentication code (PAC) failures, or unexpected Page Protection Layer (PPL)
violations, and therefore cannot achieve the "effective" interoperability
required to protect 10,000+ managed devices against advanced persistent threats (APTs).
Under the Digital Markets Act (DMA), Apple must offer interoperability with features used by or
available to Apple’s services or hardware.
Apple currently maintains platform integrity through internal telemetry and private entitlements
that are inaccessible to third parties. This creates a critical asymmetry in the
following areas:
- Process Lifecycle and Execution: Apple utilises RunningBoard and launchd to manage and
monitor process states, including the execution of posix_spawn() and exec()
calls. Third-party security tools require equivalent access to these signals to validate binary
signatures and behaviour in real-time.
- Trust and Integrity Signals: Components such as trustd and securityd evaluate system-wide
certificate trust and entitlement validity. The inability of third-party tools to
interoperate with these daemons prevents the detection of compromised or revoked
certificates used in man-in-the-middle (MitM) attacks.
- Vnode and File System Telemetry: Monitoring for modifications in sensitive directories such
as /private/var/db/ or /private/var/root/ where exploit artifacts or configuration
profiles may be staged. Identifying the creation of unauthorised LaunchDaemons or
LaunchAgents. Access to kernel-level FSEvents or an equivalent to the macOS
EndpointSecurity framework to observe file operations in real-time without the overhead of
manual polling.
- Network Activity and attribution: Current iOS NetworkExtensions do not provide the
granularity required to attribute traffic to specific system-level actors. Parity requires
process-to-socket mapping enabling the detection of exfiltration by system daemons; XPC
auditing and access to NECP parity signals to identify bypasses of system-level
firewalls or VPNs.
The lack of real-time visibility into process execution, memory integrity, and anomalous
network flows originating from system daemons constitutes a critical security risk.
As Apple can use these internal signals to maintain platform integrity, denying equivalent
access to enterprise-managed security agents prevents the implementation of a
defensive posture commensurate with the risk profile of government and high-value corporate
environments. This request seeks to bridge the gap between the internal
monitoring capabilities Apple reserves for itself and the "effective" interoperability required by
third-party providers under the DMA.

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

The interoperability request is for a restricted, entitlement-based API on iOS, functionally
equivalent to the macOS Endpoint Security (ES) framework. This feature would
enable a verified on-device agent, deployed and configured via MDM, to subscribe to specific
system events in near real-time.

## Where the Product Is/Will Be Offered

European Union

## Other Frameworks Evaluated

Current Apple-provided mechanisms are technically insufficient for the following reasons:
- MDM (Mobile Device Management): MDM queries are restricted to high-level inventory and
configuration state. They cannot detect active memory exploits or the
execution of malicious code within a legitimate process context.
- Sysdiagnose: This is a forensic, not a preventative, tool and does not contain the level of
granularity required (such as filesystem information). It requires complex manual
intervention to generate and to collect. It is therefore unscalable for 10,000 devices, and offers
only a retrospective view of system state, which most valuable logging is
truncated to a very short time window of a few days.
- Backups (iTunes/iCloud): Backups do not capture the live state of the system, omit temporary
files frequently used by attackers, and are susceptible to anti-forensic
techniques where an attacker deletes traces before a backup cycle occurs.
- App Sandbox: Standard API access is restricted by design, preventing a security application
from observing the behaviour of other processes, which is the fundamental
requirement for any EDR-like (Endpoint Detection and Response) capability.
No reasonable workaround exists within the current "black box" architecture that allows for the
continuous, remote detection required by modern enterprise security
standards.

## Confidential Treatment

Fully available to other developers

## Additional Information

To address potential privacy and stability concerns, the requested interoperability can be
governed by:
- Strict Entitlements: Access limited to apps signed by verified security vendors and deployed
via an MDM "Supervised" profile.
- Data Minimisation: The API would provide specific event notifications rather than broad raw
memory access.
- User Transparency: For BYOD scenarios, the activation of these telemetry features would be
contingent on clear user disclosure and MDM profile acceptance.
By providing an "ES-like" framework for iOS, Apple will enable a competitive market for mobile
security as envisioned by the DMA, while maintaining the robust platform
security architecture through managed, entitlement-driven API access.
Attachments

## Communications with Developer

May 13, 2026, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
