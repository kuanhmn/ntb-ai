
import json
from pathlib import Path

class UserManager:
    def __init__(self):
        self.cfg = Path("/opt/ntb-ai/ntb_config/core_users.json")
        self.root = Path("/opt/ntb-ai/user_data")
        self.root.mkdir(parents=True, exist_ok=True)
        if not self.cfg.exists():
            self.cfg.write_text(json.dumps({"current_user": "default"}))
    def get_current_user(self):
        try:
            return json.loads(self.cfg.read_text()).get("current_user","default")
        except:
            return "default"
