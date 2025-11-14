<p align="center">
  <img src="https://img.shields.io/badge/Project-NetProbe-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Type-Red%20Team%20Tool-red?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/your-username/NetProbe/main/assets/logo.png" width="160" />
</p>

<h1 align="center">⚡ NetProbe</h1>
<p align="center">A lightweight offensive security dashboard for controlled attack simulations.</p>

<hr>

<h2>🎬 Demo (GIF)</h2>
<p align="center">
  <img src="https://raw.githubusercontent.com/your-username/NetProbe/main/assets/demo.gif" width="700" />
</p>

<hr>

<h2>🔥 Overview (English)</h2>

<p><strong>NetProbe</strong> is a lightweight, web-based offensive security toolkit designed for:</p>

<ul>
  <li>🛡️ <strong>Red team training</strong></li>
  <li>🎓 <strong>Cybersecurity education</strong></li>
  <li>🧪 <strong>Authorized penetration testing labs</strong></li>
</ul>

<p>It supports the following attack modules:</p>

<ul>
  <li>🔥 <strong>SYN Flood</strong></li>
  <li>⚡ <strong>TCP Flood</strong></li>
  <li>🌐 <strong>HTTP Stress Test</strong></li>
  <li>🔍 <strong>Port Scanning</strong></li>
</ul>

<p><strong>⚠️ Legal Warning:</strong> Use only in controlled and authorized environments. Unauthorized use is illegal.</p>

<hr>

<h2>🧩 Features</h2>

<table>
  <tr>
    <th>Attack Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>🔥 <strong>SYN Flood</strong></td>
    <td>Overwhelms the target with half‑open TCP handshake packets.</td>
  </tr>
  <tr>
    <td>⚡ <strong>TCP Flood</strong></td>
    <td>Creates raw TCP connections to exhaust system resources.</td>
  </tr>
  <tr>
    <td>🌐 <strong>HTTP Stress Test</strong></td>
    <td>Generates multi-threaded intense HTTP requests.</td>
  </tr>
  <tr>
    <td>🔍 <strong>Port Scan</strong></td>
    <td>Identifies open ports on a target host.</td>
  </tr>
</table>

<hr>

<h2>🔌 API Endpoints</h2>

<table>
  <tr>
    <th>Method</th>
    <th>Endpoint</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>POST</code></td>
    <td>/syn-flood</td>
    <td>Starts a SYN Flood attack.</td>
  </tr>
  <tr>
    <td><code>POST</code></td>
    <td>/tcp-flood</td>
    <td>Starts a TCP Flood attack.</td>
  </tr>
  <tr>
    <td><code>POST</code></td>
    <td>/http-stress</td>
    <td>Launches an HTTP stress test.</td>
  </tr>
  <tr>
    <td><code>POST</code></td>
    <td>/port-scan</td>
    <td>Executes a port scan.</td>
  </tr>
  <tr>
    <td><code>GET</code></td>
    <td>/health</td>
    <td>Backend health check.</td>
  </tr>
</table>

<hr>

<h2>📁 Project Structure</h2>

<pre>
/project
  /backend
    main.py
    Dockerfile
  /frontend
    index.html
    style.css
    app.js
  /assets
    logo.png
    demo.gif
  docker-compose.yml
  README.md
</pre>

<hr>

<h2>🛠️ Technologies Used</h2>

<h3>Backend</h3>
<ul>
  <li>🟦 Python 3</li>
  <li>⚡ FastAPI</li>
  <li>🚀 Uvicorn</li>
  <li>🐳 Docker & Docker Compose</li>
</ul>

<h3>Frontend</h3>
<ul>
  <li>🎨 HTML5, CSS3</li>
  <li>🟨 Vanilla JavaScript</li>
  <li>🔗 Fetch API</li>
</ul>

<hr>

<h2>▶️ Running the Project</h2>

<h3>1️⃣ Build & Run with Docker</h3>
<pre>
docker-compose up --build
</pre>

<h3>2️⃣ Access Points</h3>
<ul>
  <li><strong>Backend (API):</strong> http://localhost:8000</li>
  <li><strong>Frontend:</strong> Open <code>/frontend/index.html</code> in your browser</li>
</ul>

<hr>

<h2>⚠️ Legal Disclaimer</h2>

<p>This tool is intended strictly for educational, authorized, and ethical use.</p>
<p>Unauthorized usage is illegal and the user accepts full responsibility.</p>

<hr>

<h2>🇹🇷 Türkçe Açıklama</h2>

<h3>🔥 Genel Bakış</h3>

<p><strong>NetProbe</strong>, web tabanlı bir saldırı simülasyon aracıdır. Aşağıdaki amaçlar için geliştirilmiştir:</p>

<ul>
  <li>🛡️ Red team çalışmaları</li>
  <li>🎓 Siber güvenlik eğitimi</li>
  <li>🧪 Yetkili laboratuvar testleri</li>
</ul>

<p>Desteklenen saldırı türleri:</p>

<ul>
  <li>🔥 SYN Flood</li>
  <li>⚡ TCP Flood</li>
  <li>🌐 HTTP Yoğunluk Testi</li>
  <li>🔍 Port Tarama</li>
</ul>

<hr>

<h3>🧩 Özellikler</h3>

<table>
  <tr>
    <th>Saldırı Türü</th>
    <th>Açıklama</th>
  </tr>
  <tr>
    <td>🔥 <strong>SYN Flood</strong></td>
    <td>Hedef sistemi yarı açık TCP istekleriyle doldurur.</td>
  </tr>
  <tr>
    <td>⚡ <strong>TCP Flood</strong></td>
    <td>Ham TCP bağlantıları oluşturarak aşırı yük bindirir.</td>
  </tr>
  <tr>
    <td>🌐 <strong>HTTP Yoğunluk Testi</strong></td>
    <td>Çoklu thread ile yoğun HTTP istekleri gönderir.</td>
  </tr>
  <tr>
    <td>🔍 <strong>Port Tarama</strong></td>
    <td>Açık portları hızlıca tespit eder.</td>
  </tr>
</table>

<hr>

<h2>🎯 Son</h2>
<p align="center">⭐ If you like this project, consider giving it a star! ⭐</p>
