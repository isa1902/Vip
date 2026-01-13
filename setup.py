"""
O'rnatish skripti
Ma'lumotlar bazasi va muhitni sozlash (SQLite versiyasi)
"""
import os
import sys
import subprocess
import sqlite3
from getpass import getpass


def print_header(text):
    """Header chop etish"""
    print("\n" + "=" * 50)
    print(text)
    print("=" * 50 + "\n")


def check_python_version():
    """Python versiyasini tekshirish"""
    if sys.version_info < (3, 9):
        print("❌ Python 3.9 yoki yuqori versiya kerak!")
        print(f"Sizning versiyangiz: {sys.version}")
        sys.exit(1)
    print(f"✅ Python versiyasi: {sys.version.split()[0]}")


def create_env_file():
    """`.env` fayl yaratish"""
    print_header("ENVIRONMENT O'ZGARUVCHILAR")
    
    if os.path.exists('.env'):
        overwrite = input(".env fayli mavjud. Qayta yozishni xohlaysizmi? (y/N): ")
        if overwrite.lower() != 'y':
            print("⏭ O'tkazib yuborildi")
            return
    
    # Ma'lumotlarni so'rash
    admin_password = getpass("Admin Password [Spectr@2008]: ") or "Spectr@2008"
    bot_token = input("Bot Token: ")
    
    # .env yaratish
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(f"# Admin\n")
        f.write(f"ADMIN_PASSWORD={admin_password}\n\n")
        f.write(f"# Bot\n")
        f.write(f"BOT_TOKEN={bot_token}\n")
    
    print("✅ .env fayli yaratildi!")


def install_requirements():
    """Kutubxonalarni o'rnatish"""
    print_header("PYTHON KUTUBXONALARINI O'RNATISH")
    
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True
        )
        print("✅ Kutubxonalar o'rnatildi!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Xatolik: {e}")
        sys.exit(1)


def setup_database():
    """Ma'lumotlar bazasini yaratish"""
    print_header("MA'LUMOTLAR BAZASI SOZLASH")
    
    db_name = "vip_control.db"
    
    try:
        # Schema ni o'qish
        with open('database/schema.sql', 'r', encoding='utf-8') as f:
            schema = f.read()
            
        print(f"📦 {db_name} yaratilmoqda...")
        
        # Bazani yaratish
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Scriptni bajarish
        cursor.executescript(schema)
        
        conn.commit()
        conn.close()
        
        print("✅ Ma'lumotlar bazasi muvaffaqiyatli yaratildi!")
        
    except Exception as e:
        print(f"❌ Xatolik: {e}")


def main():
    """Asosiy funksiya"""
    print_header("VIP CONTROL BOT - O'RNATISH (SQLite)")
    
    # Python versiyasini tekshirish
    check_python_version()
    
    # Kutubxonalarni o'rnatish
    install_requirements()
    
    # .env yaratish
    create_env_file()
    
    # Ma'lumotlar bazasini sozlash
    setup_database()
    
    print_header("O'RNATISH TUGADI!")
    print("Botni ishga tushirish uchun:")
    print("  python main.py")
    print("\nyoki:")
    print("  start_bot.bat  (Windows)")


if __name__ == '__main__':
    main()
