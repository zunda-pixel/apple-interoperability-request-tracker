# FB22766980 — European Commission — DG DIGIT

| Field | Value |
| --- | --- |
| Developer | European Commission — DG DIGIT |
| Request ID | FB22766980 |
| Official page | [https://developer.apple.com/eu-interoperability-request/fb22766980/](https://developer.apple.com/eu-interoperability-request/fb22766980/) |
| Date Received | May 12, 2026 |
| Current Status | Closed |

## Descriptive Title

Configuration and Exception Management of iOS Lockdown Mode via Mobile Device Management (MDM) Frameworks

## Request Type

Interoperability Request

## Feature Requested

iOS Lockdown Mode Security Configuration

## Reason for Request

The current mobile threat landscape is characterized by a surge in sophisticated, non-interactive exploitation chains, specifically zero-click and one-click vulnerabilities as evidenced by the “Darksword” and “Coruna” exploit architectures. These vectors bypass sandbox boundaries and exploit memory corruption vulnerabilities in media processing and web-rendering components. While Apple introduced Lockdown Mode as a robust and effective defensive posture to mitigate these attack surfaces, the current implementation lacks the interoperability necessary for enterprise-scale defence.

Under the Digital Markets Act (DMA), Apple must offer interoperability with features used by or available to Apple’s services or hardware.

Currently, an asymmetry exists: the configuration of iOS Lockdown Mode and the exception management of it are available to Apple. Apple can submit OS updates or configuration updates to implement those changes. However, third parties, especially those managing mobile devices, do not have access to the same functionality.

The inability to manage the Lockdown Mode state through a Mobile Device Management (MDM) and to keep a centralized “allow-list” of mission-critical corporate applications within Lockdown Mode creates a binary choice between high security and operational functionality. Without the ability to exclude specific applications from the structures of Lockdown Mode via MDM, organizations may often be forced to disable the feature entirely to support functionality, thereby increasing the collective risk surface and creating a security regression that sophisticated actors exploit.

## Product Description

The requested interoperability will support a Mobile Threat Detection and Response (MTDR) Platform designed for large-scale enterprise and government deployments (10,000+ mobile devices). This platform centralizes system stability, diagnostics, and security telemetry to identify indicators of compromise (IoCs) across a fleet of Corporate Owned (Apple supervised devices) and BYOD (user-consented) devices. The platform serves as a centralised defensive hub for Security Operations Centres (SOCs):

* To identify hardware and software problems.
* To detect sophisticated indicators of compromise (IoC) — such as network activity, application crashes, unauthorized binary execution, privilege escalation, and lateral movement.
* To automate the triage of suspected compromises without requiring the physical recovery of the device or user intervention.
* To provide a capability for organizations with high-security requirements sovereign control over their data, precluding the transmission of sensitive diagnostic information to external third parties, including the OS vendor.

## How the Feature Will Be Used

The product would:

1. Issue an MDM command that remotely enables Lockdown Mode on a supervised or enrolled device without requiring manual user intervention.
2. Issue an MDM command to query the Lockdown Mode status of a device.
3. Use the API to support the deployment of a managed configuration profile that defines a list of “Excluded Applications” (using bundle IDs) and “Trusted Domains” that bypass specific Lockdown Mode restrictions (such as Just-In-Time compilation limits or specific web-kit restrictions).
4. Allow the user to keep the ability to add personal exclusions, while organizationally mandated exclusions stay immutable and centrally managed.

## Where Offered

European Union

## Evaluation of Alternatives

Current Apple-provided mechanisms are insufficient for the following technical reasons:

* **Manual User Configuration:** Relying on 10,000+ individual users to manually enable Lockdown Mode is operationally impossible and unverifiable. It introduces human error and high latency in responding to active, fleet-wide threats.
* **Standard MDM Restrictions:** Existing MDM profiles can restrict specific features (e.g., disabling the camera), but they cannot replicate the comprehensive, hardened kernel and web-kit configurations native to Lockdown Mode.
* **Lockdown Mode in its Current State:** The “all-or-nothing” nature of the current implementation lacks the granularity needed for enterprise interoperability. If one mission-critical application fails under Lockdown Mode, the entire defensive layer is often discarded because no mechanism exists to selectively exempt that single process via management tools.

## Confidentiality

Fully available to other developers

## Additional Information

This request prioritizes data minimization and user privacy. By utilizing the MDM framework, no sensitive personal telemetry is transmitted to third parties or Apple; only the Boolean state of the security feature and the bundle IDs of excluded applications could be managed. This architecture supports operational scalability by allowing security operations centres (SOCs) to automate the hardening of devices based on threat intelligence triggers (e.g., “Enforce Lockdown Mode for all users in a specific geographic region during an active exploit campaign”). Allowing a centrally managed exclusion list also ensures that an organisation can exclude corporate applications and third-party applications that are known to be incompatible with Lockdown Mode, without disabling the security feature completely.

The proposed architecture involves an enhancement to the Configuration Profile Reference, adding a LockdownModeSettings payload and a list containing LockdownModeExceptions. This ensures that the security enforcement remains on-device and hardware-attested, maintaining the integrity of the iOS security model while providing the necessary administrative hooks for professional-grade defensive operations at scale.

## Communications

##### May 13, 2026 — Apple to Developer

Thank you for your interoperability request. It is currently in Phase I — Eligibility review. We will reach out via this forum if we need clarification of your request. If we do not reach out for clarification, we will endeavor to provide you with the outcome of the initial assessment of our Phase I — Eligibility review within 20 working days of the date of your request, which does not include any public holiday as defined by the European Commission.

##### June 12, 2026 — Apple to Developer

Thank you for your request. We understand that you represent the Directorate-General for Digital Services of the European Commission (DG DIGIT) responsible for digital services that support other Commission departments and EU institutions. We also understand that your request seeks interoperability for purposes of providing a Mobile Threat Detection and Response (MTDR) Platform for a fleet of corporate-owned and BYOD devices of EU staff working at various Commission departments and EU institutions. Against this background, we understand that you are not a business user or a provider of services on Apple’s platforms and are therefore ineligible to seek interoperability with hardware and software features controlled by Apple’s operating systems under Article 6(7) of the DMA.

Notwithstanding the above, we have reviewed your submission and determined that your request would, in any case, fall outside the scope of Article 6(7) DMA. Specifically, your request seeks to require Apple to create a new functionality on iOS that is not accessed by any Apple services or hardware (i.e., the remote enabling of Lockdown Mode without user intervention and customization of personal application exclusions, trusted domains and organization-wide exclusions).

For these reasons, we are not moving your request to the next phase of our interoperability process.

As these determinations are based on non-technical considerations (i.e., whether the requestor is a business user or a provider of services on Apple’s platforms; whether what is requested is available to or used by Apple services or hardware), your request is not eligible for the dispute resolution mechanism.

In relation to the ability to query the Lockdown Mode status of a device, please note that an API supporting this functionality has shipped in developer seed for iOS 27 and iPadOS 27 earlier this week — see the developer documentation available at <https://developer.apple.com/documentation/os/os_lockdown_mode_enabled> and <https://developer.apple.com/documentation/devicemanagement/statussecuritylockdownmode>.

This concludes our Article 6(7) DMA review.

Without prejudice to the legal analysis under Article 6(7) DMA set out above, we understand that our International Business team has been in touch with your organisation to discuss how we can learn more about and further support where possible your organisation’s specific needs going forward.

If you have additional questions, you may also reach out to us through Apple Developer Forums, Feedback Assistant, or a code-level support request.
