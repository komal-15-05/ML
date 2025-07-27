import requests
import os

GROQ_API_KEY = "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"

def ask_groq(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "llama-3.1-8b-instant"
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]
