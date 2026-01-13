from database.database import db
from datetime import datetime, timedelta
import pytz
from config import TIMEZONE, SESSION_TIMEOUT

TZ = pytz.timezone(TIMEZONE)

def test():
    user_id = 999999
    print(f"Testing for user {user_id}")
    
    # 1. Clear sessions
    with db.get_connection() as conn:
        conn.execute("DELETE FROM admin_sessions WHERE telegram_id = ?", (user_id,))
    
    # 2. Check active session (should be None)
    session = db.get_active_session(user_id)
    print(f"Initial session: {session}")
    
    # 3. Create session
    token = "test_token"
    expires = datetime.now(TZ) + timedelta(minutes=SESSION_TIMEOUT)
    print(f"Creating session expiring at {expires}")
    db.create_session(user_id, token, expires)
    
    # 4. Check active session
    session = db.get_active_session(user_id)
    print(f"Active session found: {session}")
    if session:
        print(f"Expires at (DB): {session['expires_at']}")
        print(f"Type of expires_at: {type(session['expires_at'])}")
    
    # 5. Check datetime comparison
    with db.get_connection() as conn:
        now_db = conn.execute("SELECT datetime('now', 'localtime')").fetchone()
        print(f"DB 'now' (localtime): {now_db}")
        
    print("Done")

if __name__ == "__main__":
    test()
