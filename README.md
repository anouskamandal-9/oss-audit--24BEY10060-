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

### 1. Preparation
Ensure all shell scripts have execution permissions:
```bash
chmod +x *.sh
