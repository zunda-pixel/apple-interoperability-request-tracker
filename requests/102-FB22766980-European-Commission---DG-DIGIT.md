# FB22766980 — European Commission - DG DIGIT

| Field | Value |
| --- | --- |
| Developer | European Commission - DG DIGIT |
| Request ID | FB22766980 |
| Date Received | May 12, 2026 |
| Current Status | Closed |

## Descriptive Title

Configuration and Exception Management of iOS Lockdown Mode via Mobile Device
Management (MDM) Frameworks.

## Request Type

Interoperability Request

## Feature Name

iOS Lockdown Mode Security Configuration.

## Reason for Request

The current mobile threat landscape is characterized by a surge in sophisticated, non-
interactive exploitation chains, specifically zero-click and one-click vulnerabilities as
evidenced by the "Darksword" and "Coruna" exploit architectures. These vectors bypass
sandbox boundaries and exploit memory corruption vulnerabilities in media
processing and web-rendering components. While Apple introduced Lockdown Mode as a
robust and effective defensive posture to mitigate these attack surfaces, the
current implementation lacks the interoperability necessary for enterprise-scale defence.
Under the Digital Markets Act (DMA), Apple must offer interoperability with features used by or
available to Apple’s services or hardware.
Currently, an asymmetry exists: The configuration of the iOS lockdown mode and the
exception management of it are available to Apple. Apple can submit OS update of
configuration updates to implement those changes. However, third parties, especially those
managing mobile devices do not have access to the same functionality.
The inability to manage the Lockdown Mode state through a Mobile Device Management
(MDM) and to keep a centralized "allow-list" of mission-critical corporate
applications within Lockdown Mode creates a binary choice between high security and
operational functionality. Without the ability to exclude specific applications from the
structures of Lockdown Mode via MDM, organizations may often be forced to disable the
feature entirely to support functionality, thereby increasing the collective risk
surface and creating a security regression that sophisticated actors exploit.

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

The product would:
1. Issue an MDM command that remotely enables Lockdown Mode on a supervised or enrolled
device without requiring manual user intervention.
2. Issue an MDM command to query the Lockdown Mode status of a device.
3. Use the API to support the deployment of a managed configuration profile that defines a first
list of "Excluded Applications" (using bundle IDs) and "Trusted Domains"
that bypass specific Lockdown Mode restrictions (such as Just-In-Time compilation limits or
specific web-kit restrictions).
4. Allow the user to keep the ability to add personal exclusions, but the organizationally
mandated exclusions would stay immutable and centrally managed.

## Where the Product Is/Will Be Offered

European Union

## Other Frameworks Evaluated

Current Apple-provided mechanisms are insufficient for the following technical reasons:
- Manual User Configuration: Relying on 10,000+ individual users to manually enable
Lockdown Mode is operationally impossible and unverifiable. It introduces human error
and high latency in responding to active, fleet-wide threats.
- Standard MDM Restrictions: Existing MDM profiles can restrict specific features (e.g.,
disabling the camera), but they cannot replicate the comprehensive, hardened
kernel and web-kit configurations native to Lockdown Mode.
- Lockdown Mode in its Current State: The "all-or-nothing" nature of the current
implementation lacks the granularity needed for enterprise interoperability. If one missioncritical
application fails under Lockdown Mode, the entire defensive layer is often discarded because
no mechanism exists to selectively exempt that single process via
management tools.

## Confidential Treatment

Fully available to other developers
