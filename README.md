# File Integrity Checker

A Python-based **File Integrity Checker** built for **Cyber Security PBL** using **Tkinter** and **SHA-256 hashing**. This application helps detect file tampering by comparing stored and current hash values through a clean graphical interface.

---

## Features

* Store file hash securely
* Verify if a file is unchanged or modified
* Detect tampering using SHA-256
* Export verification report (CSV)
* Activity logs with timestamps
* Pastel-themed Tkinter GUI
* Simple and beginner-friendly project structure

---

## Tech Stack

* Python
* Tkinter
* hashlib
* JSON
* CSV
* OS Module

---

## Project Structure

```text
FileIntegrityChecker/
├── main.py
├── gui.py
├── hasher.py
├── storage.py
├── utils.py
├── monitor.py
├── hashes.json
├── activity.log
└── reports/
```

---

## How It Works

1. Select a file
2. Generate SHA-256 hash
3. Save hash in database
4. Recheck file later
5. Compare hashes
6. Show result:

   * SAFE
   * MODIFIED

---

## Installation

```bash
git clone <your-repo-link>
cd FileIntegrityChecker
pip install -r requirements.txt
```

> If no requirements file is used, Python standard libraries are enough.

---

## Run the Project

```bash
python main.py
```

---
