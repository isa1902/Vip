# QUICK START - Tezkor boshlash yo'riqnomasi

## 📦 Kerakli dasturlar

1. **Python 3.9+** - [python.org](https://python.org)
2. **PostgreSQL 12+** - [postgresql.org](https://postgresql.org)
3. **Telegram Bot Token** - @BotFather dan

## ⚡ Tezkor o'rnatish (5 qadam)

### 1. Virtual muhit yaratish

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Kutubxonalarni o'rnatish

```powershell
pip install -r requirements.txt
```

### 3. PostgreSQL sozlash

PostgreSQL da yangi database yaratish:

```sql
-- PostgreSQL SQL Shell (psql) da bajaring
CREATE DATABASE vip_control_bot;
CREATE USER bot_user WITH PASSWORD 'your_password_here';
GRANT ALL PRIVILEGES ON DATABASE vip_control_bot TO bot_user;
\q
```

Sxemani yuklash:

```powershell
# PowerShell da
& 'C:\Program Files\PostgreSQL\15\bin\psql.exe' -U bot_user -d vip_control_bot -f database\schema.sql
```

### 4. .env faylini sozlash

`.env.example` dan `.env` ga ko'chirish:

```powershell
copy .env.example .env
notepad .env
```

`.env` faylida to'ldiring:

```env
DB_HOST=localhost
DB_NAME=vip_control_bot
DB_USER=bot_user
DB_PASSWORD=your_password_here  # ⬅️ O'zgartiring!

ADMIN_PASSWORD=Spectr@2008
BOT_TOKEN=8542494278:AAELsdOoG0msjStbJnc9gD-8qn2naxX34rw
```

### 5. Botni guruhga qo'shish va ishga tushirish

1. **Botni guruhga a'zo qilish**
   - Guruhga boring
   - Add Members > @your_bot_username
   
2. **Admin huquqlarini berish**
   - Group Members > Bot
   - ✅ Delete messages
   - ✅ Pin messages
   - ✅ Manage topics
   
3. **Botni ishga tushirish**

```powershell
python main.py
```

Yoki:

```powershell
.\start_bot.bat
```

## 🎯 Birinchi kirish (Admin panel)

1. Telegram da botga shaxsiy chatda `/start` yuboring
2. **Login:** `negmuradov`
3. **Parol:** `Spectr@2008`

## 📝 Birinchi sozlamalar

Admin panelda:

1. **Filial qo'shish**
   - Menyu > Filiallar > Filial qo'shish
   - Nom kiriting (masalan: "Yangi Hayot")

2. **Menjer qo'shish**
   - Menyu > Menejerlar > Menjer qo'shish
   - Ism: "Ali Valiyev"
   - Telegram ID: `123456789` (menejerning ID si)
   - Filial: "Yangi Hayot"

3. **Statistika guruhini ulash**
   - Botni statistika guruhiga qo'shing
   - Group ID ni oling va `config.py` da yangilang

## ✅ Test qilish

Menejer sifatida guruhga foto + caption yuboring:

```
Yangi Hayot otdel
```

Bot javob berishi kerak:
```
✅ Hisobot qabul qilindi!
📊 Tur: OTDEL
🏢 Filial: Yangi Hayot
⏰ Vaqt: 13.01.2026 14:30
```

## ⚠️ Muammolarni hal qilish

### Database ulanmayapti

```powershell
# PostgreSQL ishlaganini tekshiring
& 'C:\Program Files\PostgreSQL\15\bin\pg_isready.exe'
```

### Bot ishga tushmayapti

```powershell
# Loglarni ko'ring
type bot.log
```

### Foto qabul qilinmayapti

- Bot guruhda admin ekanligini tekshiring
- Caption formati to'g'riligini tekshiring
- Filial bazada mavjudligini tasdiqlang

## 📞 Yordam

Muammolar bo'lsa:
1. `bot.log` faylini ko'ring
2. PostgreSQL ulanishini tekshiring
3. Bot tokenini tasdiqlang
4. Admin huquqlarini tekshiring

## 🚀 Keyingi qadamlar

- [ ] Barcha menejerlarni qo'shing
- [ ] Barcha filiallarni qo'shing  
- [ ] Test hisobotlar yuboring
- [ ] 24 soat kutib statistikani ko'ring
- [ ] Backup rejasini sozlang

---

**Omad tilaymiz! 🎉**
