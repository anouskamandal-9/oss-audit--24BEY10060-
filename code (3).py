cat << 'EOF' > task4.sh
#!/bin/bash
# Project Audit: Task 4 - Dependency Analysis
echo "--- Starting Python 3 Dependency Audit ---"

# 1. Identify the binary location
BINARY_PATH=$(which python3)
echo "Analyzing: $BINARY_PATH"
echo "------------------------------------------"

# 2. Run ldd to list shared library dependencies
echo "Dynamic Library Dependencies (Shared Objects):"
ldd $BINARY_PATH

echo "------------------------------------------"
echo "Audit Note: This list shows the modular nature"
echo "of FOSS. Python relies on these external .so"
echo "files for core system functionality."
echo "--- Dependency Audit Task 4 Complete ---"
EOF
bash task4.sh