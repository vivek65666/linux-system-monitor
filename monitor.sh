#!/bin/bash

echo "==============================="
echo " Linux System Health Report"
echo "==============================="

echo ""
echo "Hostname:"
hostname

echo ""
echo "Current Date:"
date

echo ""
echo "System Uptime:"
uptime

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "CPU Information:"
lscpu | grep "Model name"

echo ""
echo "Top 5 CPU Processes:"
ps aux --sort=-%cpu | head -6

echo ""
echo "Top 5 Memory Processes:"
ps aux --sort=-%mem | head -6

echo ""
echo "Logged In Users:"
who

echo ""
echo "IP Address:"
hostname -I

echo ""
echo "Done."
