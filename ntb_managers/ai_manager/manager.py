
import requests, json
from ntb_managers.api_manager.manager import ApiManager
from ntb_managers.memory_manager.manager import MemoryManager

class Engine:
    def __init__(self):
        self.api = ApiManager()
    def call(self, eng, prompt, uid):
        cfg = self.api.get(eng, uid)
        if not cfg: return f"[{eng}] no config"
        url=cfg['base_url'].rstrip('/')+'/chat/completions'
        body={"model":cfg["model"],"messages":[{"role":"user","content":prompt}]}
        headers={"Authorization":"Bearer "+cfg["api_key"],"Content-Type":"application/json"}
        try:
            r=requests.post(url,headers=headers,json=body,timeout=60)
            j=r.json()
            return j["choices"][0]["message"]["content"]
        except Exception as e:
            return f"[{eng} error] {e}"

class AIManager:
    def __init__(self):
        self.mem=MemoryManager()
        self.eng=Engine()
    def handle(self,text,user_id="default"):
        low=text.lower()
        # direct engine
        for key,ename in [("gpt","gpt"),("ds","deepseek"),("mini","gemini")]:
            if low.startswith(key+" "):
                payload=text[len(key):].strip()
                out=self.eng.call(ename,payload,user_id)
                self.mem.log(user_id,ename,payload)
                return f"[{ename.upper()}] {out}"
        # normal pipeline
        g=self.eng.call("gpt",text,user_id)
        d=self.eng.call("deepseek",text,user_id)
        combo=json.dumps({"u":text,"gpt":g,"ds":d})
        final=self.eng.call("gemini",combo,user_id)
        self.mem.log(user_id,"pipeline",final)
        return final
