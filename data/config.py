from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')

GROUPS_ = [
-1002678298042
]

BOT_USERNAME = 'akbarali111test_bot'


Adwords = [
    "aksiya", "chegirma", "arzon", "yangilik", "sotuv", "sotiladi", "sotaman",
    "taklif", "foydali", "narxi", "bepul", "buyurtma", "buyurtma bering",
    "tezda", "maxsus taklif", "endilikda", "hozir", "bugun", "ertaga",
    "chegaralangan", "foydalang", "ulgurib qoling", "kafolat", "yetkazib berish",
    "bonus", "aksiya muddati", "savdo", "yangi", "super narx", "aksiyaga qo‘shiling",
    "pul ishlang", "online do‘kon", "yetkaziladi", "sifatli", "original", "brend",
    "ishonchli", "xizmatlar", "xizmat ko‘rsatish", "do‘kon", "mahsulot", "to‘lov",
    "karta orqali to‘lov", "telefon raqam", "aloqa", "bog‘laning", "telegram",
    "instagram", "sahifamizga yozing", "hamyonbop", "marketing", "promo", "kod",
    "chegirma kodi", "aksiyadan foydalaning", "ustama", "sovg‘a", "sovg‘a sifatida",
    "foydali narx", "aksiya davom etmoqda"
]
links = [
    "https://", "http://", "www.", ".uz", ".com", ".net", ".org", ".shop",
    "telegram.me", "t.me", "instagram.com", "facebook.com", "youtube.com",
    "link", "havola", "bosing", "sahifamiz", "profilimiz", "direct", "kanalga o‘ting", '.ru'
]


# Guruhda yozish qoidalari
group_rules = """
🔹 Guruhda Yozish Qoidalari 🔹

1. 🚫 Reklama Tarqatilmasligi
   Guruhda hech qanday reklama yoki tijorat xabarlari tarqatish qat'iyan man etiladi.
   Faqat guruhga mos va foydali ma'lumotlar bilan bo'lishing.

2. 📝 Bot Orqali Ro'yxatdan O'tish
   Guruhda yozish uchun bot orqali ro'yxatdan o'tish talab qilinadi.
   Bu jarayon oson va tez. Ro'yxatdan o'tganingizdan so'ng, guruhda faoliyat yuritishingiz mumkin.

3. 🧹 Kirdi-chiqdilarni Tozalash
   Har bir foydalanuvchi guruhga kirish yoki chiqish vaqtida chat tarixini tozalash imkoniyatiga ega.
   Bu chatni toza va tartibli saqlashga yordam beradi.
"""

# Chiqish

