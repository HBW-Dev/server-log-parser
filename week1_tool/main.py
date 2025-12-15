#! /usr/bin/env python3
"""
Script: Log File Scanner
Description:
    Reads a server log file and filters for failure events.
    Accepts filename via command line arguments.
Author: HBW
"""

import sys
import argparse
import re


def main():
    """
    Docstring for main
    """

    # Set up Argument Parser
    parser = argparse.ArgumentParser(description="Scan log file for failure events.")

    parser.add_argument("filename", help="The path to the file you want to scan")

    args = parser.parse_args()

    target_file = args.filename

    print(f"Start scanning {target_file}")

    try:
        with open(target_file, "r") as f:
            for line in f:
                if "FAILED" in line:
                    ip_pattern = r"\d+\.\d+\.\d+\.\d+"

                    match = re.search(ip_pattern, line)

                    if match:
                        ip = match.group()
                        print(f"Alert! Attack from IP: {ip}")
                    else:
                        print("Alert! FAILED found but no IP detected.")
                        # print(f"Found {line}")
    except FileNotFoundError:
        print(f"Not found: {target_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
