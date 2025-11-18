import requests

AGENT_ID = "deepseek"


def run(text, meta):
    api = meta.get("api_config", {})
    key = api.get("api_key")
    url = api.get("base_url", "https://api.deepseek.com/v1/chat/completions")
    model = api.get("model", "deepseek-chat")

    if not key:
        return "[DeepSeek] Missing key"

    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": text}
        ],
    }

    try:
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        r.raise_for_status()
        j = r.json()
        return j["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[DeepSeek error] {e}"
