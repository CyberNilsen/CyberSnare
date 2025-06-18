import smtplib
from email.mime.text import MIMEText
from config import SMTP_HOST, SMTP_PORT, SMTP_FROM_EMAIL, SMTP_FROM_NAME, SENDGRID_API_KEY, ALERT_EMAIL_TO

def send_alert(ip, user_agent, username, attempts):
    print(f"[ALERT] {ip} tried logging in as {username} using {user_agent} (Attempt #{attempts})")
    
    subject = "HONEYPOT ALERT 🚨"
    body = f"""
    Alert! A suspicious login attempt was detected.

    IP Address: {ip}
    User-Agent: {user_agent}
    Username: {username}
    Attempt #: {attempts}
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = f"{SMTP_FROM_NAME} <{SMTP_FROM_EMAIL}>"
    msg["To"] = ALERT_EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login("apikey", SENDGRID_API_KEY)
            server.sendmail(SMTP_FROM_EMAIL, ALERT_EMAIL_TO, msg.as_string())
        print("[+] Email alert sent!")
    except Exception as e:
        print(f"[!] Failed to send email alert: {e}")
