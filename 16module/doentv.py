import os
from dotenv import load_dotenv


load_dotenv()

print(os.getenv("name"))

# Reads the key-value pair from .env file and adds them to environment variable.