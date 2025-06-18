from flask import Flask, request, render_template
from logger import log_event
from alerts import send_alert

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

    send_alert(ip, ua, username)

    return "Access Denied", 403

if __name__ == '__main__':
    app.run(port=8080)
