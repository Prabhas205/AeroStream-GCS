# AeroStream GCS // Tactical Mission Control Dashboard

A high-performance, full-stack Ground Control Station (GCS) designed for real-time UAV telemetry visualization. This project bridges the gap between low-level flight protocols (MAVLink) and modern web-based interfaces.



## 🚀 Overview
AeroStream GCS is a mission-critical tool built to monitor UAV flight parameters during SITL (Software-In-The-Loop) testing. It utilizes an asynchronous architecture to handle high-frequency telemetry data with sub-second latency.

## 🛠 Tech Stack
- **Frontend:** React.js, Tailwind CSS (Tactical High-Contrast UI)
- **Backend:** Python 3.10+, FastAPI (Asynchronous Event Loop)
- **Communication:** WebSockets (Real-time streaming), MAVLink (Protocol)
- **Simulation:** ArduPilot SITL / MAVProxy

## 🏗 System Architecture
1. **Data Layer:** ArduPilot SITL generates MAVLink packets over UDP port 14550.
2. **Bridge Layer:** A Python/FastAPI backend acts as a middleware, decoding MAVLink packets via `pymavlink`.
3. **Transport Layer:** Decoded JSON data is broadcasted to the frontend via a persistent WebSocket connection.
4. **Presentation Layer:** A responsive React dashboard visualizes Altitude, Airspeed, GPS, and Battery status in real-time.



## 🔧 Installation & Setup

### 1. Prerequisites
- Node.js & npm
- Python 3.10+
- ArduPilot SITL / MAVProxy

### 2. Backend Setup
cd backend
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py

#### 2. Frontend Setup
cd frontend
npm install
npm start

#### 3.Simulation

Ensure your SITL instance is broadcasting to 127.0.0.1:14550 (UDP).

### 📡 Key Features
Low-Latency Telemetry: Sub-200ms delay from simulator to UI.

Responsive Design: Optimized for field tablets and command center monitors.

Asynchronous Processing: Non-blocking I/O ensures the UI remains responsive during high-bandwidth data bursts.


