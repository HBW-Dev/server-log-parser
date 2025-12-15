"""
Script: Login File Scanner
Description:
    Reads a sever log file and filters for failure events.
    Target Keyword: "FAILED"
Author: HBW
"""

import sys


# Hardcoded for now, will switch CLI argument later
target_file = "server.log"

try:
    print(f"Start scanning {target_file}")

    with open(target_file, "r") as f:
        for line in f:
            # We only care about the lines indicating a crash/failure
            if "FAILED" in line:
                print(f"Found error log {line.strip()}")
except FileNotFoundError as e:
    print(f"[ERROR] File not found: {target_file}")
    sys.exit(1)

except Exception as e:
    print(f"[ERROR] Unexpected error: {e}")
    sys.exit(1)
