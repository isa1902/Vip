import telegram
from telegram import Update
import sys

print(f"Python version: {sys.version}")
print(f"PTB version: {telegram.__version__}")

try:
    u = Update(update_id=1, message=None)
    print(f"Update object created: {u}")
    print(f"Has message attribute? {hasattr(u, 'message')}")
except Exception as e:
    print(f"Error creating Update: {e}")

try:
    from telegram.constants import ParseMode
    print(f"ParseMode: {ParseMode.HTML}")
except ImportError as e:
    print(f"ParseMode Error: {e}")
