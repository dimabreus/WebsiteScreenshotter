import os
from dotenv import load_dotenv

load_dotenv()

turnstile_secret_key = os.getenv('TURNSTILE_SECRET_KEY')

if not turnstile_secret_key:
    raise RuntimeError("TURNSTILE_SECRET_KEY is not specified.")
