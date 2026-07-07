# 🚨 Automated SRE Incident Escalation Bot

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Requests](https://img.shields.io/badge/Library-Requests-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📖 Overview
In modern Operations Engineering, minimizing Mean Time to Detection (MTTD) is critical. This project is a lightweight, automated health-checking service designed to monitor critical infrastructure endpoints. When a service degradation or outage is detected (e.g., HTTP 4xx or 5xx errors, connection timeouts), the bot immediately escalates the incident via Webhook to a designated support channel, enforcing Service Level Agreement (SLA) visibility.

## ✨ Key Features
* **Proactive Monitoring:** Continuously polls a configurable list of URLs for availability and uptime.
* **Intelligent Error Handling:** Captures not just HTTP error codes, but also connection timeouts, DNS failures, and TCP rejections.
* **SLA Enforcement:** Alerts include timestamps and explicit SLA countdowns to ensure engineers acknowledge critical SEV-1 incidents promptly.
* **Secure by Design:** Uses environment variables for Webhook URLs, ensuring no sensitive secrets are hardcoded into the repository.

## 🏗️ Architecture & Tech Stack
* **Language:** Python 3.x
* **Core Libraries:** `requests` (HTTP handling), `os` (Environment variable management), `datetime` (Timestamping), `time` (Loop polling).
* **Integration:** Discord/Slack Webhooks via JSON payloads.

---

## 📸 Incident Alert Example

<img width="1146" height="604" alt="Screenshot 2026-07-07 181442" src="https://github.com/user-attachments/assets/77cfebaa-f9e9-440e-a0d8-e36fea55553c" />
<img width="1200" height="653" alt="Screenshot 2026-07-07 180143" src="https://github.com/user-attachments/assets/90299fb4-a7b9-4557-a0e8-de8d18f906e7" />

*Example of a Sev-1 alert triggered by a 500 Internal Server Error, detailing the affected endpoint, time of failure, and SLA.*

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher installed.
* A Discord or Slack workspace with Webhook permissions.

### 1. Clone the Repository
```bash
git clone [https://github.com/YourUsername/sre-escalation-bot.git](https://github.com/YourUsername/sre-escalation-bot.git)
cd sre-escalation-bot
