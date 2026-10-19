#!/usr/bin/env bash
# ============================================
# KID NUCLEI (CLOUDFEAR v9.5) - ULTIMATE INSTALLER
# Support: Termux, Kali, Ubuntu, Debian, Arch, Fedora, Alpine
# ============================================

set -e

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════╗"
echo "║   KID NUCLEI - ULTIMATE INSTALLER v2.0   ║"
echo "╚══════════════════════════════════════════╝"
echo -e "${NC}"

# ============ 1. DETEKSI ENVIRONMENT ============
if [ -d "/data/data/com.termux" ]; then
    ENV="termux"; PKG="pkg"; INSTALL_CMD="pkg install -y"; SUDO=""
elif command -v apt &>/dev/null; then
    ENV="debian"; PKG="apt"; [ "$EUID" -ne 0 ] && SUDO="sudo"; INSTALL_CMD="$SUDO apt install -y"
elif command -v pacman &>/dev/null; then
    ENV="arch"; PKG="pacman"; [ "$EUID" -ne 0 ] && SUDO="sudo"; INSTALL_CMD="$SUDO pacman -S --noconfirm"
elif command -v dnf &>/dev/null; then
    ENV="fedora"; PKG="dnf"; [ "$EUID" -ne 0 ] && SUDO="sudo"; INSTALL_CMD="$SUDO dnf install -y"
elif command -v apk &>/dev/null; then
    ENV="alpine"; PKG="apk"; [ "$EUID" -ne 0 ] && SUDO="sudo"; INSTALL_CMD="$SUDO apk add"
else
    echo -e "${RED}[ERR]${NC} Distro tidak dikenali. Install manual: python3, pip3, git"
    exit 1
fi

echo -e "${GREEN}[OK]${NC} OS: ${CYAN}$ENV${NC} | Pkg: ${CYAN}$PKG${NC}"

# ============ 2. INSTALL SISTEM DEPENDENSI (BIAR COMPILE PYTHON GAK ERROR) ============
echo -e "\n${CYAN}[INFO]${NC} Update repositori & install paket dasar sistem..."

case $ENV in
    termux)
        pkg update -y || true
        pkg upgrade -y || true
        # Core tools & compile tools
        $INSTALL_CMD python python-pip git curl wget
        $INSTALL_CMD rust openssl libffi clang make binutils
        $INSTALL_CMD resolv-conf
        ;;
    debian)
        $SUDO apt update -y || true
        $INSTALL_CMD python3 python3-pip python3-venv git curl wget
        $INSTALL_CMD build-essential libssl-dev libffi-dev python3-dev cargo
        ;;
    arch)
        $SUDO pacman -Sy --noconfirm
        $INSTALL_CMD python python-pip git curl wget
        $INSTALL_CMD base-devel openssl rust
        ;;
    fedora)
        $INSTALL_CMD python3 python3-pip git curl wget
        $INSTALL_CMD gcc openssl-devel libffi-devel python3-devel cargo
        ;;
    alpine)
        $INSTALL_CMD python3 py3-pip git curl wget
        $INSTALL_CMD gcc musl-dev libffi-dev openssl-dev rust cargo
        ;;
esac

echo -e "${GREEN}[OK]${NC} Sistem dependensi terinstall."

# ============ 3. UPGRADE PIP & INSTALL PYTHON LIBRARY ============
echo -e "\n${CYAN}[INFO]${NC} Upgrade pip & install library Python..."
python3 -m pip install --upgrade pip setuptools wheel 2>/dev/null || pip install --upgrade pip setuptools wheel

# List library utama
PY_LIBS=(
    "rich"
    "requests"
    "httpx[http2]"
    "dnspython"
    "tldextract"
    "python-dotenv"
)

for lib in "${PY_LIBS[@]}"; do
    echo -e "  ${CYAN}->${NC} Installing $lib..."
    pip install "$lib" || python3 -m pip install "$lib"
done

# ============ 4. INSTALL GEMINI AI (OPSIONAL) ============
echo -e "\n${CYAN}[INFO]${NC} Install Gemini AI (opsional)..."
pip install google-genai || python3 -m pip install google-genai || echo -e "${YELLOW}[WARN]${NC} Gemini AI gagal di-install (bisa di-skip)"

# ============ 5. SETUP .env ============
if [ ! -f ".env" ]; then
    echo -e "\n${CYAN}[INFO]${NC} Membuat file .env..."
    cat > .env << 'ENVEOF'
# Gemini API Key (Optional)
# Daftar gratis: https://aistudio.google.com/apikey
GEMINI_API_KEY=
ENVEOF
    echo -e "${GREEN}[OK]${NC} File .env berhasil dibuat."
fi

# ============ 6. VERIFIKASI AKHIR ============
echo -e "\n${CYAN}[INFO]${NC} Verifikasi instalasi..."
python3 -c "
import sys
try:
    import rich, requests, httpx, dns, tldextract, dotenv
    print('\033[0;32m[OK]\033[0m Semua dependency utama berhasil di-import!')
except ImportError as e:
    print(f'\033[0;31m[ERR]\033[0m Gagal import: {e}')
    sys.exit(1)
" || exit 1

echo -e "\n${GREEN}"
echo "╔══════════════════════════════════════════╗"
echo "║      INSTALASI SELESAI 100%!             ║"
echo "╚══════════════════════════════════════════╝"
echo -e "${NC}"
echo -e "${GREEN}[OK]${NC} Jalankan tools: ${CYAN}python3 main.py${NC}"
echo -e "${GREEN}[OK]${NC} Setup API Key : ${CYAN}nano .env${NC}"
echo ""
