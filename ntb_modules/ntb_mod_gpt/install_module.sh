#!/usr/bin/env bash
set -e

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$THIS_DIR/../.." && pwd)"
CONFIG_FILE="$BASE_DIR/ntb_config/system_api.json"

echo "== Install module: GPT =="

mkdir -p "$(dirname "$CONFIG_FILE")"
if [ ! -f "$CONFIG_FILE" ]; then
  echo "{}" > "$CONFIG_FILE"
fi

echo "Nhập GPT API key (OpenAI):"
read -r GPT_KEY

echo "Nhập base_url GPT (Enter = https://api.openai.com/v1/chat/completions):"
read -r GPT_URL
if [ -z "$GPT_URL" ]; then
  GPT_URL="https://api.openai.com/v1/chat/completions"
fi

echo "Nhập model GPT (Enter = gpt-4.1-mini):"
read -r GPT_MODEL
if [ -z "$GPT_MODEL" ]; then
  GPT_MODEL="gpt-4.1-mini"
fi

python3 - <<PY
import json

config_path = r"$CONFIG_FILE"
try:
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception:
    data = {}

data["gpt"] = {
    "api_key": r"$GPT_KEY",
    "base_url": r"$GPT_URL",
    "model": r"$GPT_MODEL",
}

with open(config_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Đã cập nhật system_api.json cho GPT.")
PY

echo "== GPT module install done =="
