## Week 12
# Task - 3, Multi-Turn Console Chat
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # reads OPENAI_API_KEY from .env (never commit this file)
client = OpenAI()
def run_console_chat(system_prompt, client):
    messages = [{"role": "system", "content": system_prompt}]
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            break
        if not user_input:
            continue
        messages.append({"role": "user", "content": user_input})
        try:
            response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        except Exception as error:
            print(f"API error: {error}")
            messages.pop() # keep the history consistent after a failed call
            continue
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(f"AI: {reply}")
run_console_chat("You are a helpful assistant.", client)

# Task - 4, Prompt Engineering
SYSTEM_PROMPTS = {
    "Cybersecurity": (
        "You are a senior incident response analyst. "
        "Structure every answer as: 1) Summary, 2) Likely cause, 3) Immediate actions, 4) Prevention. "
        "Prioritise containment, then evidence preservation, then recovery. "
        "Give a clear risk rating, reference MITRE ATT&CK where relevant and never invent indicators."
    ),
    "Data Science": (
        "You are an experienced data scientist and ML engineer. "
        "Structure every answer as: 1) Approach, 2) Method, 3) Steps or code, 4) Caveats. "
        "Prioritise data quality, correct statistics and reproducibility, and state your assumptions."
    ),
    "IT Operations": (
        "You are an IT operations lead. "
        "Structure every answer as: 1) Impact, 2) Diagnosis, 3) Fix, 4) Follow-up. "
        "Prioritise service availability, low-risk changes and a documented rollback plan."
    ),
}
for domain, prompt in SYSTEM_PROMPTS.items():
    print(f"{domain}: {len(prompt)} characters")

# Task - 5, Combining Database Data with AI
incident = {
    "id": "INC-2026-014",
    "severity": "High",
    "category": "Phishing",
    "status": "Open",
    "description": "Finance staff received emails impersonating the CEO asking for urgent payments. "
                   "Two users clicked the link and entered credentials.",
}
def build_incident_prompt(incident):
    return (
        "Analyse the following security incident.\n\n"
        f"ID: {incident['id']}\n"
        f"Severity: {incident['severity']}\n"
        f"Category: {incident['category']}\n"
        f"Status: {incident['status']}\n"
        f"Description: {incident['description']}\n\n"
        "Provide:\n"
        "1. Root cause analysis\n"
        "2. Immediate containment actions (bullet points)\n"
        "3. Long-term prevention measures\n"
        "4. Risk assessment (Low / Medium / High / Critical)"
    )
prompt = build_incident_prompt(incident)
print(prompt)
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": SYSTEM_PROMPTS["Cybersecurity"]},
                  {"role": "user", "content": prompt}],
    )
    print(response.choices[0].message.content)
except Exception as error:
    print(f"API error: {error}")

# Task - 6, Streamlit Chat Page
# The page is in ../streamlit_app/pages/4_AI_Assistant.py.
