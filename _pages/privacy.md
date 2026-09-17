---
layout: page
title: Privacy Policy
subtitle: Meow Family (referred to as “we,” “us,” or “our”) highly values and respects your privacy. This Privacy Policy explains how we collect, use, store, and protect your personal information, specifically regarding how our applications handle your data when you use the Google Drive Backup and Restore features. By using our application, you agree to the terms described in this Privacy Policy.
permalink: /privacy/
---

_Last Updated: September 17, 2026_

## 1. Our Core Principle: Data Minimization
We strictly adhere to the principle of data minimization. Our application only requests access to your Google Account when you explicitly trigger the "Backup" or "Restore" functions, and we only access data that is absolutely necessary to perform these actions.
## 2. Google User Data Access and Usage (drive.file Scope)
When you log in to your Google Account and enable the cloud backup feature, our application requests the Google Drive API (.../auth/drive.file) permission. Our usage of this permission is strictly limited to the following actions:

* Creating and Writing Backups: When you click "Backup Data," the application packages your local app data (such as cat profiles, app settings, and history logs) into a backup file. It then uploads this file directly to your personal Google Drive.
* Reading and Restoring Data: When you click "Restore Data," the application looks for and reads only the specific backup files previously created by Meow Family on your Google Drive to download and synchronize them back to your local device.
* Deleting Backups: If you choose to manage or clear your cloud backup history within the app, the application will delete the older backup files created by our app from your Google Drive based on your explicit command.

Important Note on Scope: The drive.file scope does NOT give us access to your entire Google Drive. We cannot see, modify, or delete any other files, folders, or photos stored in your Google Drive that were not created by the Meow Family application.
## 3. Data Storage, Transmission, and Security

* Local Storage: All your app data remains securely stored within your device's local encrypted sandbox.
* Encryption in Transit: All data transfers between the application and Google Drive are performed using secure HTTPS (SSL/TLS) channels to prevent data interception or tampering.
* Direct Cloud Ownership: Your backup files are stored exclusively in your own Google Drive account. We do not operate any external servers to host, cache, intercept, or store your Google account credentials, authentication tokens, or backup files.

## 4. Google API Limited Use Policy Compliance
We strictly comply with the Google API Services User Data Policy, including the Limited Use requirements:

* No Sharing or Selling: We never sell, rent, share, or disclose your Google user data to any third parties (such as advertisers, data brokers, or other independent developers).
* No Advertising: Your Google Drive data will never be used for serving advertisements, user profiling, or any commercial purposes outside of the core backup and restore function.
* No Human Review: No human beings, including members of our development team, can view, read, or access the data stored in your Google Drive.

## 5. Your Rights: Revoking Access and Deleting Data
You retain full control over your data at all times:

* Disconnecting in App: You can log out of your Google Account anytime within the application settings.
* Revoking Google Access: You can permanently revoke the application's access to your Google Drive at any time via the [Google Third-party apps with account access page](https://myaccount.google.com/permissions).
* Deleting Cloud Data: You can use the app's backup management tool to delete any uploaded backup files from your Google Drive prior to disconnecting your account.

## 6. Changes to This Privacy Policy
We may update this Privacy Policy from time to time to reflect changes in our application features or applicable legal requirements. We will notify you of any significant changes by updating the "Last Updated" date at the top of this policy or via an in-app notice.
## 7. Contact Us
If you have any questions, suggestions, or concerns regarding this Privacy Policy or our Google data practices, please contact us at:

* Developer/Team Name: Meow Apps Studio
* Official Website: https://spacemanmeow.com/
* Contact Email: meow@spacemanmeow.com
