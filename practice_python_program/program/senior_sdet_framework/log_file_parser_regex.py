"""
Automation Log Parser using Regex
Senior SDET Context: Parses execution logs to aggregate ERROR / FATAL occurrences and extract stack trace exception details.
"""

import re

def parse_automation_log(log_content: str) -> dict:
    error_pattern = re.compile(r"\[(ERROR|FATAL)\]\s+(?:(?P<exception>\w+Exception|\w+Error):\s+)?(?P<msg>.+)")
    errors = []
    log_lines = log_content.strip().split("\n")

    for line in log_lines:
        match = error_pattern.search(line)
        if match:
            errors.append({
                "level": match.group(1),
                "exception": match.group("exception") or "GeneralError",
                "message": match.group("msg")
            })

    return {
        "total_errors": len(errors),
        "errors": errors
    }

if __name__ == "__main__":
    sample_log = """
2026-09-25 10:00:01 [INFO] Starting test execution suite...
2026-09-25 10:00:05 [ERROR] ElementNotFoundException: Submit button not clickable
2026-09-25 10:00:08 [INFO] Retrying login request...
2026-09-25 10:00:12 [FATAL] ConnectionTimeoutError: Gateway 504 Timeout on /auth/token
"""
    parsed = parse_automation_log(sample_log)
    print("Parsed Log Summary:", parsed)
