"""
VIP Control Bot - Ishga tushirish skripti
"""
import sys
import os

# Loyiha yo'lini PATH ga qo'shish
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bot.bot import main

if __name__ == '__main__':
    main()
