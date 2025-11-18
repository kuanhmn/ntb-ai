
from ntb_managers.ai_manager.manager import AIManager
from ntb_managers.user_manager.manager import UserManager

def main():
    um = UserManager()
    ai = AIManager()
    user = um.get_current_user()
    print("NTB-AI RUN V1 READY. User:", user)
    while True:
        try:
            t = input(">>> ").strip()
        except:
            break
        if not t: continue
        if t.lower() in ("exit","quit"): break
        print(ai.handle(t, user_id=user))

if __name__ == "__main__":
    main()
