ip_attempts = {}

def record_attempt(ip):
    if ip not in ip_attempts:
        ip_attempts[ip] = 1
    else:
        ip_attempts[ip] += 1
    return ip_attempts[ip]

def should_alert(ip, threshold):
    return ip_attempts.get(ip, 0) >= threshold
