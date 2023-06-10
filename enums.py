import os
from dotenv.main import load_dotenv


load_dotenv()

TEST_EMAIL = os.environ["TEST_EMAIL"]
MAIN_EMAIL = os.environ["MAIN_EMAIL"]
TOKEN = os.environ["TOKEN"]
SENDED_TXT = "sended.txt"
NOT_SENDED_TXT = "not_sended.txt"
EMAILS_TO_IGNORE = (
    "0@0.se",
)
