import datetime

def log_event(ip, user_agent, action, detail="N/A", username=None, referrer=None, language=None):
    timestamp = datetime.datetime.utcnow().isoformat()
    log_entry = (
        f"[{timestamp}] IP: {ip} | UA: {user_agent} | ACTION: {action} | "
        f"USER: {username or 'Unknown'} | DETAIL: {detail} | "
        f"REF: {referrer or 'N/A'} | LANG: {language or 'N/A'}\n"
    )
    with open("honeypot.log", "a") as f:
        f.write(log_entry)
