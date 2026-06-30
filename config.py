from os import environ 

class Config:
    API_ID = environ.get("API_ID", "20599570")
    API_HASH = environ.get("API_HASH", "0d5a7f73ea37f1d11dd470cda9a1a75f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7357607802:AAF1f8v-rtO7NKQ12ooYQvt-IVmf905H79I") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ytuserbot12:30v6lYiMPLdUBM7d@cluster0.9l53pxx.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "ytuserbot12")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6858251193').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
