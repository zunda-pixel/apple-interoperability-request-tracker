# FB21689218 — Jann Schafranek

| Field | Value |
| --- | --- |
| Developer | Jann Schafranek |
| Request ID | FB21689218 |
| Date Received | January 20, 2026 |
| Current Status | Closed |

## Descriptive Title

Bring iOS Keyboard Extensions to Feature Parity with the Stock Keyboard

## Request Type

Interoperability Request

## Feature Name

Keyboard Extension

## Reason for Request

Hello,
My name is Jann Schafranek and I am one of the two developers of the app called “Mister
Keyboard”, which help tens of thousands of users to use their iPhone more effectively.
The apps offer Keyboard Extensions that can be customized in any way the user can imagine.
Now, the Keyboard Extension interface isn’t exactly rigid or on par with what the stock iOS
keyboard can do, which is why we are sending this interoperability request.

## Product Description

- Mister Keyboard
- Uniboard

## How the Product Will Use the Feature

This is the list of features we request:
- Easy retrieval of the entire document text, not just small chunks of text before and after the
cursor (hasText should also reflect all text)
- Get and set absolute cursor position functions
- Guarantee that all document editing functions return after the document has been modified
- Deletion:
- Delete multiple characters at once (delete(count: Int))
- Delete forward functions (deleteForward() and deleteForward(count: Int))
- Move cursor position by character (currently it moves it by utf16 scalars and reflects that
incorrectly in the UITextDocumentProxy)
- Text Selection:
- Set selected text
- Select complete document
- Microphone (for Dictation) and Camera (for OCR) Access after the user permits it
- Access to the system autocorrect engine
- Make the keyboard usable in all contexts, when the user asks for it, such as:
- Password Fields
- Apps that try to prevent third party keyboards
- Show suggestions from “Passwords”, OTPs from Notifications, E-Mails and SMS
- Launch into Passwords and Contacts Popovers
- Insert images, GIFs and other types of data
- Show controls outside of the main keyboard extension view
- Control padding
- Add custom view(s) and controls to bottom bar (iPhone X and newer)
- Show suggestions that will be applied inline with text, like the iOS stock keyboard autocorrect
does
- Don’t clip contents of the keyboard extension view (when long pressing keys like ‘a’ on the
system keyboard, that key can escape from the bounds of the keyboard)
- Make requestable alerts, like for Camera or Photos access, to:
- Add a keyboard to the user selected keyboards
- Allow full access for that keyboard
- Fix a bug where iOS (sometimes, race condition?) doesn’t show the keyboard extension in
settings after the app is downloaded
- Support Multiple Languages instead of just the primaryLanguage on the
UIInputViewController
- Getter for markedText
- clear() function to clear entire document
- Add explicit, settable height parameter to set the height of the keyboard at any time without
bugs or glitches
- Use the stock iOS trackpad-like gesture to move the cursor within text
Even though we believe all of the features mentioned above qualify for inclusion under the
DMA, we acknowledge that you might decide to include certain ones only in the Full Access
Mode, if explained in detail.

All of these features are or can deliver long-time requests of our users, and we hope you can
help to make your platform and our app even more helpful to all of them. ❤
Thanks in advance,
Jann Schafranek
FiveSheep OÜ

## Where the Product Is/Will Be Offered

Worldwide

## Other Frameworks Evaluated

We have used the technologies offered to Keyboard Extensions for many years. Sadly, they are
far from ideal and don't offer many of the features our users are requesting all the time. Most of
these requests are either quality issues caused by the APIs or features included in Apples
keyboards that are impossible to use as third party keyboards.

## Confidential Treatment

Fully available to other developers

## Additional Information

Attachments

## Communications with Developer

January 21, 2026, from Apple to Developer:
Thank you for your interoperability request.
It is currently in Phase I - Eligibility review. We will reach out via this forum if we need
clarification of your request.
If we do not reach out for clarification, we will endeavor to provide you with the outcome of the
initial assessment of our Phase I - Eligibility review within 20 working days of the date of your
request, which does not include any public holiday as defined by the European Commission.
February 16, 2026, from Apple to Developer:
Thank you again for your request.
We have reviewed your submission and determined that your request falls outside the scope of
Article 6(7) DMA because those which could constitute features are not available to or used by
Apple’s hardware and/or services. For this reason, we are not moving your request to the next
phase of our interoperability process.
As this determination is based on a non-technical consideration (i.e., whether a requested
feature is available to or used by an Apple service or hardware), it is not eligible for the dispute
resolution mechanism.
This concludes our review under Article 6(7) DMA.
Separately from the conclusion of this review, our Worldwide Developer Relations team will
reach out to you to discuss the potential to seek to address some aspects of your request
outside of the Article 6(7) DMA process.
If you have additional questions, you may reach out to us through Apple Developer Forums
(https://developer.apple.com/forums/) , Feedback Assistant (https://developer.apple.com/bug-
reporting/), or a code-level support request (https://developer.apple.com/contact/request/
code-level-support/).
