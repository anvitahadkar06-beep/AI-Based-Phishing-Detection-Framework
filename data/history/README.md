# History Module
This directory manages the storage and retrieval of application scan logs. It acts as the local data store for tracking operations.

## Directory Structure
```"scan_history"``` — The primary data file containing chronological scan records.

## Data Format
The scan_history file records data using the following format:

Type: [e.g., JSON / Plain Text / CSV]

Structure: [e.g., Timestamp | Operation | Status | Target]

## How It Works
Writing: The application appends a new entry to scan_history every time a scan completes.

Reading: The history UI or CLI parses this file to display past activities to the user.

## Maintenance Note
Do not delete the scan_history file manually, as it may cause read errors in the main application.

Large history files can be archived or cleared using the built-in application settings.
