# 📲 BCTBomber v2.0 - Ultimate SMS + Call Bomber

[![Version](https://img.shields.io/badge/version-2.0-red.svg)](https://github.com/jundulkafa/BCTBomber)
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://python.org)
[![Termux](https://img.shields.io/badge/Termux-Android-green.svg)](https://termux.com)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)

> ⚠️ **DISCLAIMER:** This tool is for **educational and authorized testing purposes only**. The author is not responsible for any misuse or illegal activities. Use at your own risk.

---

## 👨‍💻 **Author**
**Jundul Kafa**  
- GitHub: [@jundulkafa](https://github.com/jundulkafa)  
- Telegram: [@bcthacker](https://t.me/bcthacker)  

---

## 🚀 **Features**

| Feature | Description |
|---------|-------------|
| 📨 **SMS Bombing** | Send unlimited SMS via multiple gateways |
| 📞 **Call Bombing** | Make thousands of calls via SIP (no registration) |
| 💀 **Dual-Mode** | SMS + Call simultaneously for maximum impact |
| 🔒 **Password Protected** | Secure access with `jundulbct` |
| 🚫 **3-Strike Lockout** | Permanent IP blacklist after 3 failed attempts |
| 📱 **Bangladesh Optimized** | Validates 11-digit 01x numbers |
| 🧵 **Multi-Threading** | 10-200 threads for maximum speed |
| 🎨 **Color Output** | Beautiful terminal UI with real-time stats |

---

## 📦 **Requirements**

- **Termux** (Android) or **Linux** (Kali, Ubuntu)
- **Python 3.6+**
- **Internet Connection**

---

## 🛠 **Installation (Termux)**

```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python and Git
pkg install python python-pip git -y

# Clone the repository
git clone https://github.com/jundulkafa/BCTBomber.git
cd BCTBomber

🔥 SINGLE LINE TERMUX INSTALLATION
bash
pkg update -y && pkg upgrade -y && pkg install python python-pip git -y && pip install requests colorama && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh
📱 EVEN SHORTER (For lazy people)
bash
pkg update -y && pkg install python git -y && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh
⚡ ULTIMATE ONE-LINER (Auto-everything)
bash
pkg update -y && pkg upgrade -y && pkg install python python-pip git -y && pip install requests colorama && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh && bct


# Run the installer
bash setup.sh

# Launch
bct
