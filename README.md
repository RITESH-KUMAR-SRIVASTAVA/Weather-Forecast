# 🌤️ Weather Forecast Desktop Notifier 

A lightweight **Python** script that fetches live weather data for cities using the **Open-Meteo API** and sends a **cross-platform desktop notification** with the current temperature and wind speed.

---

## 📌 Features

* 🌍 Fetches real-time weather data via Open-Meteo API (no API key required)
* 📍 Geocoding: Converts city name to coordinates automatically
* 🔔 Sends desktop notifications with current temperature & wind speed
* 🖥️ Prints weather info to the terminal as fallback
* ✅ Error handling for invalid city or missing weather data

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **APIs:** Open-Meteo (Geocoding + Weather Forecast)
* **Notifications:** plyer (cross-platform desktop notifications)
* **HTTP Client:** requests

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or above
* Internet connection

### Installation

1. Clone the repository

```bash
git clone https://github.com/RITESH-KUMAR-SRIVASTAVA/Weather-Forecast.git
```

2. Navigate to the project directory

```bash
cd Weather-Forecast
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python Weather-Forecast.py
```

---

## 📸 Sample Output

```
Weather: Delhi: 33.3°C, Wind 7.3 km/h
```

A desktop notification will also pop up with the same information.

---

## 📁 Project Structure

```text
Weather-Forecast/
│
├── Weather-Forecast.py   # Main weather script
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 📚 Concepts Demonstrated

* REST API consumption (requests library)
* JSON parsing
* Cross-platform desktop notifications (plyer)
* Error handling
* Geocoding & reverse geocoding

---

## 👨‍💻 Author

**Ritesh Kumar Srivastava**

* GitHub: [@RITESH-KUMAR-SRIVASTAVA](https://github.com/RITESH-KUMAR-SRIVASTAVA)

---

> ⭐ If you found this project useful, consider giving it a star!
