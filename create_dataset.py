import json
import csv

# Read the log file
log_entries = []
with open("logs/requests.log", "r") as f:
    for line in f:
        entry = json.loads(line.strip())
        log_entries.append(entry)

# Write to CSV
with open("data/dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # Header
    writer.writerow(["input", "attack_type"])
    # Data
    for entry in log_entries:
        writer.writerow([entry["input"], entry["attack_type"]])

print(f"✅ Dataset created with {len(log_entries)} samples!")
print("Saved to data/dataset.csv")

# Show breakdown
normal = sum(1 for e in log_entries if e["attack_type"] == "NORMAL")
sqli = sum(1 for e in log_entries if e["attack_type"] == "SQL_INJECTION")
xss = sum(1 for e in log_entries if e["attack_type"] == "XSS")

print(f"\nBreakdown:")
print(f"  NORMAL:        {normal} samples")
print(f"  SQL_INJECTION: {sqli} samples")
print(f"  XSS:           {xss} samples")