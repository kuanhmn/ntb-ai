
import json
from pathlib import Path

class ApiManager:
    def __init__(self):
        self.path = Path("/opt/ntb-ai/ntb_config/system_api.json")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("{}")
    def get(self, engine, user=None):
        try:
            return json.loads(self.path.read_text()).get(engine,{})
        except:
            return {}
