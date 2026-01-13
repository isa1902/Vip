@echo off
REM VIP Control Bot - Ishga tushirish skripti (Windows)

echo ===============================================
echo VIP CONTROL BOT - Ishga tushirish
echo ===============================================
echo.

REM Virtual environmentni faollashtirish
if exist "venv\Scripts\activate.bat" (
    echo Virtual environment faollashtirmoqda...
    call venv\Scripts\activate.bat
) else (
    echo XATO: Virtual environment topilmadi!
    echo Avval 'python -m venv venv' buyrug'ini bajaring
    pause
    exit /b 1
)

REM Botni ishga tushirish
echo.
echo Botni ishga tushirmoqda...
echo.
python main.py

pause
