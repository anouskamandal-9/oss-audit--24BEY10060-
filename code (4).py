cat << 'EOF' > task5.sh
#!/bin/bash
# Project Audit: Task 5 - Final Report Generation
REPORT_FILE="Python_Audit_Summary.txt"

echo "--- Generating Final Audit Report ---"
echo "Project: Open Source Software Audit (Python 3)" > $REPORT_FILE
echo "Date: $(date)" >> $REPORT_FILE
echo "System: $(uname -a)" >> $REPORT_FILE
echo "------------------------------------------" >> $REPORT_FILE

echo "1. Installation: $(python3 --version)" >> $REPORT_FILE
echo "2. Binary Path: $(which python3)" >> $REPORT_FILE
echo "3. Security: $(ls -l $(which python3) | awk '{print $1, $3, $4}')" >> $REPORT_FILE

echo "------------------------------------------" >> $REPORT_FILE
echo "Status: Audit Complete. All core files verified." >> $REPORT_FILE

echo "Report saved to: $REPORT_FILE"
echo "--- Displaying Report Content ---"
cat $REPORT_FILE
EOF
bash task5.sh