import os
from dotenv import load_dotenv

load_dotenv()

turnstile_secret_key = os.getenv('TURNSTILE_SECRET_KEY')
