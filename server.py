from flask import Flask, request, render_template, redirect, session, url_for, abort
import os
from logger import log_event
from alerts import send_alert
from ip_tracker import record_attempt, should_alert
from config import ALERT_THRESHOLD, ADMIN_USERNAME, ADMIN_PASSWORD

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def home():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited Home Page", "N/A")
    if 'username' in session:
        return render_template('home.html', is_admin=(session['username'] == 'admin'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')

    log_event(ip, ua, username, password)
    attempt_count = record_attempt(ip)

    if should_alert(ip, ALERT_THRESHOLD):
        send_alert(ip, ua, username, attempt_count)

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        session['logged_in'] = True
        session['username'] = username
        session['is_admin'] = True
        return redirect('/dashboard')

    elif username == "guest":
        session['logged_in'] = True
        session['username'] = username
        session['is_admin'] = False
        return redirect('/dashboard')

    abort(403)


@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect('/')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited /dashboard", session.get("username", "unknown"))
    return render_template('dashboard.html', is_admin=session.get('is_admin'))

@app.route('/settings')
def settings():
    if not session.get('logged_in'):
        return redirect('/')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited /settings", session.get("username", "unknown"))
    return render_template('settings.html', is_admin=session.get('is_admin'))

@app.route('/users')
def users():
    if not session.get('logged_in'):
        return redirect('/')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited /users", session.get("username", "unknown"))
    return render_template('users.html', is_admin=session.get('is_admin'))

@app.route('/api/config')
def config_leak():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Accessed /api/config", "N/A")
    send_alert(ip, ua, "Attempted config leak", 999)
    abort(403)

@app.route('/logout')
def logout():
    session.clear()
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Logged out", "N/A")
    return render_template('logout.html')

@app.errorhandler(404)
@app.errorhandler(403)
@app.errorhandler(500)
def handle_errors(e):
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, f"ERROR {e.code}", str(e))
    return render_template("error.html", error_code=e.code, error_message=str(e)), e.code


# For local hosting
#if __name__ == '__main__':
    app.run(port=8080)

# For lan hosting
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
