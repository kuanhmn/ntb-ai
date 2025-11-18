#!/usr/bin/env bash
set -e

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$THIS_DIR/../.." && pwd)"
CONFIG_FILE="$BASE_DIR/ntb_config/system_api.json"

echo "== Install module: DeepSeek =="

mkdir -p "$(dirname "$CONFIG_FILE")"
if [ ! -f "$CONFIG_FILE" ]; then
  echo "{}" > "$CONFIG_FILE"
fi

echo "Nhập DeepSeek API key:"
read -r DS_KEY

echo "Nhập base_url DeepSeek (Enter = https://api.deepseek.com/v1/chat/completions):"
read -r DS_URL
if [ -z "$DS_URL" ]; then
  DS_URL="https://api.deepseek.com/v1/chat/completions"
fi

echo "Nhập model DeepSeek (Enter = deepseek-chat):"
read -r DS_MODEL
if [ -z "$DS_MODEL" ]; then
  DS_MODEL="deepseek-chat"
fi

python3 - <<PY
import json

config_path = r"$CONFIG_FILE"
try:
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception:
    data = {}

data["deepseek"] = {
    "api_key": r"$DS_KEY",
    "base_url": r"$DS_URL",
    "model": r"$DS_MODEL",
}

with open(config_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Đã cập nhật system_api.json cho DeepSeek.")
PY

echo "== DeepSeek module install done =="
