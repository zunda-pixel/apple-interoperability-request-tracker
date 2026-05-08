# FB20588738 — Crystal Alarm

| Field | Value |
| --- | --- |
| Developer | Crystal Alarm |
| Request ID | FB20588738 |
| Date Received | October 9, 2025 |
| Current Status | Closed |

## Descriptive Title

Access to nearby WiFi BSSIDs

## Request Type

Interoperability Request

## Feature Name

Access to nearby WiFi BSSIDs

## Reason for Request

On behalf of Crystal  Alarm  AB, a provider of certified personal safety solutions used by
enterprises and public authorities across Europe, we hereby submit a new interoperability
request under Article 6(7) of the Digital Markets Act (DMA).
Requested Interoperability Scope
We request access to APIs enabling:
• Retrieval of Wi‑Fi BSSID and SSID metadata for nearby access points; and
• Programmatic use of this data for deterministic indoor positioning within our safety‑critical
application.
Justification
Our service must provide precise indoor location when a user triggers an emergency alarm. In
many workplaces—such as hospitals, factories, or underground facilities—GPS and
mobile‑network positioning are insufficient.
While Apple’s Core Location framework can use Wi‑Fi signals to improve accuracy, it relies on
crowd‑sourced Wi‑Fi databases that are outside our control. For a certified personal safety
system, the Wi‑Fi data source must be strictly controlled and verifiable, and it must be possible
to limit which BSSIDs are used.
Core Location does not offer this capability. As a result:
• We cannot guarantee accuracy or traceability of location data, which is mandatory in safety
applications;
• Apple, by contrast, could implement such a controlled solution internally, since both the
OS‑level and app‑level components are under Apple’s control.
This situation gives Apple’s own services an unfair functional advantage—they can combine
knowledge of private OS‑side data with application logic, whereas third‑party developers
cannot reproduce equivalent functionality.
DMA Relevance
Under Article 6(7) of the DMA, gatekeepers must provide third‑party developers effective
interoperability with the same operating‑system, hardware, and software features used by their
own services.
Our request therefore seeks equal technical capability to implement Wi‑Fi‑assisted indoor
positioning—on the same basis that Apple’s own Core Location and “Find My” frameworks
already benefit from internal access to Wi‑Fi metadata.
Without such access:
• Apple retains exclusive control over how Wi‑Fi‑based positioning functions, including
undisclosed algorithmic and data‑handling details;
• Third‑party developers cannot achieve equivalent reliability, even when user safety depends
on it; and
• Users are deprived of competitive, high‑accuracy safety solutions.
We emphasize that our requested use is solely for user‑initiated emergency alarms and will fully
comply with data‑protection and transparency obligations.
Next Steps
We respectfully request that this submission be reviewed as a new interoperability request
under Article 6(7) of the DMA and that Apple provide a path to access the necessary Wi‑Fi
metadata APIs, subject to appropriate privacy safeguards.
Please confirm the process and any additional information required.

## Product Description

Crystal Alarm

## How the Product Will Use the Feature

Indoor location

## Where the Product Is/Will Be Offered

European Union

## Other Frameworks Evaluated

Yes
We have asked for access to Hotspot Helper API which might be a part solution, but this was
denied since indoor location is not the intent of the API

## Confidential Treatment

Fully available to other developers

## Additional Information

Attachments

## Communications with Developer

October 10, 2025, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
October 27, 2025, from Apple to Developer:
Thank you for your interoperability request.
We have reviewed your submission and determined that you submitted a request seeking the
same functionality involving Wi-Fi BSSID and SSID metadata for nearby access points, on at
least one prior occasion, and the most recent request was denied on 3 June 2025. We followed
up to inform you that the dispute resolution mechanism was available on 22 July 2025, but as
no appeal was submitted, that decision is now final. For this reason, we are closing this
request.
