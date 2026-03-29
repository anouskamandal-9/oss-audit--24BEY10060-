#!/bin/bash
# Project Audit: Task 1 - Installation Verification
echo "--- Starting Python 3 Audit ---"

# Checking if the python3 command exists
if command -v python3 &>/dev/null; then
    echo "Status: Python 3 is already installed on this system."
    echo "Current Version:"
    python3 --version
else
    echo "Status: Python 3 was NOT found."
    echo "Suggestion: Use 'sudo apt install python3' to install it."
fi

echo "--- Audit Task 1 Complete ---"