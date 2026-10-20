## Week 10
# Task - 1 & 2, Create the Database and users Table
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "DATA"
DATA_DIR.mkdir(exist_ok=True)
DB_FILE = DATA_DIR / "lab_week10.db"
conn = sqlite3.connect(DB_FILE)
conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        role TEXT DEFAULT 'user'
    )
""")
conn.commit()

# Task - 3, INSERT (add_user)
import bcrypt

def add_user(conn, username, password_hash, role="user"):
    conn.execute(
        "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
        (username, password_hash, role),
    )
    conn.commit()
def hash_pw(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
add_user(conn, "alice", hash_pw("AlicePass1!"), "admin")
add_user(conn, "bob", hash_pw("BobPass2!"))
add_user(conn, "charlie", hash_pw("CharliePass3!"))

# Task - 4, SELECT
def get_all_users(conn):
    return conn.execute("SELECT * FROM users").fetchall()
def get_user(conn, username):
    return conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
print(len(get_all_users(conn)), "users")
print(get_user(conn, "alice")[:2])
print(get_user(conn, "nobody"))   # None

# Task - 5, UPDATE and DELETE
def update_role(conn, username, new_role):
    cursor = conn.execute("UPDATE users SET role = ? WHERE username = ?", (new_role, username))
    conn.commit()
    return cursor.rowcount
def delete_user(conn, username):
    cursor = conn.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    return cursor.rowcount
update_role(conn, "bob", "moderator")
delete_user(conn, "charlie")
for user_id, username, _, role in get_all_users(conn):
    print(user_id, username, role)

# Task - 6, SQL Injection Demonstration
def get_user_unsafe(conn, username):
    query = f"SELECT * FROM users WHERE username = '{username}'"   # NEVER do this
    print("Query run:", query)
    return conn.execute(query).fetchall()
print(len(get_user_unsafe(conn, "alice")))           # 1 row
print(len(get_user_unsafe(conn, "' OR '1'='1")))     # every row: the condition is always true
print(get_user(conn, "' OR '1'='1"))                 # None: safe version treats it as plain text
# With an f-string the input becomes part of the SQL itself, so an attacker can change the query.
# Parameterised queries (?) send the input separately as data, so it can never be run as SQL.

# Task - 7, Load CSV Data with Pandas
import pandas as pd

pd.DataFrame({
    "incident_id": [1, 2, 3],
    "severity": ["High", "Critical", "Low"],
    "category": ["Phishing", "Ransomware", "Policy"],
    "status": ["Open", "Investigating", "Closed"],
    "description": ["Credential phishing email reported by finance",
                    "Ransomware detected on file server",
                    "Unapproved software installed on laptop"],
}).to_csv(DATA_DIR / "sample_incidents.csv", index=False)
incidents = pd.read_csv(DATA_DIR / "sample_incidents.csv")
incidents.to_sql("cyber_incidents", conn, if_exists="replace", index=False)
print(pd.read_sql("SELECT * FROM cyber_incidents", conn))

# Task - 8, Reflection Questions
# 1. fetchone() returns the next single row (or None); fetchall() returns every remaining row as a list.
# 2. Every row in the table would be deleted, because there is no WHERE clause to limit it.
# 3. If the table already exists, to_sql raises an error by default. if_exists tells pandas whether to
#    'replace' it, 'append' to it, or 'fail'.
conn.close()

