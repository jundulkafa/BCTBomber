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

### **Method 1: Full Installation (Recommended)**

```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python and Git
pkg install python python-pip git -y

# Clone the repository
git clone https://github.com/jundulkafa/BCTBomber.git
cd BCTBomber

# Run the installer
bash setup.sh

# Launch
bct
Method 2: 🔥 SINGLE LINE INSTALLATION (Fastest)
bash
pkg update -y && pkg upgrade -y && pkg install python python-pip git -y && pip install requests colorama && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh
Method 3: 📱 EVEN SHORTER (For lazy people)
bash
pkg update -y && pkg install python git -y && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh
Method 4: ⚡ ULTIMATE ONE-LINER (Auto-everything)
bash
pkg update -y && pkg upgrade -y && pkg install python python-pip git -y && pip install requests colorama && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh && bct
🔑 Password & Security
Item	Value
Default Password	jundulbct
Max Attempts	3
Lockout	Permanent IP blacklist
If You Get Locked Out:
bash
# Reset blacklist
nano data/blacklist.txt  # Delete your IP

# Or complete reset
rm -rf ~/BCTBomber/data
📱 Usage Guide
Option 1: SMS Bombing
bash
1. Select [1] from menu
2. Enter target (e.g., 017xxxxxxxx)
3. Enter custom message
4. Enter number of SMS (1000+)
5. Enter threads (10-50)
6. Confirm and watch the chaos
Option 2: Call Bombing
bash
1. Select [2] from menu
2. Enter target (e.g., 017xxxxxxxx)
3. Enter number of calls (1000+)
4. Enter threads (50-200)
5. Confirm and watch the ringing
Option 3: Dual-Mode (SMS + Call)
bash
1. Select [3] from menu
2. Enter target
3. Enter SMS message
4. Enter SMS count
5. Enter call count
6. Enter threads (20-100)
7. Confirm for simultaneous attack
🔧 SMS Gateways Used:
Infobip API (Primary - working)

TextLocal API (Backup)

Free Mobile API (Fallback)

📞 Call Method Used:
Public SIP servers (no registration)

Rotating proxy IPs

Raw UDP packets

⚡ Quick Commands
bash
# Install
bash setup.sh

# Launch
bct

# Update
git pull

# Reinstall
rm -rf ~/BCTBomber && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh
⚠️ Legal Disclaimer
This tool is provided for educational and security testing purposes only.

✅ Use on your own numbers for testing

✅ Use with explicit permission

❌ Do not harass or spam

❌ Do not use for illegal activities

The author assumes no responsibility for misuse. Users are solely responsible for their actions.

🌟 Star & Fork
https://img.shields.io/github/stars/jundulkafa/BCTBomber.svg
https://img.shields.io/github/forks/jundulkafa/BCTBomber.svg

Made with 💀 by Jundul Kafa

Remember: With great power comes great responsibility. Use wisely.

text

---

## 🚀 **QUICK COMMANDS TO UPDATE README**

```bash
# Navigate to project
cd ~/BCTBomber

# Open README
nano README.md

# Select all and paste the content above
# Ctrl+A (select all), Ctrl+U (paste in nano)

# Save and exit
# Ctrl+X, then Y, then Enter

# Push to GitHub
git add README.md
git commit -m "Updated README with complete installation guide"
git push
