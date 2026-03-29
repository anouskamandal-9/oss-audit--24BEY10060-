cat << 'EOF' > task3.sh
#!/bin/bash
# Project Audit: Task 3 - Security & Permissions
echo "--- Starting Python 3 Security Audit ---"

# 1. Identify the binary location
BINARY_PATH=$(which python3)

echo "Target File: $BINARY_PATH"
echo "----------------------------------------"

# 2. Check detailed permissions and ownership
echo "File Permissions (ls -l):"
ls -l $BINARY_PATH

echo "----------------------------------------"
echo "Note for Report: In a secure Linux environment,"
echo "the Python binary should be owned by 'root'."
echo "--- Security Audit Complete ---"
EOF
bash task3.sh