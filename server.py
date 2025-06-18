from flask import Flask, request, render_template
from logger import log_event
from alerts import send_alert
from ip_tracker import record_attempt, should_alert
from config import ALERT_THRESHOLD, ADMIN_USERNAME, ADMIN_PASSWORD

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')

    log_event(ip, ua, username, password)
    attempt_count = record_attempt(ip)

    if should_alert(ip, ALERT_THRESHOLD):
        send_alert(ip, ua, username, attempt_count)

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return ('/dashboard')

    return "Access Denied", 403


@app.route('/dashboard')
def dashboard():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited /dashboard", "N/A")
    return render_template('dashboard.html')

@app.route('/settings')
def settings():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited /settings", "N/A")
    return render_template('settings.html')

@app.route('/users')
def users():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited /users", "N/A")
    return render_template('users.html')

@app.route('/api/config')
def config_leak():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Accessed /api/config", "N/A")
    send_alert(ip, ua, "Attempted config leak", 999)
    return "403 Forbidden", 403

@app.route('/logout')
def logout():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited /logout", "N/A")
    return render_template('logout.html')


if __name__ == '__main__':
    app.run(port=8080)
