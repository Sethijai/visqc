import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "29626867")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "82b19751497d00e47c3032409d130423") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6906281434:AAFu3P7NslUS4Nh0aRN45Wf5Q59ONGYAqeI") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002072979014') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://namanjain123eudhc:opmaster@cluster0.5iokvxo.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6650589235 5487643307")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002138960289')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/bd21f0b96f8af58016488.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
