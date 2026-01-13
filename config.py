"""
Tizim konfiguratsiyasi
"""
import os
from dotenv import load_dotenv
import hashlib

# .env faylini yuklash
load_dotenv()

# Bot token
BOT_TOKEN = os.getenv("BOT_TOKEN", "8542494278:AAELsdOoG0msjStbJnc9gD-8qn2naxX34rw")

# Chat va Topic IDlar
CONTROL_GROUP_ID = -1003488691700  # Asosiy guruh ID
CONTROL_TOPIC_ID = 2  # Controll topik (2 - umumiy chat ID bo'lishi mumkin)

# Hisobot turlariga mos topic IDlar
TOPICS = {
    "vitrina": 205,
    "obuv": 207,
    "sklad": 206,
    "hr": 1,  # Shtraf va jarimalar
    "oshxona": 8434  # Yangi oshxona topic ID
}

# Statistika guruhi
STATS_GROUP_LINK = "https://t.me/+O51GOfNi3I1iMDYy"
# Link orqali group ID olish kerak, hozircha placeholder
STATS_GROUP_ID = None  # Botni guruhga qo'shgandan keyin yangilanadi

# Deadline vaqtlari (soat:daqiqa, 24-soatlik format)
OTDEL_MORNING_DEADLINE = "12:00"  # Birinchi 4 ta otdel hisoboti
OTDEL_EVENING_DEADLINE = "19:00"  # Oxirgi 4 ta otdel hisoboti
SKLAD_DEADLINE = "19:00"
OBUV_DEADLINE = "19:00"
OSHXONA_DEADLINE = "19:00"  # Yangi!
SHTRAF_DEADLINE = "16:00"   # hr (shtraf va jarimalar) uchun

# Otdel hisobotlari limiti
OTDEL_MORNING_LIMIT = 4  # 12:00 gacha
OTDEL_EVENING_LIMIT = 4  # 19:00 gacha
TOTAL_OTDEL_REPORTS = 8  # Jami

# Kunlik eslatma vaqtlari (yangi tizim)
REMINDERS = [
    {
        "time": "09:30",
        "title": "OTDEL (bo'limlar)",
        "tasks": [
            "▪️ Vitrina",
            "▪️ Stellaj",
            "▪️ Kiyinish xonalari"
        ],
        "note": "📸 Video → UPR / HR",
        "deadline": "10:00"
    },
    {
        "time": "11:00",
        "title": "OBUV BO'LIMI",
        "tasks": [
            "▪️ Juftlar to'g'ri joylashtirilgan",
            "▪️ Pol va vitrinalar toza"
        ],
        "note": "📸 Video → UPR / HR",
        "deadline": "11:30"
    },
    {
        "time": "15:00",
        "title": "SKLAD",
        "tasks": [
            "▪️ Kirim-chiqim",
            "▪️ Tovar joylashuvi",
            "▪️ Sklad tartibi"
        ],
        "note": "📸 Video → UPR / HR / Baza",
        "deadline": "15:30"
    },
    {
        "time": "16:00",
        "title": "USTKI KIYIMLAR",
        "tasks": [
            "▪️ Rang, model, dazmol holati"
        ],
        "note": "📸 Video → Telegram (rahbariyat)",
        "deadline": "16:30"
    },
    {
        "time": "16:30",
        "title": "OBUV (QAYTA TEKSHIRUV)",
        "tasks": [
            "▪️ Sotuvdan keyingi holat"
        ],
        "note": "📸 Video → UPR",
        "deadline": "17:00"
    },
    {
        "time": "17:00",
        "title": "UMUMIY HOLAT",
        "tasks": [
            "▪️ Shim bo'limi",
            "▪️ Kiyinish xonalari",
            "▪️ Oshxona",
            "▪️ Pol va umumiy ko'rinish"
        ],
        "note": "📸 Video → UPR",
        "deadline": "17:30"
    },
    {
        "time": "23:00",
        "title": "KUN YAKUNI (YAKUNIY VIDEO)",
        "tasks": [
            "▪️ Barcha bo'limlar",
            "▪️ Do'kon yopilishi"
        ],
        "note": "📸 Video → UPR / HR",
        "deadline": "00:00"
    }
]

# Kunlik hisobot vaqti
DAILY_REPORT_TIME = "00:00"

# Haftalik hisobot vaqti (yakshanba)
WEEKLY_REPORT_DAY = 6  # 0=Monday, 6=Sunday
WEEKLY_REPORT_TIME = "22:00"

# Vaqt zonasi
TIMEZONE = "Asia/Tashkent"

# Admin ma'lumotlari
ADMIN_LOGIN = "negmuradov"
ADMIN_PASSWORD_HASH = hashlib.sha256(
    os.getenv("ADMIN_PASSWORD", "Spectr@2008").encode()
).hexdigest()

# Session timeout (daqiqalarda)
SESSION_TIMEOUT = 60

# Ma'lumotlar bazasi
DB_NAME = "vip_control.db"
DB_CONFIG = {
    "database": DB_NAME
}

# Foto dublikat tekshirish (kunlarda)
DUPLICATE_CHECK_DAYS = 3

# Hash o'xshashlik chegarasi (0-64, pastroq = qattiqroq)
HASH_SIMILARITY_THRESHOLD = 5

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Xabarlar (o'zbekcha)
MESSAGES = {
    "report_received": "✅ Hisobot qabul qilindi!\n📊 Tur: {report_type}\n🏢 Filial: {branch}\n⏰ Vaqt: {time}",
    "report_late": "⚠️ Kechikish!\n\nSiz hisobotni belgilangan vaqtdan keyin yubordingiz.\n\n"
                  "Tasdiqlanishi uchun @vipbrandislom bilan bog'laning va sababini tushuntiring.",
    "duplicate_photo": "❌ Bu foto allaqachon yuborilgan!\n\nOxirgi 3 kun ichida bir xil foto topildi.\n"
                      "Iltimos, yangi foto yuboring.",
    "invalid_format": "❌ Noto'g'ri format!\n\nTo'g'ri format:\n[Filial nomi] [tur]\n\n"
                     "Masalan: Yangi Hayot otdel\n\nTurlar: otdel, obuv, sklad, oshxona, hr",
    "otdel_limit_morning": "❌ Siz allaqachon {count} ta otdel hisoboti yubordingiz (12:00 gacha limit: 4 ta).\n\n"
                          "Qolgan otdel hisobotlarini 12:00 dan keyin yuboring.",
    "otdel_limit_evening": "❌ Siz bugun maksimal {count} ta otdel hisoboti yubordingiz (limit: 8 ta).",
    "admin_welcome": "👋 Xush kelibsiz, administrator!\n\nIltimos, login va parolni kiriting.",
    "admin_login_prompt": "📝 Loginni kiriting:",
    "admin_password_prompt": "🔐 Parolni kiriting:",
    "admin_auth_failed": "❌ Noto'g'ri login yoki parol!",
    "admin_auth_success": "✅ Muvaffaqiyatli kirildi!\n\nBoshqaruv paneli:",
    "unauthorized": "🚫 Sizda bu buyruqdan foydalanish huquqi yo'q!",
}

# Hisobot turlari va ularning deadline
REPORT_TYPES = {
    "otdel": {
        "deadline_morning": OTDEL_MORNING_DEADLINE,
        "deadline_evening": OTDEL_EVENING_DEADLINE, 
        "name": "Otdel (bo'lim)",
        "daily_limit": TOTAL_OTDEL_REPORTS
    },
    "obuv": {
        "deadline": OBUV_DEADLINE, 
        "name": "Obuv"
    },
    "sklad": {
        "deadline": SKLAD_DEADLINE, 
        "name": "Sklad"
    },
    "oshxona": {
        "deadline": OSHXONA_DEADLINE, 
        "name": "Oshxona"
    },
    "hr": {
        "deadline": SHTRAF_DEADLINE, 
        "name": "Shtraf va jarimalar"
    }
}

