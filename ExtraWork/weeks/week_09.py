## Week 9
# Task - 1, Write generate_hash()
import bcrypt

def generate_hash(psw):
    hashed = bcrypt.hashpw(psw.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")
hash1 = generate_hash("Magic123")
hash2 = generate_hash("Magic123")
print(hash1)
print(hash2)
print("Hashes identical:", hash1 == hash2)   # False, different salts

# Task - 2, Write is_valid_hash()
def is_valid_hash(psw, hash_str):
    return bcrypt.checkpw(psw.encode("utf-8"), hash_str.encode("utf-8"))
print(is_valid_hash("Magic123", hash1))   # True
print(is_valid_hash("Wrong123", hash1))   # False

# Task - 3, Register and Login with File I/O
import os
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "DATA"
DATA_DIR.mkdir(exist_ok=True)


def register_user(name, password, filepath=DATA_DIR / "lab_users.txt"):
    if not name or "," in name:
        print("Invalid username.")
        return False
    if os.path.exists(filepath):
        with open(filepath) as f:
            if any(line.split(",", 1)[0] == name for line in f):
                print(f"{name} already exists.")
                return False
    with open(filepath, "a") as f:
        f.write(f"{name},{generate_hash(password)}\n")
    return True
def login_user(name, password, filepath=DATA_DIR / "lab_users.txt"):
    if not os.path.exists(filepath):
        return False
    with open(filepath) as f:
        for line in f:
            stored_name, _, stored_hash = line.strip().partition(",")
            if stored_name == name and is_valid_hash(password, stored_hash):
                return True
    return False
register_user("alice", "AlicePass1!")
register_user("bob", "BobPass2!")
print(login_user("alice", "AlicePass1!"))   # True
print(login_user("alice", "wrong"))         # False
print(login_user("mallory", "anything"))    # False

# Task - 4, Reflection Questions
# 1. bcrypt generates a new random salt on every call and stores it inside the hash,
#    so the same password produces a different string each time.
# 2. No. Each user gets a different salt, so identical passwords give different hashes.
#    An attacker cannot tell who shares a password and precomputed rainbow tables are useless.
# 3. == on two hashes always fails for a correct password because the salt differs each time.
#    checkpw() reads the salt from the stored hash, re-hashes the attempt and compares properly.

