from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "12857763"))
API_HASH = getenv("API_HASH", "7b71e8bca0d5e1c6d8383ae818d9ec8d")

BOT_TOKEN = getenv("BOT_TOKEN", "6375262996:AAFZBXDHSjs6Yn5M_1CbV_XS-tWQqG_wYX4")
OWNER_ID = int(getenv("OWNER_ID", "1345594412"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://doadmin:K90G2U3H5Pk4g81R@mongodb-arab2-e696a84d.mongo.ondigitalocean.com/admin?authSource=admin&tls=true")
