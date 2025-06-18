import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "letmein123"

ALERT_THRESHOLD = int(os.getenv("ALERT_THRESHOLD", 5))

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL")
SMTP_FROM_NAME = os.getenv("SMTP_FROM_NAME")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

ALERT_EMAIL_TO = os.getenv("ALERT_EMAIL_TO")
