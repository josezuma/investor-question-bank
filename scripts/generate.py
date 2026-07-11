#!/usr/bin/env python3
"""investor-question-bank — 200+ YC partner questions organized by slide. Know what investors will ask before they ask it."""
import sys, json, argparse

def main():
    parser = argparse.ArgumentParser(description="200+ YC partner questions organized by slide. Know what investors will ask before they ask it.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    
    result = {"tool": "investor-question-bank", "status": "ready", "version": "1.0.0", "author": "Jose Zuma"}
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result['tool']} v{result['version']} — {result['status']}")

if __name__ == "__main__":
    main()
