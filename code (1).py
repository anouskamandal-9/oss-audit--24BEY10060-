cat << 'EOF' > task2.sh
#!/bin/bash
# Project Audit: Task 2 - Directory Mapping
echo "--- Locating Python 3 Footprint ---"

# Finding the exact path of the binary
echo "1. Binary Executable Path:"
which python3

# Finding where the libraries are stored
echo "2. Library Directories (Top 3):"
find /usr/lib -name "python3*" -type d 2>/dev/null | head -n 3

echo "--- Audit Task 2 Complete ---"
EOF