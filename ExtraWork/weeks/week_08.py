## Week 8
# Task - 5, Slow Requests and Retries
import time
import requests

try:
    requests.get("https://httpbin.org/delay/5", timeout=2)
except requests.exceptions.Timeout:
    print("The request timed out.")
def get_with_retry(url, attempts=3):
    for attempt in range(1, attempts + 1):
        try:
            response = requests.get(url, timeout=2)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print(f"Attempt {attempt}/{attempts} timed out.")
            if attempt < attempts:
                time.sleep(2 ** (attempt - 1))   # exponential backoff: 1s, 2s, ...
        except requests.exceptions.RequestException as error:
            print(f"Request failed: {error}")
            return None
    print(f"Giving up after {attempts} attempts.")
    return None

get_with_retry("https://httpbin.org/delay/5")

# Task - 7, Regex Basics
import re
text = "Contact Ann on 07123 456789 or ann@mail.com. Bob: bob@work.org, 07987 654321."
match = re.search(r"07\d{3} \d{6}", text)
print("First phone:", match.group() if match else "none found")
print("Emails:", re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+", text))
print("Masked:", re.sub(r"\d", "*", text))

# Task - 8, Pure Python EDA - Text Extractor
import re
import ipaddress

log_data = "User 192.168.1.1 logged in. Failed login from 10.0.0.55. Connection closed by 192.168.1.1."
def is_valid_ip(candidate):
    try:
        ipaddress.ip_address(candidate)   # rejects octets above 255
        return True
    except ValueError:
        return False
candidates = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", log_data)
unique_ips = {ip for ip in candidates if is_valid_ip(ip)}
print("Unique IPs:", sorted(unique_ips))
print("Count:", len(unique_ips))

# Task - 9, Refactor into a Class
import requests

class PostClient:
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
    def _get(self, endpoint, params=None):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            print(f"Timed out fetching {endpoint}.")
        except requests.exceptions.HTTPError as error:
            print(f"HTTP error {error.response.status_code} fetching {endpoint}.")
        except requests.exceptions.RequestException as error:
            print(f"Request failed: {error}")
        return None
    def get_post(self, post_id):
        return self._get(f"posts/{post_id}")
    def get_user_posts(self, user_id):
        return self._get("posts", params={"userId": user_id})

client = PostClient("https://jsonplaceholder.typicode.com")
post = client.get_post(1)
if post:
    print(f"Post 1: {post['title']}")
user_posts = client.get_user_posts(3)
if user_posts is not None:
    print(f"User 3 has {len(user_posts)} posts")
