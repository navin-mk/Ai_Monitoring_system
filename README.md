# AI-Powered Real-Time System Monitoring Dashboard

## Overview
This project is a full-stack system monitoring platform that tracks system metrics such as CPU, memory, and disk usage in real time. It integrates a machine learning model to predict future CPU utilization and provides intelligent auto-scaling recommendations. The system uses a Flask backend and a React-based frontend for visualization.

## Features
- Real-time monitoring of CPU, memory, and disk usage
- Machine learning-based CPU prediction using historical data
- Auto-scaling recommendation system based on current and predicted metrics
- Interactive React dashboard with charts
- Email alert system for high CPU usage (optional)
- Modular and scalable backend structure

## Tech Stack
- Backend: Flask (Python)
- Frontend: React.js
- Machine Learning: Python (Pandas)
- Visualization: Recharts
- Communication: REST APIs
- System Monitoring: psutil

## System Architecture
Monitor Script → Backend API → ML Prediction → Scaling Logic → React Dashboard

## Project Structure
project/
│
├── backend/
│   ├── app.py
│   ├── autoscale.py
│   ├── email_alert.py
│
├── collector/
│   └── monitor.py
│
├── model/
│   └── predict.py
│
├── frontend/
│
├── data/
│   └── metrics.csv

## Setup Instructions

### Clone the Repository
git clone https://github.com/navin-mk/Ai_Monitoring_system.git
cd Ai_Monitoring_system

### Backend Setup
python -m venv venv
venv\Scripts\activate
pip install flask pandas psutil

### Run Backend
python backend/app.py

### Run Monitoring Script (in new terminal)
python collector/monitor.py

### Frontend Setup
cd frontend
npm install

### Run Frontend
npm start

## Usage
Backend API runs on http://127.0.0.1:5000  
Frontend runs on http://localhost:3000  

The dashboard displays:
- Current system metrics
- Predicted CPU usage
- Scaling recommendations
- Historical charts

## Workflow
1. The monitoring script collects system metrics periodically.
2. Data is sent to the backend.
3. The prediction model forecasts CPU usage.
4. The scaling module determines system action.
5. The frontend dashboard updates with real-time data.

## Future Improvements
- Migration to FastAPI
- Event-driven architecture
- Real-time streaming using WebSockets
- Cloud deployment
- Advanced anomaly detection

## Author
Navin Mahendran
