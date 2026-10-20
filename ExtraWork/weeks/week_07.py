## Week 7
# Task - 9, Word Frequency Counter
from pathlib import Path

def word_frequency(text):
    text = text.lower()
    for mark in ".,!?":
        text = text.replace(mark, "")
    frequency = {}
    for word in text.split():
        frequency[word] = frequency.get(word, 0) + 1
    top5 = sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:5]
    print("Top 5 words:")
    for word, count in top5:
        print(f"  {word}: {count}")
    return frequency

text = """Data science is the study of data. Data scientists use data to find patterns.
Machine learning is a part of data science. Scientists study data every day!
The science of data is growing, and data is everywhere."""
word_frequency(text)

try:
    text_path = Path(__file__).resolve().parents[1] / "DATA" / "Les_Brown.txt"
    with text_path.open(encoding="utf-8") as f:
        word_frequency(f.read())
except FileNotFoundError:
    print("DATA/Les_Brown.txt not found; add the text file to the DATA folder to run this example.")

# Task - 11, Caesar Cipher Encoder and Decoder
def shift_text(text, key):
    result = []
    for ch in text:
        if ch.isalpha() and ch.isascii():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + key) % 26 + base))   # % 26 wraps z -> a
        else:
            result.append(ch)
    return "".join(result)

def encode(text, key):
    return shift_text(text, key)

def decode(text, key):
    return shift_text(text, -key)

original = "Hello World! 123"
key = 5
encoded = encode(original, key)
decoded = decode(encoded, key)
print(f"Original: {original}")
print(f"Encoded:  {encoded}")
print(f"Decoded:  {decoded}")
print("Round trip OK:", decoded == original)

# Task - 12, Text Data Cleaning Pipeline
def clean_dataset(records):
    valid_records = []
    invalid_records = []
    for raw in records:
        fields = [f.strip() for f in raw.split("|")]
        if len(fields) != 4 or not all(fields):
            invalid_records.append((raw.strip(), "Empty or missing field"))
            continue
        name, age, email, country = fields
        name = " ".join(name.split()).title()
        if not (age.isdigit() and 18 <= int(age) <= 120):
            invalid_records.append((name, f"Invalid age: {age}"))
            continue
        at = email.find("@")
        if at == -1 or email.find(".", at) == -1:
            invalid_records.append((name, f"Invalid email: {email}"))
            continue
        valid_records.append({"name": name, "age": int(age), "email": email, "country": country.upper()})
    return valid_records, invalid_records
raw_data = [
    "  john SMITH  | 25 | john.smith@email.com | united kingdom ",
    "  MARY  johnson | abc | mary@email | france",
    " | 30 | test@test.com | germany",
    "  bob wilson  | 17 | bob@mail.com | spain  ",
    "  alice Brown  | 28 | alice.b@data.org | italy  ",
    "charlie DAVIS | 35 | | usa",
]
valid_records, invalid_records = clean_dataset(raw_data)
print("VALID")
for record in valid_records:
    print(" ", record)
print("INVALID")
for record, reason in invalid_records:
    print(f"  {record!r} -> {reason}")

# Task - 14, Build a Simple Search Engine
def search(documents, query):
    words = query.lower().split()
    results = []
    for doc in documents:
        tokens = [t.strip(".,!?") for t in doc.lower().split()]
        found = {w: tokens.count(w) for w in words if tokens.count(w) > 0}
        score = sum(found.values())
        if score:
            results.append((score, doc, found))
    results.sort(key=lambda r: r[0], reverse=True)
    print(f"\nResults for '{query}':")
    if not results:
        print("  No matches.")
    for score, doc, found in results:
        matched = ", ".join(f"{w} x{c}" for w, c in found.items())
        print(f"  [score {score}] {doc}")
        print(f"      matched: {matched}")
    return results
documents = [
    "Python is a great programming language for data science and machine learning",
    "Data analysis with Python involves cleaning and processing large datasets",
    "Machine learning models can predict outcomes from historical data",
    "Web development with JavaScript and HTML is different from data work",
    "Python data science libraries include NumPy and Pandas for data processing",
]
search(documents, "data science")
search(documents, "Python machine learning")

