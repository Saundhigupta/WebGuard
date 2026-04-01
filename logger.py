import re
import json
from datetime import datetime

# Attack patterns to detect
SQL_PATTERNS = [
    r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
    r"((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))",
    r"union.*select",
    r"select.*from",
    r"or\s+\d+=\d+",
    r"insert|update|delete|drop|truncate",
]

XSS_PATTERNS = [
    r"<script.*?>",
    r"javascript:",
    r"onload\s*=",
    r"onerror\s*=",
    r"alert\s*\(",
    r"document\.cookie",
    r"<iframe.*?>",
]

def detect_attack(input_string):
    input_lower = input_string.lower()
    
    # Check XSS FIRST before SQL
    for pattern in XSS_PATTERNS:
        if re.search(pattern, input_lower, re.IGNORECASE):
            return "XSS"
    
    # Then check SQL injection
    for pattern in SQL_PATTERNS:
        if re.search(pattern, input_lower, re.IGNORECASE):
            return "SQL_INJECTION"
    
    return "NORMAL"

def log_request(input_string, source="manual"):
    attack_type = detect_attack(input_string)
    
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input": input_string,
        "attack_type": attack_type,
        "source": source
    }
    
    # Print to console
    status = "🚨 ATTACK" if attack_type != "NORMAL" else "✅ NORMAL"
    print(f"{status} | {attack_type} | {input_string[:50]}")
    
    # Save to log file
    with open("logs/requests.log", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    return log_entry

# Test it with your attack payloads
if __name__ == "__main__":
    test_inputs = [
        # Normal inputs
    "1",
    "2", 
    "admin",
    "hello world",
    "john",
    "search query",
    "username123",
    "test input",
    "normal text here",
    "page=1",

    # SQL Injection payloads
    "1' OR '1'='1",
    "' UNION SELECT user, password FROM users -- -",
    "1; DROP TABLE users--",
    "' OR 1=1--",
    "admin'--",
    "1' AND '1'='1",
    "' OR 'x'='x",
    "1' ORDER BY 1--",
    "' UNION SELECT null, null--",
    "1; SELECT * FROM users",

    # XSS payloads
    "<script>alert('XSS')</script>",
    "<script>alert(document.cookie)</script>",
    "<img src=x onerror=alert('XSS')>",
    "<iframe src='javascript:alert(1)'>",
    "javascript:alert(1)",
    "<body onload=alert('XSS')>",
    "<svg onload=alert(1)>",
    "<script>document.location='http://evil.com'</script>",
    "'\"><script>alert(1)</script>",
    "<scRipt>alert('XSS')</scRipt>",
    ]
    
    print("=== WebGuard Attack Logger ===\n")
    for inp in test_inputs:
        log_request(inp)
    
    print("\n✅ Logs saved to logs/requests.log")