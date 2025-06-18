# 🛡️ CyberSnare

A lightweight, web-based **Admin Panel honeypot** designed for **cybersecurity learning, experimentation, and research**.  
Ideal for students, ethical hackers, and developers who want hands-on experience with authentication flows, access control, and simulated secure interfaces.



## 🚀 Purpose

**CyberSnare** simulates an internal administration portal commonly found in enterprise environments. It provides a **controlled, safe environment** to:

- Practice user login/session management  
- Understand role-based access control (admin vs guest)  
- Experiment with misconfigurations and UI/UX pitfalls  
- Visualize system status and simulated settings  
- Learn core concepts behind honeypots and defensive deception  



## 🧠 Features
This project is designed to help you learn and experiment with:

- 🔐 Login system with session-based access control  
- 🧑‍💼 Admin dashboard with:
  - ✅ System status overview  
  - 👥 User management interface  
  - 🔥 Editable firewall rules (simulated)  
- 📬 Email alerts via **SendGrid**  
- ⚠️ Custom error pages for 403 / 404 / 500  
- ✨ Clean, responsive UI with Bootstrap 5  
- 🧪 Predefined users for safe testing  
- 🧲 Built as an educational honeypot concept  


## 🧰 Prerequisites

Make sure you have the following installed:

- Python **3.8+**  
- [pip](https://pip.pypa.io/en/stable/)  
- A verified **SendGrid account** (for sending email alerts)  

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/cybersnare.git
cd cybersnare
```
2. Create and activate a virtual environment
```bash
python -m venv venv
```
3. Install Python dependencies
```bash
pip install -r requirements.txt
```
4. Set up environment variables
Create a .env file in the root directory:
# .env

```
ALERT_THRESHOLD=5

SENDGRID_API_KEY=your_sendgrid_api_key
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_FROM_EMAIL=verified_sender@example.com
SMTP_FROM_NAME=your_name

ALERT_EMAIL_TO=your_email@example.com
```
⚠️ Important: SMTP_FROM_EMAIL must be a verified sender in your SendGrid account (e.g. a verified Gmail address or authenticated domain).

## ▶️ Running the App
```bash
flask run
```
Visit:
http://127.0.0.1:8080 (localhost)
http://<your-lan-ip>:8080 (on your LAN)



## 🧪 Default Users
| Username |	Password |	Role |
|----------|-----------|-------|
| admin |	letmein123 |	Administrator |

You can customize users in the config.py or similar config file.



## ⚠️ Disclaimer
This project is intended for educational and research purposes only.
It is not secure for production use without significant hardening and proper authentication/security reviews.



## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



## 🙌 Credits
Created with ❤️ by CyberNilsen
