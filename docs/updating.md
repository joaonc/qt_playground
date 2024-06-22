There's an update functionality where the app checks if an update is available and updates itself
if needed.

**Notes:**

* All code is included.  
  No external dependencies or extra scripts required.
* Transparent for users.
* Can update without running the UI (to run as script).
* Code can easily be modified to check for updates from S3, http, etc.  
  Currently checking locally.

## Update mechanism
This mechanism copies the new file to the current one by taking advantage of the fact that a file
currently in use cannot be overwritten but can be renamed.

The update flow is:

1. Rename file currently running to `*.bak_<timestamp>`
2. Copy new file to where the currently running file was prior to rename.

Next time the app runs, will be with the new version.

Sample output from the update flow:
```
INFO:root:Updating to version 1.0.1.
DEBUG:root:Updating file C:\Users\joaon\code\qt_playground\dist\qt_playground.exe
DEBUG:root:Backing up file to C:\Users\joaon\code\qt_playground\dist\qt_playground.bak_1719096410
DEBUG:root:Copying new version from C:\Users\joaon\code\qt_playground\dist_test\qt_playground_101.exe
INFO:root:Update was successful and the new version will be used the next time the app runs.
```

## Updating
For the normal update flow, simply run the UI app and it will update before exiting.  
`--update-manifest` and `--update-file` need to be set.

To update via CLI without showing the UI:  
Note: Example below is for PowerShell. Use `\` as line separator for Mac and Linux CLI.
```
.\qt_playground.exe `
--check-update-only `
--log-level debug `
--update-manifest "../dist_test/app.yaml" `
--update-file "../dist_test/qt_playground_101.exe"
```

## Checking app version
There are two ways to check the app version:

* CLI: `qt_playground --version`
* UI:  _Help > About_

## Debugging options
The options below are available as environment variables for debugging purposes.

Set them to `True` or `1` in the environment to enable them.

* `IGNORE_BUNDLED_APP`  
  Do not check if the code is running as a bundled app (an executable) or a python script.  
  Ie, code that is supposed to execute only as a bundled app will run as script also.
* `QT_PLAYGROUND_IGNORE_UPDATE`  
  Do not perform an app update (and backup), even if one is available.  
  See also the ``check-update`` and ``check-update-only`` CLI options.
