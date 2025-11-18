import requests

AGENT_ID = "gemini"


def run(text, meta):
    api = meta.get("api_config", {})
    key = api.get("api_key")
    model = api.get("model", "gemini-2.5-flash")
    base_url = api.get("base_url", "")

    if not key:
        return "[Gemini] Missing API key"

    if base_url:
        url = base_url
    else:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"

    payload = {
        "contents": [
            {"parts": [{"text": text}]}
        ]
    }

    try:
        r = requests.post(url, json=payload, timeout=30)
        r.raise_for_status()
        j = r.json()
        return j["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"[Gemini error] {e}"
