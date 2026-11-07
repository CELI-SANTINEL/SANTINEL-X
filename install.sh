#!/usr/bin/env bash
# KID NUCLEI - ULTIMATE INSTALLER v2.2 (Force Detect)

set -e

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════╗"
echo "║   KID NUCLEI - ULTIMATE INSTALLER v2.2   ║"
echo "╚══════════════════════════════════════════╝"
echo -e "${NC}"

# ============ DETEKSI OS (PRIORITAS apt DULU) ============
if command -v apt &>/dev/null; then
    ENV="debian"; PKG="apt"; INSTALL_CMD="apt install -y"
    if [ "$EUID" -ne 0 ]; then SUDO="sudo"; INSTALL_CMD="sudo apt install -y"; fi
elif command -v pkg &>/dev/null; then
    ENV="termux"; PKG="pkg"; INSTALL_CMD="pkg install -y"; SUDO=""
elif command -v pacman &>/dev/null; then
    ENV="arch"; PKG="pacman"; [ "$EUID" -ne 0 ] && SUDO="sudo"; INSTALL_CMD="$SUDO pacman -S --noconfirm"
elif command -v dnf &>/dev/null; then
    ENV="fedora"; PKG="dnf"; [ "$EUID" -ne 0 ] && SUDO="sudo"; INSTALL_CMD="$SUDO dnf install -y"
else
    echo -e "${RED}[ERR]${NC} OS tidak dikenali"
    exit 1
fi

echo -e "${GREEN}[OK]${NC} OS: ${CYAN}$ENV${NC} | Pkg: ${CYAN}$PKG${NC}"

# ============ INSTALL SISTEM DEPENDENSI ============
case $ENV in
    debian)
        $SUDO apt update -y || true
        $INSTALL_CMD python3 python3-pip python3-venv git curl wget build-essential libssl-dev libffi-dev python3-dev
        ;;
    termux)
        pkg update -y || true
        pkg upgrade -y || true
        $INSTALL_CMD python python-pip git curl wget rust openssl libffi clang make binutils
        ;;
    arch)
        $SUDO pacman -Sy --noconfirm
        $INSTALL_CMD python python-pip git curl wget base-devel openssl rust
        ;;
    fedora)
        $INSTALL_CMD python3 python3-pip git curl wget gcc openssl-devel libffi-devel python3-devel
        ;;
esac

echo -e "${GREEN}[OK]${NC} Sistem dependensi terinstall."

# ============ INSTALL PYTHON DEPS ============
echo -e "\n${CYAN}[INFO]${NC} Install library Python..."
pip install --upgrade pip setuptools wheel

PY_LIBS=("rich" "requests" "httpx[http2]" "dnspython" "tldextract" "python-dotenv")
for lib in "${PY_LIBS[@]}"; do
    echo -e "  ${CYAN}->${NC} Installing $lib..."
    pip install "$lib" || true
done

# ============ GEMINI AI ============
echo -e "\n${CYAN}[INFO]${NC} Install Gemini AI (opsional)..."
pip install google-genai 2>/dev/null && echo -e "${GREEN}[OK]${NC} Gemini installed" || echo -e "${YELLOW}[WARN]${NC} Gemini skip"

# ============ SETUP .env ============
if [ ! -f ".env" ]; then
    cat > .env << 'ENVEOF'
GEMINI_API_KEY=
ENVEOF
    echo -e "${GREEN}[OK]${NC} .env dibuat"
fi

# ============ VERIFIKASI ============
echo -e "\n${CYAN}[INFO]${NC} Verifikasi instalasi..."
python3 -c "import rich, requests, httpx, dns, tldextract, dotenv; print('✅ Semua dependency OK!')" || echo -e "${RED}[ERR]${NC} Ada yang gagal"

echo -e "\n${GREEN}"
echo "╔══════════════════════════════════════════╗"
echo "║      INSTALASI SELESAI 100%!             ║"
echo "╚══════════════════════════════════════════╝"
echo -e "${NC}"
echo -e "${GREEN}[OK]${NC} Jalankan: ${CYAN}python3 main.py${NC}"
