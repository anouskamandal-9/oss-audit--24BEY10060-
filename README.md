# oss-audit--24BEY10060-
# 🛡️ Open Source Software Audit: Python 3 Environment
**Course Component:** FOSS Project (40 Marks)

## 👤 Student Information
* **Student Name:** [ANOUSKA MANDAL]
* **Roll Number:** [24BEY10060]
* **Chosen Software:** Python 3 (Open Source Interpreter)

---

## 📝 Project Description
This repository contains a professional audit suite designed to analyze the installation, security, and dependencies of Python 3 on a Linux system. The audit uses a **dual-scripting approach**, providing both Bash and Python versions for every task to ensure cross-verification of system data.

---

## 📂 Description of Audit Scripts

### Task 1: Version & Environment Verification
* **Scripts:**  `code.py`
* **Description:** Verifies the installed version of Python 3 and ensures the environment is ready for auditing.

### Task 2: Directory & Filesystem Mapping
* **Scripts:**  `code(1).py`
* **Description:** Locates the binary executable path and maps the library directories to ensure standard FOSS filesystem hierarchy.

### Task 3: Security & Ownership Audit
* **Scripts:** `code(2).py`
* **Description:** Audits file permissions and ownership (UID) to ensure the Python binary is secured against unauthorized modification.

### Task 4: Dynamic Dependency Analysis
* **Scripts:**  `code(3).py`
* **Description:** Uses the `ldd` utility to map all shared libraries (.so files) that Python 3 depends on to function.

### Task 5: Automated Reporting & Logging
* **Scripts:**  `code(4).py`
* **Description:** Aggregates all audit findings into a final text report (`Python_Audit_Summary.txt`) for administrative review.

---

## 🚀 Step-by-Step Instructions (Linux)

Follow these steps in your Linux terminal (e.g., TutorialsPoint) to execute the audit:

Phase 1: Preparing the Environment
Before running the Python scripts, you need to make sure the terminal is ready.

 1) Open your Terminal: (e.g., TutorialsPoint or your college Linux VM).

2) Upload your files: Use the terminal's "Upload" button to bring in code.py, code(1).py, code(2).py, code(3).py, and code(4).py.

3) Check the files: Type ls and press Enter. You should see all your "code" files listed in the terminal.
   
Phase 2: Running the Python Audit (Step-by-Step)
Because your filenames have parentheses, you must wrap them in double quotes so Linux reads them correctly.
Step 1: Version Verification
python3 'code.py'
Step 2: Filesystem Mapping
python3 "code(1).py"
Step 3: Security Audit
python3 "code(2).py"
Step 4: Dependency Analysis
python3 "code(3).py"
Step 5: Final Report Generation
python3 "code(4).py"
Phase 3: Verifying the Final Output

Required Dependencies
To ensure the audit suite functions correctly, the following must be present:

Python 3.x: The primary software being audited.

Linux Utilities: ldd, grep, and which.

Standard Libraries: The scripts utilize built-in Python modules (os, sys, subprocess, platform)—no external pip installations are required.
