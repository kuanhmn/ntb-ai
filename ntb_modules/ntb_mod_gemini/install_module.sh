#!/usr/bin/env bash
set -e

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$THIS_DIR/../.." && pwd)"
CONFIG_FILE="$BASE_DIR/ntb_config/system_api.json"

echo "== Install module: Gemini =="

mkdir -p "$(dirname "$CONFIG_FILE")"
if [ ! -f "$CONFIG_FILE" ]; then
  echo "{}" > "$CONFIG_FILE"
fi

echo "Nhập Gemini API key (Google AI):"
read -r GEM_KEY

echo "Nhập model Gemini (Enter = gemini-2.0-flash):"
read -r GEM_MODEL
if [ -z "$GEM_MODEL" ]; then
  GEM_MODEL="gemini-2.0-flash"
fi

echo "Nhập base_url Gemini (Enter = dùng URL mặc định của Google):"
read -r GEM_URL

python3 - <<PY
import json

config_path = r"$CONFIG_FILE"
try:
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception:
    data = {}

data["gemini"] = {
    "api_key": r"$GEM_KEY",
    "base_url": r"$GEM_URL",
    "model": r"$GEM_MODEL",
}

with open(config_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Đã cập nhật system_api.json cho Gemini.")
PY

echo "== Gemini module install done =="
