<p align="center">
  <img src="https://img.shields.io/badge/Project-NetProbe-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Type-Red%20Team%20Tool-red?style=for-the-badge" />
</p>

<h1 align="center">⚡ NetProbe</h1>
<p align="center">A lightweight offensive security dashboard for controlled attack simulations.</p>

---

# 🔥 Overview (English)

**NetProbe** is a web-based offensive security toolkit built for **red team training**, **cybersecurity education**, and **authorized penetration testing labs**.

It provides a clean dashboard to simulate common network attack types such as:

- 🔸 **SYN Flood**
- 🔸 **TCP Flood**
- 🔸 **HTTP Stress Test**
- 🔸 **Port Scanning**

> ⚠️ **Warning** > This project is strictly for **legal and authorized testing** in controlled environments.  
> Misuse of these attack techniques may be illegal.

---

# 🧩 Features

### 🛡️ Attack Modules

| Attack Type | Description |
|:-----------|:------------|
| 🔥 **SYN Flood** | Sends massive half-open TCP requests to overwhelm a target. |
| ⚡ **TCP Flood** | Raw TCP connection flooding against target ports. |
| 🌐 **HTTP Stress Test** | Multi-thread heavy request generator for load/stress testing. |
| 🔍 **Port Scan** | Scans IP addresses for open ports using ranged or enumerated lists. |

---

# 📁 Project Structure

```bash
/project
  /backend
    main.py
    Dockerfile
  /frontend
    index.html
    style.css
    app.js
  docker-compose.yml
  README.md
🛠️ Technologies UsedBackend🟦 Python 3⚡ FastAPI🚀 Uvicorn🐳 Docker / Docker ComposeFrontend🎨 HTML5, CSS3🟨 Vanilla JavaScript🔗 Fetch API▶️ Running the Project (Optional)If you want to test the project locally:1️⃣ Build & Run (Docker)Bashdocker-compose up --build
Access Points:Backend: http://localhost:8000 (Access the API endpoints)Frontend: Open the file /frontend/index.html manually in your browser.⚠️ Legal Disclaimer (Global)This tool is intended strictly for educational, authorized, and ethical use.Running attack modules on systems without explicit permission is illegal and punishable by law. The user assumes all responsibility.🧑‍💻 AuthorDeveloped as part of a cybersecurity learning & red team practice project.🇹🇷 Türkçe Açıklama🔥 Genel BakışNetProbe, web tabanlı bir saldırı simülasyon aracıdır. Siber güvenlik eğitimleri, red team çalışmaları ve laboratuvar test ortamları için geliştirilmiştir.Simüle edilebilen saldırı türleri:🔸 SYN Flood🔸 TCP Flood🔸 HTTP Yoğunluk Testi🔸 Port Tarama🧩 ÖzelliklerSaldırı TürüAçıklama🔥 SYN FloodHedefi yarı açık TCP istekleriyle doldurur.⚡ TCP FloodHam TCP bağlantıları ile portlara yük bindirir.🌐 HTTP Stress TestÇoklu thread ile yoğun HTTP isteği gönderir.🔍 Port TaramaIP üzerindeki açık portları hızlıca tespit eder.⚠️ Yasal UyarıBu yazılım yalnızca izinli, eğitim amaçlı, laboratuvar ortamı için geliştirilmiştir.İzinsiz saldırı girişimleri yasal suçtur ve ağır cezalara neden olabilir.Sorumluluk tamamen kullanıcıya aittir.<p align="center"> ⭐ If you like this project, consider giving it a star on GitHub! </p>
