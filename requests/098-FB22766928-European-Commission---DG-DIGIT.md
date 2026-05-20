# FB22766928 — European Commission - DG DIGIT

| Field | Value |
| --- | --- |
| Developer | European Commission - DG DIGIT |
| Request ID | FB22766928 |
| Date Received | May 12, 2026 |
| Current Status | Phase I |

## Descriptive Title

Access to mobile analytics data for enterprise diagnostics and threat detection

## Request Type

Interoperability Request

## Feature Name

MDM-Integrated configurable Analytics Data endpoint and documentation of the analytics
schemas.

## Reason for Request

The current mobile threat landscape is characterised by a proliferation of sophisticated, non-
persistent, and zero/one-click exploit chains, such as those identified in the "Darksword" and
"Coruna" frameworks. These attacks operate with high levels of stealth, frequently cleaning up
filesystem artifacts to evade detection. To protect high-value enterprise and sovereign
environments, defenders require near real-time visibility into system logging, process crashes,
and kernel panics—indicators that often precede or accompany successful exploitation.
Under the Digital Markets Act (DMA), Apple must offer interoperability with features used by or
available to Apple's services or hardware.
Apple currently uses internal diagnostic streams and the "Share iPhone/iPad Analytics"
pipeline to monitor device health, stability, and security and shares information about
application crashes with developers of those apps.
Apple also uses on-device diagnostic data, such as system diagnosis, in Feedback Assistant.
The feedback assistant app is a service that Apple offers for Beta versions, to help users and
developers improve Apple's software.
Current mechanisms provided by Apple only allow disabling this analytics data to be sent to
Apple and do not allow the configuration of a custom diagnostic server.
Interoperability is therefore necessary to allow third-party security platforms to offer a level of
protection equivalent to Apple's internal capabilities, ensuring a competitive and secure
ecosystem for enterprise users.

## Product Description

The requested interoperability will support a Mobile Threat Detection and Response (MTDR)
Platform designed for large-scale enterprise and government deployments (10,000+ mobile
devices). This platform centralizes system stability, diagnostics, and security telemetry to
identify indicators of compromise (IoCs) across a fleet of Corporate Owned (Apple supervised
devices) and BYOD (user-consented) devices. The platform serves as centralised defensive
hub for Security Operations Centres (SOCs)
(1) to identify hardware and software problems, (2) to detect sophisticated indicators of
compromise (IoC) —such as network activity, application crashes, unauthorized binary
execution, privilege escalation, and lateral movement, (3) to automate the triage of suspected
compromises without requiring the physical recovery of the device or user intervention and (4)
to provide a capability for organizations with high-security requirements sovereign control over
their data, precluding the transmission of sensitive diagnostic information to external third
parties, including the OS vendor.

## How the Product Will Use the Feature

The product would require the following:
1. Telemetry Redirection: The product would configure, via an MDM payload (e.g., a
com.apple.managedconfiguration profile), a custom URL for the existing "Share iPhone/iPad
Analytics" feature. This would redirect standard diagnostic payloads—specifically crash logs,
kernel panics, and system usage metrics—directly to the organization's secure, self-hosted
ingestion server instead of non-sovereign Apple systems.
2. API Documentation: The product would implement the Apple-provided technical
documentation regarding the schema, transport protocols (e.g., Protobuf/JSON structures),
and authentication headers used by the OS to transmit these reports.
The goal is to allow for near real-time monitoring of system crashes. In an enterprise context, a
sudden cluster of unique application crashes or kernel panics can be automatically flagged as
a potential exploit attempt, triggering immediate containment protocols via MDM.
The high-level architecture is the following: A managed iOS device generating a standard
CrashReporter or analyticsd payload. Instead of reaching the Apple servers, the device
connects to https://soc.enterprise.tld/telemetry. The enterprise server then parses the incoming
data against the requested documentation to store the telemetry and diagnostic information
locally so that it can identify anomalies and provide the adequate user support.

## Where the Product Is/Will Be Offered

European Union

## Other Frameworks Evaluated

The following existing mechanisms have been evaluated and considered technically
insufficient:
- Disabling sharing Analytics Data: Current exposed MDM features only allow opting out of
telemetry being sent to the OS vendor (Apple), not the collection hereof by the owner or
organisation managing the device.
- MDM InstalledApplicationList & DeviceInformation: These provide high-level inventory data
but offer zero visibility into runtime process behaviour, memory corruption events, or kernel-
level instabilities.
- Sysdiagnose: While comprehensive, a sysdiagnose file can exceed 500MB, requires physical
device access or manual user intervention to trigger and offload, and is not designed for
automated, remote, or frequent collection. It is a tool to assist developers, not a defensive
operation telemetry stream.
- iTunes/iCloud Backups: Backups do not capture transient execution states or logs stored in
protected system partitions. Furthermore, attackers with high-level privileges can remove files
containing diagnostic data and even modify the logs within the filesystem before a backup is
initiated.
- Physical Extraction: This requires the device to be physically tethered to a workstation, which
is non-scalable for a distributed workforce of 10,000 users, provides no live detection
capability, and may impact the device integrity.
No reasonable workaround currently exists that provides the necessary frequency and
granularity of telemetry without the requested interoperability.

## Confidential Treatment

Fully available to other developers

## Additional Information

Security and Privacy Safeguards:
- Data Minimization: This request does not seek access to user content (emails, photos,
messages). It seeks access only to the system-level diagnostic telemetry that Apple already
collects.
- Enhanced Privacy: By redirecting analytics to a private corporate server, the organization
ensures that sensitive metadata about their internal device usage is not transmitted to the OS
vendor (Apple), thereby also reducing the external attack surface through a 3rd party and
enhancing data sovereignty.
- Consent Framework: For supervised devices the consent is implicit by definition. For BYOD
devices, this telemetry redirection would only be active upon explicit user enrolment in the
MDM platform, ensuring transparency and compliance with GDPR/national privacy laws.
Attachments

## Communications with Developer

May 13, 2026, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
