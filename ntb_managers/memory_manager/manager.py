
import sqlite3
from pathlib import Path
from datetime import datetime

class MemoryManager:
    def __init__(self):
        self.base = Path("/opt/ntb-ai/user_data")
    def _conn(self, uid):
        d = self.base/uid/"memory"
        d.mkdir(parents=True, exist_ok=True)
        db = d/"mem.db"
        conn = sqlite3.connect(db)
        conn.execute("CREATE TABLE IF NOT EXISTS facts(k TEXT PRIMARY KEY, v TEXT)")
        conn.execute("CREATE TABLE IF NOT EXISTS log(ts TEXT, role TEXT, text TEXT)")
        return conn
    def get(self, uid, k):
        c=self._conn(uid).cursor()
        r=c.execute("SELECT v FROM facts WHERE k=?",(k,)).fetchone()
        return r[0] if r else None
    def set(self, uid, k, v):
        conn=self._conn(uid)
        conn.execute("DELETE FROM facts WHERE k=?",(k,))
        conn.execute("INSERT INTO facts VALUES(?,?)",(k,v))
        conn.commit()
    def log(self, uid, role, text):
        conn=self._conn(uid)
        conn.execute("INSERT INTO log VALUES(?,?,?)",(datetime.utcnow().isoformat(),role,text))
        conn.commit()
