# Smart Waste Management System

An intelligent IoT solution that automates waste classification, tracking, and analysis using AI-powered computer vision, cloud connectivity, and real-time data visualization.

**Group:** Clowns  
**Course:** Multi-Discipline Project  
**Institution:** Vietnamese-German University (VGU)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Configuration](#configuration)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [Troubleshooting](#troubleshooting)

---

## Project Overview

The **Smart Waste Management System** integrates multiple technologies to provide an end-to-end solution for waste monitoring. It captures waste items via a webcam, uses machine learning to classify them into 5 categories, stores the data in a database, and visualizes trends through an interactive web dashboard. A chatbot assistant helps users understand waste classification and system features.

### Problem Statement
Traditional waste management lacks real-time tracking and classification, making it difficult for users to monitor their waste generation patterns and make informed decisions about recycling and disposal.

### Solution
This system automates waste detection and provides instant feedback through a web-based dashboard, enabling users to track daily and weekly waste statistics, understand disposal habits, and improve their waste management practices.

---

## Key Features

✨ **AI-Powered Waste Detection**
- Real-time classification of 5 waste types: Glass, Paper, Organic, Plastic, and Metal
- Custom-trained Keras deep learning model
- Confidence scoring for detection accuracy

📡 **IoT Cloud Integration**
- MQTT protocol for reliable data transmission
- Adafruit IO for cloud storage and real-time data streaming
- Bi-directional communication between hardware and dashboard

📊 **Data Analytics & Tracking**
- Automatic daily waste totals and weekly statistics
- Historical data storage in Microsoft Access database
- Trend analysis across time periods

🎨 **Interactive Web Dashboard**
- Real-time visualization with dynamic charts (Bar, Pie, Line graphs)
- Daily and weekly waste tracking pages
- Responsive design for desktop and tablet access

💬 **Intelligent Chatbot**
- FAQ assistance for waste classification
- System usage guidance
- User-friendly interface embedded in the dashboard

---

## System Architecture

```
┌─────────────────┐
│   AI Camera     │  ─ Captures video
│ (OpenCV/Keras)  │  ─ Classifies waste
└────────┬────────┘
         │ (Publishes labels)
         ↓
┌─────────────────────┐
│ Adafruit IO (Cloud) │
└────┬────────────────┘
     │ (MQTT protocol)
     ↓
┌──────────────────┐
│  MQTT Listener   │  ─ Receives classifications
│   (mqtt.py)      │  ─ Calculates statistics
└────────┬─────────┘  ─ Updates database
         │
         ↓
┌──────────────────────┐
│  MS Access Database  │  ─ Stores historical data
│ (WasteManagement.    │  ─ Waste_Tracking table
│   accdb)             │  ─ Daily/Weekly summaries
└──────────────────────┘
         ↑
         │ (API calls)
         ↓
┌──────────────────────┐
│  Web Dashboard       │  ─ Real-time statistics
│ (HTML/CSS/JS)        │  ─ Chart visualizations
│ + Chatbot            │  ─ User interaction
└──────────────────────┘
```

---

## Tech Stack

| Layer         | Technologies                                  |
|---------------|-----------------------------------------------|
| **AI/ML**     | TensorFlow, Keras, Teachable Machine, OpenCV  |
| **IoT**       | MQTT Protocol, Adafruit IO                    |
| **Backend**   | Python 3.x, PyODBC, NumPy, Statistics         |
| **Database**  | Microsoft Access (.accdb)                     |
| **Frontend**  | HTML5, CSS3, JavaScript, Chart.js             |

---

## Prerequisites

### Hardware
- PC or Laptop with a built-in or external webcam
- Stable internet connection (for MQTT and Adafruit IO)
- At least 2GB RAM, 500MB disk space

### Software
- **Python 3.7+** (download from [python.org](https://www.python.org/downloads/))
- **Microsoft Access Database Driver** (Windows native or download separately)
- Modern web browser (Chrome, Firefox, Edge)

### Accounts
- **Adafruit IO Account** (free tier available at [io.adafruit.com](https://io.adafruit.com))
  - Used for cloud data storage and real-time feed updates

---

## Installation Guide

### Step 1: Clone the Project

### Step 2: Install Python Dependencies

```bash
pip install opencv-python tensorflow keras adafruit-io pyodbc pillow
```


### Step 3: Set Up the Database

1. Open the provided `WasteManagement.accdb` file in Microsoft Access
2. Verify the following tables exist:
   - `Waste_Tracking` - stores individual waste classifications
   - `Daily_Bin_Tracking` - daily aggregated data
   - `Weekly_Tracking` - weekly summaries

3. Note the full path to your database file (e.g., `C:\Path\To\WasteManagement.accdb`)


---

## Configuration

### Step 1: Set Up Adafruit IO

1. Create a free account at [io.adafruit.com](https://io.adafruit.com)
2. Create a new dashboard
3. Create the following **Feeds** (case-sensitive):
   - `ai_camera` - receives real-time classifications
   - `daily_tracking` - stores daily totals
   - `total_week` - weekly total waste
   - `glass_week`, `paper_week`, `metal_week`, `organic_week`, `plastic_week` - weekly breakdown by type

4. Note your Adafruit IO:
   - **Username** (visible in account settings)
   - **Active Key** (AIO Key - keep this private)

### Step 2: Update Python Configuration

Open `AI camera/AI_camera.py` and `Data Analysis Model/mqtt.py`:

```python
# Adafruit IO Credentials
AIO_USERNAME = "YOUR_ADAFRUIT_USERNAME"
AIO_KEY = "YOUR_ADAFRUIT_KEY"

# Database Connection String (update path to your database)
CONNECTION_STRING = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Path\To\WasteManagement.accdb;'
```

### Step 3: Update Website Configuration

Open `Website Model/js/daily_waste_tracking.js` and `Website Model/js/weekly_waste_tracking.js`:

```javascript
// Replace with your Adafruit IO credentials
const AIO_USERNAME = "YOUR_ADAFRUIT_USERNAME";
const AIO_KEY = "YOUR_ADAFRUIT_KEY";
const API_URL = "https://io.adafruit.com/api/v2/" + AIO_USERNAME + "/feeds/";
```

### Step 4: Configure Chatbot (Optional)

If using the Rasa chatbot component in `Chatbot_Model/`:

1. Update `Chatbot_Model/credentials.yml` with your credentials
2. Update `Chatbot_Model/endpoints.yml` with correct API endpoints

---

## Getting Started

### Quick Start (4 Steps)

**Step 1: Start the Backend Server**

Open a terminal and run:

```bash
cd ~/Data Analysis Model
python mqtt.py
```

You should see output indicating the MQTT listener is running and waiting for data.

**Step 2: Start the AI Camera**

Open a new terminal and run:

```bash
cd ~/AI camera
python AI_camera.py
```

The webcam window will open. Point it at objects you want to classify. The terminal will display:
- **Class**: The detected waste type
- **Confidence**: How confident the model is in its prediction

**Step 3: Run the Chatbot Module**

To enable the chatbot feature on the website, start the Rasa chatbot server as follows:

1. Open a new terminal and navigate to Chatbot_Model folder:

   ```bash
   cd ~/Chatbot_Model
   ```
2. Run the following command to train and save the chatbot model:
   ```bash
   rasa train
   ```
3. After training completes, start the Rasa server with API and CORS enabled:
   ```bash
   rasa run --enable-api --cors="*"
   ```
4. Once the server is running, go to the homepage of the website and chat with the chatbot.

**Step 4: View the Dashboard**

1. Open `Website Model\index.html` in your web browser
2. Navigate through the pages:
   - **Home** - Overview and chatbot
   - **Daily Waste Tracking** - Real-time bin levels and daily statistics
   - **Weekly Waste Tracking** - Historical trends and weekly breakdowns

---

## Usage Guide

### AI Camera Operation

The camera module continuously classifies waste in real-time:

1. **Pointing the Camera**: Face the webcam toward the waste item
2. **Reading Output**: Terminal shows detected class and confidence percentage
3. **Confidence Threshold**: Classifications above 70% confidence are published to Adafruit IO
4. **Stopping**: Press `Q` or `Esc` to quit the application

### Dashboard Navigation

**Daily Waste Tracking Page**
- Shows current bin fill levels
- Displays today's waste breakdown by type
- Updates in real-time as camera detects items

**Weekly Waste Tracking Page**
- Line graph showing daily totals over the past week
- Pie chart showing waste distribution by type
- Average daily and weekly statistics

### Chatbot Interaction

Click the chatbot icon on the homepage to:
- Ask about waste classification guidelines
- Get system usage instructions
- Learn about recycling best practices

---

## Troubleshooting

### Camera Not Detected
- Ensure your webcam is connected and working (test with Photo app)
- Check if another application is using the camera
- Verify camera drivers are up-to-date

### MQTT Connection Failed
- Verify your Adafruit IO username and key are correct
- Check your internet connection
- Ensure Adafruit IO service is online (check status.adafruit.com)

### Database Connection Error
- Verify the database path in `mqtt.py` is correct
- Ensure Microsoft Access Database Driver is installed on Windows
- Check that `WasteManagement.accdb` file is not locked by another application

### Dashboard Not Updating
- Verify JavaScript credentials match Adafruit IO username and key
- Open browser Developer Tools (F12) to check for JavaScript errors
- Check the browser console for API error messages
- Ensure the camera and MQTT listener are running

### Model Accuracy Issues
- Clean the camera lens
- Ensure adequate lighting on the waste item
- The model is trained for 5 categories; unrecognized items may show low confidence
- For improved accuracy, retrain the model with additional data using Teachable Machine

---

## Project Team

**Group Name:** Clowns  
**Course:** Multi-Discipline Project  
**Semester:** Year 1  
**Institution:** Vietnamese-German University (VGU)
