import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

if not GOOGLE_API_KEY or not DATABASE_URL:
    raise Exception("Missing GOOGLE_API_KEY or DATABASE_URL in environment variables.")