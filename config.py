import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    APP_NAME = os.getenv("APP_NAME", "Production Health API")
    VERSION = os.getenv("VERSION", "1.0.0")

    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")

    AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
    S3_BUCKET = os.getenv("S3_BUCKET", "")