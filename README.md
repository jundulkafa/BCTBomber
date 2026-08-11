# 📲 BCTBomber v2.0 - Ultimate SMS + Call Bomber 🔥

[![Version](https://img.shields.io/badge/version-2.0-red.svg)](https://github.com/jundulkafa/BCTBomber)
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://python.org)
[![Termux](https://img.shields.io/badge/Termux-Android-green.svg)](https://termux.com)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/jundulkafa/BCTBomber.svg)](https://github.com/jundulkafa/BCTBomber/stargazers)
[![Forks](https://img.shields.io/github/forks/jundulkafa/BCTBomber.svg)](https://github.com/jundulkafa/BCTBomber/network)

> ⚠️ **DISCLAIMER:** This tool is for **educational and authorized testing purposes only**. The author is not responsible for any misuse or illegal activities. Use at your own risk.

---

## 👨‍💻 **Author**
**Jundul Kafa**  
- GitHub: [@jundulkafa](https://github.com/jundulkafa)  
- Telegram: [@bcthacker](https://t.me/bcthacker)  
- Discord: BCT#1337

---

## 🚀 **Features**

| Icon | Feature | Description |
|------|---------|-------------|
| 📨 | **SMS Bombing** | Send unlimited SMS via multiple gateways |
| 📞 | **Call Bombing** | Make thousands of calls via SIP (no registration) |
| 💀 | **Dual-Mode** | SMS + Call simultaneously for maximum impact |
| 🔒 | **Password Protected** | Secure access with `jundulbct` |
| 🚫 | **3-Strike Lockout** | Permanent IP blacklist after 3 failed attempts |
| 📱 | **Bangladesh Optimized** | Validates 11-digit 01x numbers |
| 🧵 | **Multi-Threading** | 10-200 threads for maximum speed |
| 🎨 | **Color Output** | Beautiful terminal UI with real-time stats |
| 🔄 | **Auto-Retry** | Failed requests automatically retry |
| 🌐 | **Multi-Gateway** | Multiple SMS providers for redundancy |
| 🛡️ | **Anti-Detection** | Rotating proxies and random delays |
| ⚡ | **Lightning Fast** | Optimized for maximum performance |

---

## 📦 **Requirements**

| Requirement | Details |
|-------------|---------|
| 📱 **Termux** | Android terminal emulator (F-Droid version) |
| 🐍 **Python** | Version 3.6 or higher |
| 🌐 **Internet** | WiFi or Mobile Data connection |
| 💾 **Storage** | Minimum 50MB free space |
| 🧠 **RAM** | 2GB+ recommended for multi-threading |

---

## 🛠 **Installation (Termux)**

### **Method 1: Full Installation (Recommended)**

```bash
# 📦 Update packages
pkg update && pkg upgrade -y

# 🐍 Install Python and Git
pkg install python python-pip git -y

# 📥 Clone the repository
git clone https://github.com/jundulkafa/BCTBomber.git
cd BCTBomber

# 🔧 Run the installer
bash setup.sh

# 🚀 Launch
bct
```

### **Method 2: 🔥 SINGLE LINE INSTALLATION (Fastest)**

```bash
pkg update -y && pkg upgrade -y && pkg install python python-pip git -y && pip install requests colorama && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh
```

### **Method 3: 📱 EVEN SHORTER (For lazy people)**

```bash
pkg update -y && pkg install python git -y && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh
```

### **Method 4: ⚡ ULTIMATE ONE-LINER (Auto-everything)**

```bash
pkg update -y && pkg upgrade -y && pkg install python python-pip git -y && pip install requests colorama && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh && bct
```

---

## 🔑 **Password & Security**

| Item | Value |
|------|-------|
| 🔑 **Default Password** | `jundulbct` |
| 🔢 **Max Attempts** | 3 |
| 🔒 **Lockout** | Permanent IP blacklist |
| 📁 **Blacklist File** | `data/blacklist.txt` |
| 📝 **Attempts File** | `data/attempts.txt` |

### **If You Get Locked Out:**

```bash
# 🔓 Reset blacklist
nano data/blacklist.txt  # Delete your IP and save

# 🔄 Complete reset
rm -rf ~/BCTBomber/data
```

---

## 📱 **Usage Guide**

### **Option 1: 📨 SMS Bombing**

```bash
1️⃣ Select [1] from menu
2️⃣ Enter target (e.g., 017xxxxxxxx)
3️⃣ Enter custom message
4️⃣ Enter number of SMS (1000+)
5️⃣ Enter threads (10-50)
6️⃣ Confirm and watch the chaos 🔥
```

### **Option 2: 📞 Call Bombing**

```bash
1️⃣ Select [2] from menu
2️⃣ Enter target (e.g., 017xxxxxxxx)
3️⃣ Enter number of calls (1000+)
4️⃣ Enter threads (50-200)
5️⃣ Confirm and watch the ringing 📳
```

### **Option 3: 💀 Dual-Mode (SMS + Call)**

```bash
1️⃣ Select [3] from menu
2️⃣ Enter target
3️⃣ Enter SMS message
4️⃣ Enter SMS count
5️⃣ Enter call count
6️⃣ Enter threads (20-100)
7️⃣ Confirm for simultaneous attack ⚡
```

---

## 🔧 **Technical Details**

### **📨 SMS Gateways Used:**

| # | Gateway | Status |
|---|---------|--------|
| 1 | **Infobip API** | ✅ Primary (Working) |
| 2 | **TextLocal API** | ✅ Backup |
| 3 | **Free Mobile API** | ⏳ Fallback |

### **📞 Call Method Used:**

| # | Method | Description |
|---|--------|-------------|
| 1 | **Public SIP Servers** | No registration required |
| 2 | **Rotating Proxy IPs** | Anti-detection |
| 3 | **Raw UDP Packets** | Direct SIP INVITE flooding |

### **🧵 Threading Model:**

| Attack Type | Threads | Speed |
|-------------|---------|-------|
| 📨 SMS Bombing | 10-50 | 10-20 SMS/sec |
| 📞 Call Bombing | 50-200 | 50-100 calls/sec |
| 💀 Dual-Mode | 20-100 | Combined |

---

## ⚡ **Quick Commands**

```bash
# 🔧 Install
bash setup.sh

# 🚀 Launch
bct

# 📥 Update
git pull

# 🔄 Reinstall
rm -rf ~/BCTBomber && git clone https://github.com/jundulkafa/BCTBomber.git && cd BCTBomber && bash setup.sh

# 📊 Check logs
cat data/attempts.txt

# 🔓 Reset password
echo "newpassword" > data/passwords.txt
```

---

## 📂 **File Structure**

```
BCTBomber/
├── 📄 README.md          # Documentation
├── 📄 LICENSE            # MIT License
├── 📄 requirements.txt   # Python dependencies
├── 🔧 setup.sh           # Installer script
├── 🐍 bctbomber.py       # Main application
└── 📁 data/              # Data storage
    ├── 🔒 passwords.txt  # Encrypted password
    ├── 📝 attempts.txt   # Failed attempt counter
    └── 🚫 blacklist.txt  # Blocked IPs
```

---

## 🛡️ **Security Features**

| Feature | Description |
|---------|-------------|
| 🔑 **Password Authentication** | Secure access control |
| 🔢 **3-Attempt Lockout** | Brute force protection |
| 🚫 **IP Blacklisting** | Permanent block after 3 fails |
| 🔒 **Encrypted Storage** | Password protection |
| 🛡️ **Anti-Debugging** | Basic protection measures |
| ✅ **Error Handling** | Graceful failure recovery |

---

## 📊 **Performance Metrics**

| Attack Type | Speed | Success Rate | Best For |
|-------------|-------|--------------|----------|
| 📨 SMS Bombing | 10-20/sec | 70-85% | Maximum harassment |
| 📞 Call Bombing | 50-100/sec | 60-75% | Network disruption |
| 💀 Dual-Mode | Combined | 65-80% | Maximum damage |

*Results vary based on network conditions and API limits*

---

## 🎯 **Target Requirements**

| Requirement | Details |
|-------------|---------|
| 📱 **Country** | Bangladesh |
| 🔢 **Format** | 11 digits, starts with 01 |
| 📞 **Operators** | 013, 014, 015, 016, 017, 018, 019 |
| ✅ **Example** | `017xxxxxxxx` (without +88) |

---

## ⚠️ **Legal Disclaimer**

This tool is provided **for educational and security testing purposes only**.

✅ **Allowed:**
- Testing on your own numbers
- Testing with explicit permission
- Security research and education

❌ **Not Allowed:**
- Harassment or spamming
- Illegal activities
- Unauthorized testing
- Commercial use without permission

**⚠️ The author assumes no responsibility for misuse. Users are solely responsible for their actions.**

---

## 📞 **Support & Contact**

| Platform | Handle |
|----------|--------|
| 🐙 **GitHub** | [@jundulkafa](https://github.com/jundulkafa) |
| ✈️ **Telegram** | [@bcthacker](https://t.me/bcthacker) |
| 💬 **Discord** | BCT#1337 |
| 📧 **Email** | jundulkafa@protonmail.com |
| 🐞 **Issues** | [Report here](https://github.com/jundulkafa/BCTBomber/issues) |

---

## 🌟 **Star & Fork**

If you find this useful, please consider starring ⭐ and forking 🍴 the repository!

[![GitHub stars](https://img.shields.io/github/stars/jundulkafa/BCTBomber.svg)](https://github.com/jundulkafa/BCTBomber/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/jundulkafa/BCTBomber.svg)](https://github.com/jundulkafa/BCTBomber/network)

---

## 📝 **Changelog**

### **v2.0** (Latest) 🆕
- ✅ Dual-mode (SMS + Call) 💀
- ✅ Password protection 🔒
- ✅ 3-strike lockout 🚫
- ✅ Multi-threading 🧵
- ✅ Bangladesh validation 📱
- ✅ Color output 🎨
- ✅ Professional README 📄
- ✅ One-line installation ⚡

### **v1.0** (Initial) 🐣
- SMS bombing only 📨
- Single gateway 🌐
- Basic functionality ✅

---

## 🤝 **Contributing**

We welcome contributions! Please:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch
3. 💾 Commit your changes
4. 📤 Push to the branch
5. 🔀 Open a Pull Request

---

**Made with 💀 by Jundul Kafa & BCT Team**

*"With great power comes great responsibility. Use wisely."*

---

## ⭐ **Support Us**

If you like this project, please:
- ⭐ Star the repository
- 🍴 Fork it
- 📤 Share with others
- 💰 Donate (coming soon)

---

**Thank you for using BCTBomber! 🚀**

---
