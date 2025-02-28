# Network Traffic Analysis Tool

## 📌 Overview
This tool captures and analyzes **real-time network traffic** to help users monitor, visualize, and detect potential security threats. It uses **Scapy** for packet sniffing and **Plotly/Dash** for interactive visualization.

## 🔧 Features
- **Real-time Packet Sniffing**: Captures live network packets.
- **Protocol Analysis**: Displays TCP, UDP, ICMP traffic distribution.
- **Source & Destination Tracking**: Monitors communication between IPs.
- **Live Data Visualization**: Updates graphs dynamically with incoming packets.
- **Filtering Options**: Allows filtering based on protocol/IP.

## 📂 Project Structure
```
network_traffic_analysis/
│── sniffing/
│   ├── __init__.py
│   ├── packet_sniffer.py   # Captures network packets
│
│── visualization/
│   ├── __init__.py
│   ├── plot_traffic.py     # Handles real-time data visualization
│
│── main.py                 # Entry point to run the tool
│── requirements.txt         # Dependencies (Scapy, Plotly, Pandas, Dash, etc.)
│── README.md               # Documentation
```

## 🛠️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/network_traffic_analysis.git
cd network_traffic_analysis
```
### 2️⃣ Install Dependencies
Make sure you have **Python 3.8+** installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Tool
```bash
python main.py
```
This will start the packet sniffing process and launch the **interactive visualization** in your browser.

## 📊 How It Works
1. **Packet Sniffing**
   - The tool captures **live network packets**.
   - Extracts **source IP, destination IP, and protocol**.
2. **Visualization**
   - The data is plotted in **real-time**.
   - Displays graphs for **protocol distribution**, **top IPs**, etc.

## 🔍 Customization
- Modify `packet_sniffer.py` to change **filtering rules** (e.g., capture only TCP packets).
- Adjust `plot_traffic.py` to **customize graphs**.

## 🛠️ Troubleshooting
- **No packets captured?** Run with **administrator privileges**:
  ```bash
  sudo python main.py   # (Linux/Mac)
  python main.py        # (Windows, run as Admin)
  ```
- **Visualization not appearing?** Ensure **Dash** is installed:
  ```bash
  pip install dash
  ```

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Feel free to **fork the repo** and submit **pull requests** for improvements!

## 🚀 Future Enhancements
- **GeoIP Mapping** to visualize external connections.
- **Bandwidth Monitoring**.
- **Intrusion Detection System (IDS)** integration.

---
### 📨 Contact
For questions, open an **issue** or contact me at `your-email@example.com`.

Happy Sniffing! 🕵️‍♂️

