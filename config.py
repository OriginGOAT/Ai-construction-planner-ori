import os
from dotenv import load_dotenv

# load values from .env file
load_dotenv()

# read API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
