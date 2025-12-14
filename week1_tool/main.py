"""
Script: Login File Scanner
Description:
    Reads a sever log file and filters for failure events.
    Target Keyword: "FAILED"
Author: HBW
"""

# Hardcoded for now, will switch CLI argument later
target_file = "server.log"

print(f"Start scanning {target_file}")

with open(target_file, "r") as f:
    for line in f:
        # We only care about the lines indicating a crash/failure
        if "FAILED" in line:
            print(f"Found error log {line.strip()}")
