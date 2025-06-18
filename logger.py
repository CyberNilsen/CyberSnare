import datetime

def log_event(ip, user_agent, username, password):
    with open("honeypot.log", "a") as f:
        f.write(f"[{datetime.datetime.now()}] IP: {ip}, UA: {user_agent}, USER: {username}, PASS: {password}\n")
