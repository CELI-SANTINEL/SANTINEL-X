<div align="center">

#SANTINEL-X (CLOUDFALL-V2)
### *Advanced Web Reconnaissance & Vulnerability Scanner*

[![Version](https://img.shields.io/badge/version-9.5-blue?style=for-the-badge&logo=python)](https://github.com/username/KID-NUCLEI)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](https://github.com/username/KID-NUCLEI/blob/main/LICENSE)
[![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Kali%20Linux-red?style=for-the-badge)](https://github.com/username/KID-NUCLEI)
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow?style=for-the-badge&logo=python)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/username/KID-NUCLEI/pulls)

<img src='https://cdn.phototourl.com/member/2026-10-19-bbfc7b45-7275-4399-9340-5aab938e99db.jpg'/>

**All-in-One Automated Security Audit Framework.**

[Fitur](#-fitur-utama) • [Instalasi](#-instalasi) • [Cara Pakai](#-cara-pakai) • [ Struktur](#-struktur-direktori) • [FAQ](#-faq--troubleshooting) • [Disclaimer](#️-legal-disclaime)

</div>

---

## Tentang Project

**SANTINEL-X** adalah framework keamanan web berbasis Python yang dirancang untuk berjalan di **Termux (Android)**, **Kali NetHunter**, maupun **Linux Desktop**. Tools ini menggabungkan *Reconnaissance*, *Vulnerability Scanning*, dan *AI Analysis* ke dalam satu antarmuka terminal (TUI) yang modern, cepat, dan ringan.

Dirancang khusus untuk *bug bounty hunter*, *penetration tester*, dan *security researcher* yang membutuhkan alat audit cepat tanpa membebani resource perangkat.

---

## Fitur Utama

### 1. Reconnaissance (Recon)
- **DNS & Subdomain Scanner** — Multi-nameserver fallback (8.8.8.8, 1.1.1.1, dll).
- **Port Scanner** — Klasifikasi 4-status: `OPEN`, `CLOSED`, `FILTERED`, `UNREACHABLE`.
- **Security Headers** — Deteksi 11+ header (HSTS, CSP, X-Frame-Options, dll).
- **WAF Detection** — Fingerprint Cloudflare, AWS, Akamai, Fastly, Imperva.
- **CMS Detection** — Identifikasi WordPress, Joomla, Drupal, dll.

### 2. Vulnerability Scanner
| Modul | Payload | Deskripsi |
|-------|---------|-----------|
| **XSS** | 60+ | Reflected, DOM, Context Breaking, WAF Bypass |
| **SQL Injection** | 60+ | Error-based, Time-based, Boolean, Union |
| **SSRF** | 48 | Internal IP, Cloud Metadata, File Protocol |
| **IDOR** | 30+ | Parameter Enumeration (User, Order, Invoice) |
| **Open Redirect** | 37 | Protocol-relative, Encoded, Backslash |
| **LFI** | 45+ | Sensitive Path (`.env`, `.git`, Backup, Config) |

### 3. CVE Database
- **278 CVE templates** tervalidasi dari **NVD**.
- **Passive Matching** — Cocokkan versi server (Apache, Nginx, WordPress).
- **Confidence Scoring** — Jujur soal keterbatasan data.

### 4. AI Analysis
- **Gemini AI** — Analisis mendalam (optional).
- **Local Backend** — Rule-based fallback (100% offline).

### 5. Modern TUI (Terminal UI)
- **Rich Table** — Output rapi, berwarna, dan profesional.
- **Progress Bar** — Real-time scanning progress.
- **Tag Info** — Menggunakan tag `[INFO]`, `[VULN]`, `[ERR]`, `[WARN]`.

---

## Instalasi

### Prasyarat
- Python 3.10+
- Git & Pip

### 1. Clone Repository
```
git clone https://github.com/username/KID-NUCLEI.git
cd KID-NUCLEI
pip3 install -r requirements.txt
bash install.sh
python3 main.py
