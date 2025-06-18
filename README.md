# 🛡️ CyberSnare

A lightweight web-based **Admin Panel** designed for **cybersecurity learning, research, and experimentation**. This project is ideal for students, ethical hackers, and developers interested in understanding core security principles, login flows, and internal system interfaces.

---

## 🚀 Purpose

**CyberSnare** simulates a secure internal interface often found in enterprise environments. It provides a safe environment to:

- Practice user authentication and session control
- Explore admin/guest permission handling
- Experiment with web security best practices and misconfigurations
- Understand protected dashboards, system status interfaces, and settings panels

---

## 🧠 Features

- 🧑‍💼 Admin roles
- 🔐 Session-based access control
- ⚙️ Admin dashboard with:
  - System status
  - User management
  - Editable security settings (firewall simulation)
- 👁️ Custom error pages
- 📬 Email alert system via **SendGrid**
- 💡 Built with Flask and Bootstrap 5

---

## 🧰 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- A SendGrid account (for email alerts)

---

## 🔧 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/cybernilsen-admin-portal.git
cd cybernilsen-admin-portal
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up your environment variables**
```bash
ALERT_THRESHOLD=5

SENDGRID_API_KEY=your_sendgrid_api_key
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_FROM_EMAIL=verified_sender@example.com
SMTP_FROM_NAME=your_name

ALERT_EMAIL_TO=you@example.com
```
⚠️ Make sure SMTP_FROM_EMAIL is a verified sender in your SendGrid account (free or authenticated domain for example gmail account1 to  gmail account2 hence from and to).

---

**▶️ Running the App**
```bash
flask run
```
The app will be available at http://127.0.0.1:8080 and http://x.x.x.x:8080 your lan side IP.

---

**🧪 Default Users (for testing)**
Username |	Password |	Role
admin |	letmein123 |	Administrator
> You can customize or expand this in the config Python file.

---

**Learning Focus** 
This project includes:

- Secure session handling using Flask

-Admin privilege

- Fake configurable firewall simulation panel

- SendGrid email alerts

- Clean UI with Bootstrap 5

- Modular template structure (layout.html, dashboard.html, etc.)

- General learning concept of what a honeypot is and what it does

---

**⚠️ Disclaimer**
This project is for educational purposes only and to learn the concept of a honeypot. Do not deploy this in production environments without proper hardening, security reviews, and authentication measures. 

---

**📄 License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**🙌 Credits**
Created with ❤️ by CyberNilsen






