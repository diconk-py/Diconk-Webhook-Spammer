# 💥 Diconk Webhook Spammer
![diconk preview](https://github.com/user-attachments/assets/6f53e4f5-6851-4942-8974-6e818db7a7a4)
**Diconk Webhook Spammer** is a high-speed, fully asynchronous Discord webhook spammer written in Python.  
It supports RGB gradient themes in terminal, multiple webhooks, proxy rotation, and a clean user experience — all in style.

> ⚠️ **Educational use only. Do not use this tool maliciously.**

---

## 📦 Requirements

- **Python** 3.13.3+
- Python packages:
  - [`aiohttp`](https://pypi.org/project/aiohttp/)
  - [`colorama`](https://pypi.org/project/colorama/)

---

## 🔧 Installation

1. **Clone this repository**
```bash
git clone https://github.com/diconk-py/Diconk-Webhook-Spammer
cd Diconk-Webhook-Spammer
```

2. **Install dependencies**

- **Automatic (Windows only)**:
```bat
start download requirements.bat
```

- **Manual (cross-platform)**:
```bash
pip install aiohttp colorama
```

---

## 🚀 Usage

1. **Start the launcher:**

```bat
start Diconk-Launcher.bat
```

Or to **test proxies first**:

```bat
start Test-Proxies-Launcher.bat
```

2. **Answer the prompts:**

- `Use proxies? (yes/no)`
- `Paste your webhook URLs` *(separated by spaces)*
- `Enter the message to spam`

3. ✅ **Done!** Messages will now be sent across all webhooks using async concurrency with rate-limit handling.

---

## 📂 Project Structure

```
├── Diconk-Webhook-Spammer.py        # Main script
├── Diconk-Launcher.bat              # Starts the spammer
├── test_proxies.py                  # Validates proxy servers
├── Test-Proxies-Launcher.bat        # Starts the proxy tester
├── requirements.bat                 # Installs aiohttp & colorama
├── proxies.txt                      # List your proxies here
├── proxies_working.txt              # Output file of working proxies
```

---

## ✅ Features

- 📤 Supports **multiple webhooks**
- 🌈 **Violet → Blue gradient** terminal interface
- 🌐 Optional **proxy rotation**
- 🚫 Graceful handling of rate-limits (`429`)
- 🖥️ Compatible with Windows and Linux (terminal)

---

## ⚠️ Disclaimer

This project is intended **for educational and ethical use only**.  
Do **not** use this tool to:

- Spam or harass Discord servers you do not own
- Bypass security systems or moderation
- Violate Discord’s [Terms of Service](https://discord.com/terms)

By using this script, **you take full responsibility** for any actions or consequences.  
Please respect others’ work and communities.

---

Made with 🛠️ by **Diconk**
