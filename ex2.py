import hashlib
import datetime


def sha256_of(filename):
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# Create evidence
with open("evidence.txt", "w") as f:
    f.write("Suspect chat log: meeting at 10pm, bring the drive.")

# Initial hash
seizure_hash = sha256_of("evidence.txt")

custody_log = []

custody_log.append(
    f"{datetime.datetime.now()} - SEIZED by Officer A - Hash = {seizure_hash}"
)

# Verify integrity during handoff
handoff_hash = sha256_of("evidence.txt")

if handoff_hash == seizure_hash:
    custody_log.append(
        f"{datetime.datetime.now()} - RECEIVED by Analyst B - Integrity VERIFIED"
    )
else:
    custody_log.append(
        f"{datetime.datetime.now()} - RECEIVED by Analyst B - Integrity FAILED"
    )

print("=== Chain of Custody Log ===\n")

for entry in custody_log:
    print(entry)
