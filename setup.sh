#!/bin/bash
# =============================================
# BCTBomber v2.0 - Ultimate Installer
# Author: Jundul Kafa
# =============================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RESET='\033[0m'

clear
echo -e "${RED}"
cat << "EOF"
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║   ██████╗  ██████╗████████╗██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗
║   ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
║   ██████╔╝██║        ██║   ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
║   ██╔══██╗██║        ██║   ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
║   ██████╔╝╚██████╗   ██║   ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
║   ╚═════╝  ╚═════╝   ╚═╝   ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
║                                                                            ║
║              🔥 BCTBomber v2.0 - Ultimate SMS + Call Bomber 🔥             ║
║              📱 Bangladesh Optimized - Blackhat Edition                    ║
╚════════════════════════════════════════════════════════════════════════════╝
EOF
echo -e "${RESET}"

echo -e "${CYAN}╔═══════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${CYAN}║                  📦 INSTALLATION PROCESS                      ║${RESET}"
echo -e "${CYAN}╚═══════════════════════════════════════════════════════════════╝${RESET}"

# Check environment
echo -e "${YELLOW}[*] Checking environment...${RESET}"
if [ -d "/data/data/com.termux" ]; then
    echo -e "${GREEN}[✓] Termux detected${RESET}"
    TERMUX_MODE=true
else
    echo -e "${YELLOW}[!] Not in Termux, assuming Linux${RESET}"
    TERMUX_MODE=false
fi

# Update packages
echo -e "${YELLOW}[*] Updating packages...${RESET}"
if [ "$TERMUX_MODE" = true ]; then
    pkg update -y && pkg upgrade -y
else
    sudo apt update -y && sudo apt upgrade -y
fi

# Install dependencies
echo -e "${YELLOW}[*] Installing dependencies...${RESET}"
if [ "$TERMUX_MODE" = true ]; then
    pkg install -y python python-pip git nano
else
    sudo apt install -y python3 python3-pip git nano
fi

# Install Python packages
echo -e "${YELLOW}[*] Installing Python packages...${RESET}"
pip install -r requirements.txt

# Create data directory
echo -e "${YELLOW}[*] Setting up data directory...${RESET}"
mkdir -p data
echo "jundulbct" > data/passwords.txt
echo "0" > data/attempts.txt
echo "" > data/blacklist.txt

# Create launcher
echo -e "${YELLOW}[*] Creating launcher...${RESET}"
cat > bct << 'EOF'
#!/bin/bash
cd ~/BCTBomber
python bctbomber.py
EOF
chmod +x bct
if [ "$TERMUX_MODE" = true ]; then
    mv bct $PREFIX/bin/
else
    sudo mv bct /usr/local/bin/
fi

echo -e "${GREEN}"
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                    ✅ INSTALLATION COMPLETE!                                ║"
echo "║                                                                            ║"
echo "║   🔥 BCTBomber v2.0 is ready to use!                                      ║"
echo "║   📁 Location: ~/BCTBomber                                                ║"
echo "║   🔑 Password: jundulbct                                                  ║"
echo "║   🚀 Run with: bct                                                        ║"
echo "║                                                                            ║"
echo "║   ⚠️  WARNING: 3 wrong attempts = PERMANENT LOCK!                          ║"
echo "║   📱 Only for Bangladesh numbers (01x-xxxxxxx)                            ║"
echo "║                                                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo -e "${RESET}"

echo -e "${YELLOW}[*] Type 'bct' to start the bomber${RESET}"
