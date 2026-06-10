# Hubble CTF – Capture The Flag Challenge Set

**Based on real vulnerabilities discovered during the black‑box penetration test of Hubble Digital Platform (hubble.sh)**  

![CTF](https://img.shields.io/badge/CTF-8%20challenges-blue) ![Flask](https://img.shields.io/badge/Flask-2.3.3-green) ![Python](https://img.shields.io/badge/Python-3.11%2B-yellow) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview

This repository contains **8 Capture The Flag (CTF) challenges** developed as part of the **Work Integrated Learning (WIL) programme** with the University of Adelaide and Hubble. Each challenge is directly mapped to a **real vulnerability** identified during the external black‑box penetration test conducted in Weeks 4–7.

The CTF set is designed to:
- **Educate** Hubble’s developers and security champions by letting them exploit the exact weaknesses found in their own infrastructure.
- **Demonstrate** practical attack paths for OWASP Top 10, cloud misconfigurations, and supply chain risks.
- **Serve as a reusable training tool** that can be run locally or in a sandbox.

---

## 🧩 Challenge List

| ID | Challenge Name | Difficulty | Vulnerability (Real Finding) |
|----|----------------|------------|------------------------------|
| 1  | **Meteor Leak** | Easy | Exposed API keys in Meteor `__meteor_runtime_config__` (AWS-07) |
| 2  | **No WAF, No Cry** | Medium | Ktor cache leak + Cloudflare WAF bypass (AWS-05) |
| 3  | **Basic Brute** | Medium | HTTP Basic Auth on admin service – no rate limiting, no MFA (AWS-09) |
| 4  | **Splunkd Sneak** | Medium | Exposed Splunkd log aggregation service (AWS-01) |
| 5  | **TLS Time Machine** | Easy | Deprecated TLS 1.0/1.1 and CBC ciphers (AWS-03) |
| 6  | **Email Spoof** | Easy | Missing SPF record and DMARC `p=none` (AWS-08) |
| 7  | **Dependency Confusion** | Hard | No `package-lock.json` integrity → dependency confusion (A08-01) |
| 8  | **Git History Ghost** | Medium | Hard‑coded credentials in git commit history (A07-02) |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- `pip` (Python package manager)
- (Optional) Docker and Docker Compose

### Run with Python (local)

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/hubble-ctf.git
cd hubble-ctf

# Install Flask
pip install flask

# Start the CTF server
python app.py
