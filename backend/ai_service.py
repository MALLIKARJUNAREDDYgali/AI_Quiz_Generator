import requests
import json
from backend.config import EURI_API_KEY, EURI_API_URL, EURI_MODEL
from backend.utils import generate_prompt

def generate_quiz(topic: str, qtype: str):
    prompt = generate_prompt(topic, qtype)

    headers = {
        "Content-Type": "application/json",
        "Authorization": EURI_API_KEY
    }

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": EURI_MODEL,
        "max_tokens": 2000,
        "temperature": 0.7
    }

    response = requests.post(EURI_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            content = response.json()['choices'][0]['message']['content'].strip()
            questions = json.loads(content)
            return {"questions": questions}
        except Exception as e:
            raise Exception(f"[Parse Error] Could not decode EURI response: {e}\nRaw content:\n{content}")
    else:
        raise Exception(f"[EURI API Error] Status {response.status_code}: {response.text}")
