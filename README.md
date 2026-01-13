# VIP CONTROL BOT

Telegram bot menejerlarning kunlik hisobotlarini avtomatik nazorat qilish, eslatmalar yuborish va statistika to'plash uchun.

## 📋 Xususiyatlar

- ✅ **Hisobotlarni qabul qilish**: Foto/video + caption orqali
- 🕐 **Deadline tekshiruvi**: Vitrina (19:00), Shtraf (16:00)
- 🔍 **Dublikat aniqlash**: Bir xil fotolarni rad etish (3 kun)
- ⏰ **Avtomatik eslatmalar**: 18:00 va 15:00 da
- 📊 **Kunlik hisobot**: Har kecha 00:00 da
- 📈 **Haftalik hisobot**: Yakshanba 22:00 da
- 👨‍💼 **Admin panel**: Menejerlar va filiallarni boshqarish
- ✋ **Qo'lda tasdiqlash**: Kechikkan hisobotlarni qo'lda kiritish

## 🛠 O'rnatish

### 1. Talablar

- Python 3.9+
- PostgreSQL 12+
- Telegram Bot Token

### 2. Loyihani yuklab olish

```bash
cd C:\Users\Administrator\Desktop\vip_controlll
```

### 3. Virtual muhit yaratish

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

### 5. Ma'lumotlar bazasi sozlash

PostgreSQL da yangi database yaratish:

```sql
CREATE DATABASE vip_control_bot;
CREATE USER bot_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE vip_control_bot TO bot_user;
```

Sxemani import qilish:

```bash
psql -U bot_user -d vip_control_bot -f database/schema.sql
```

### 6. Environment o'zgaruvchilari

`.env.example` dan nusxa oling va sozlang:

```bash
copy .env.example .env
```

`.env` faylida to'ldiring:

```env
DB_HOST=localhost
DB_NAME=vip_control_bot
DB_USER=bot_user
DB_PASSWORD=your_secure_password

ADMIN_PASSWORD=Spectr@2008
BOT_TOKEN=8542494278:AAELsdOoG0msjStbJnc9gD-8qn2naxX34rw
```

### 7. Botni guruhga qo'shish

1. Botni guruhga a'zo qilish
2. Botga **admin** huquqlarini berish
3. **Xabarlarni o'chirish** va **Topiklarda post qilish** ruxsatlarini berish

## 🚀 Ishga tushirish

```bash
python main.py
```

Yoki Windows PowerShell da:

```powershell
python main.py
```

## 📱 Foydalanish

### Admin panel

1. Botga shaxsiy chatda `/start` yuboring
2. Login: `negmuradov`
3. Parol: `Spectr@2008`
4. Menyudan kerakli bo'limni tanlang

### Hisobot yuborish (menejerlar uchun)

Guruhda foto/video yuborish + caption:

```
[Filial nomi] [tur]
```

Masalan:
- `Yangi Hayot otdel` - Vitrina hisoboti
- `UPR Ibrahim obuv` - Obuv hisoboti
- `Mahkamov sklad` - Sklad hisoboti
- `Filial1 hr` - Shtraf va jarimalar

### Hisobot turlari

- `otdel` - Vitrina (deadline: 19:00)
- `obuv` - Obuv (deadline: 19:00)
- `sklad` - Sklad (deadline: 19:00)
- `hr` - Shtraf va jarimalar (deadline: 16:00)

## 🏗 Loyiha tuzilmasi

```
vip_controlll/
├── bot/
│   ├── handlers/
│   │   ├── admin_handler.py    # Admin panel
│   │   └── report_handler.py   # Hisobotlarni qabul qilish
│   └── bot.py                   # Asosiy bot
├── database/
│   ├── database.py              # Database klassi
│   └── schema.sql               # Ma'lumotlar bazasi sxemasi
├── scheduler/
│   └── scheduler.py             # Avtomatik vazifalar
├── utils/
│   ├── formatters.py            # Xabarlarni formatlash
│   ├── photo_hash.py            # Foto dublikat aniqlash
│   └── validators.py            # Validatsiya
├── config.py                    # Konfiguratsiya
├── main.py                      # Ishga tushirish
├── requirements.txt             # Python kutubxonalar
└── .env                         # Environment o'zgaruvchilar
```

## 🔧 Sozlamalarni o'zgartirish

`config.py` faylida:

- Deadline vaqtlarini o'zgartirish
- Eslatma vaqtlarini sozlash
- Statistika yuborish vaqtini belgilash
- Chat/Topic ID larni yangilash

## 📊 Statistika

### Kunlik hisobot (00:00)

- Har bir menjer bo'yicha 4 ta hisobot holati
- Vaqtida/Kech/Topshirilmagan
- Umumiy foiz

### Haftalik hisobot (Yakshanba 22:00)

- Haftalik ko'rsatkichlar
- Menjerlar reytingi
- Progress bar va foizlar

## ⚠️ Muhim eslatmalar

1. **Vaqt zonasi**: Barcha vaqtlar UTC+5 (Toshkent)
2. **Foto dublikat**: Oxirgi 3 kun ichidagi fotolar tekshiriladi
3. **Session timeout**: Admin panel 60 daqiqa
4. **Backup**: Ma'lumotlar bazasini muntazam backup qiling

## 🐛 Xatoliklarni aniqlash

Loglarni ko'rish:

```bash
cat bot.log
# yoki Windows da
type bot.log
```

## 📝 Lisenziya

Shaxsiy foydalanish uchun.

## 👨‍💻 Muallif

VIP Brand - Menejerlar nazorat tizimi
