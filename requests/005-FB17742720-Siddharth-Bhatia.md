# FB17742720 — Siddharth Bhatia

| Field | Value |
| --- | --- |
| Developer | Siddharth Bhatia |
| Request ID | FB17742720 |
| Date Received | May 30, 2025 |
| Current Status | Closed |

## Descriptive Title

Allow Transferring DeviceActivity and Screen Time data outside of the app extension, allowing
it to be sent to servers and the main app

## Request Type

Interoperability Request

## Feature Name

DeviceActivity

## Reason for Request

Currently, DeviceActivity only allows accessing device activity within a
"DeviceActivityReportExtension", which is not allowed to make network requests or persist
data to a container shared with the main app. This is in contrast to the native Screen Time
feature, which is able to send device activity data over a network and persist it to disk. Apple
uses this feature in the Settings app to sync screen time data between devices. The restrictions
on device activity data specifically for third-party apps, but not first-party ones, therefore
restricts access to "the same hardware and software features accessed or controlled via the
operating system" (Article 6(7) of the DMA)
This DeviceActivity sandboxing restriction also prevents “effective portability of data…
generated through the activity of the end user” (Article 6(9) of the DMA), as device activity data
is generated through the activity of the end user yet is not currently “portable” off-device via
third-party services.
We request the following interoperability solution:
- With the appropriate privacy authorizations, as described in the last bullet, third-party apps
can access device activity data continuously, freely, and without restriction or obfuscation,
including in the background, and can use this data in the main app, save it to disk, and send it
over the network. This includes the exact time and duration of each app use, the number of
pickups, counts of app notifications, and any other information shared to the first-party screen
time service
- Allow apps to access the actual names and bundle identifiers of apps and activity categories
being used, which the operating system has access to, instead of obfuscated tokens. This is
useful for advanced and custom categorization and filtering, as well as more extensive
reporting.
- For user protection, create a new privacy prompt that an app can activate, in the same format
as the one used ask for location services or contacts access, asking the user whether to allow
the app to transmit screen time data off device. If they decline, the app will be bound by the
‘sandboxing’ that exists currently.

## Product Description

ScreenResearch, an app that allows users to voluntarily share their screen time data with
university researchers who can use it to investigate how people use their devices.

## How the Product Will Use the Feature

The product will use this new or updated DeviceActivity framework. It will collect device and
app usage data at regular intervals and transmit them to a server where the data is aggregated
and can be used in research projects. The data on the server will include the name of each app
used and the exact dates/times they were used and for how long, along with other information.
Data will only be shared with the user’s consent, and personally identifying information will be
removed from the data before it’s shared with researchers.

## Where the Product Is/Will Be Offered

Worldwide
European Union

## Other Frameworks Evaluated

The DeviceActivity framework is closest to what we want to do, but it does not allow the ability
to share raw data externally or with the main app. We have also evaluated the FamilyControls
framework, but that appears to serve a different purpose from what we want.

## Confidential Treatment

Fully available to other developers

## Communications with Developer

June 3, 2025, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
In addition, based on your confidentiality designation, your request will appear in full (including
the name of your developer organization) on the following tracker: https://developer.apple.com/
file/?file=interoperability-request-tracker. If you wish not to include the name of your developer
organization on the tracker, please let us know and we will remove it in future versions of the
tracker.
June 30, 2025, from Apple to Developer:
Thank you for your request.
We have reviewed your submission and determined that your request falls outside the scope of
Article 6(7) DMA because there is no feature available to Apple services or hardware that
provides the functionality you seek. For this reason, we are not moving your request to the next
phase of our interoperability process.
In addition, your reference to Article 6(9) DMA is not relevant to this 6(7) interoperability
request. Apple notes, however, that it makes available all applicable 6(9) data through the Data
& Privacy page at privacy.apple.com.
This concludes our review under Article 6(7) DMA. If you have additional questions, you may
reach out to us through Apple Developer Forums, Feedback Assistant, or a code-level support
request.
Starting in July 2025, you will have the opportunity to appeal this decision, should you wish,
through a dispute resolution mechanism that Apple will set up as part of the European
Commission’s specification decision on process. You will be notified once the dispute
resolution mechanism is available, after which you will have 15 working days by which to
submit your appeal.
The Apple Developer Relations Team
