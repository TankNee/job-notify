import dotenv
import re

def check_mail_fomat(mail_address: str):
    if not mail_address:
        return False
    if not re.match(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', mail_address):
        return False
    return True

def load_env(env_path: str):
    dotenv.load_dotenv(dotenv_path=env_path, override=True)