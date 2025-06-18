from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY, SMTP_FROM_EMAIL, ALERT_EMAIL_TO

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

    message = Mail(
        from_email=SMTP_FROM_EMAIL,
        to_emails=ALERT_EMAIL_TO,
        subject=subject,
        plain_text_content=body
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"[+] Email alert sent! Status: {response.status_code}")
    except Exception as e:
        print(f"[!] Failed to send email alert: {e}")
