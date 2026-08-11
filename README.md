# AI-Powered Real-Time System Monitoring Dashboard

## Overview

A full-stack AI-powered system monitoring application that continuously monitors CPU, memory, and disk utilization, predicts CPU usage using machine learning, and provides intelligent auto-scaling recommendations through an interactive React dashboard.

The system collects system metrics using Python and Psutil, stores historical data in CSV format, exposes the data through Flask REST APIs, performs CPU prediction using machine learning, and visualizes the results through an interactive React dashboard.

## Features

- Real-time CPU monitoring
- Real-time memory monitoring
- Real-time disk monitoring
- Historical system metric collection
- CSV-based metric storage
- Machine learning-based CPU prediction
- Intelligent auto-scaling recommendations
- Interactive React dashboard
- Multiple monitoring charts
- CPU prediction visualization
- Scaling recommendation display
- High CPU alert detection
- Email alert system
- Flask REST APIs
- Full-stack Python and React architecture

## Technology Stack

- Backend: Python, Flask
- Frontend: React.js, JavaScript
- Machine Learning: Python, Pandas, Scikit-learn
- System Monitoring: Psutil
- Visualization: Recharts
- API Communication: REST APIs
- Data Storage: CSV
- Tools: Git, GitHub, VS Code

## Architecture

System Resources
       |
       v
collector/monitor.py
       |
       v
data/metrics.csv
       |
       v
Flask Backend
       |
       +------------------+
       |                  |
       v                  v
ML Prediction      Scaling Decision
       |                  |
       +--------+---------+
                |
                v
           REST APIs
                |
                v
        React Dashboard
                |
       +--------+--------+
       |        |        |
       v        v        v
    Metrics   Charts   Alerts

## Prerequisites

Install the following:

- Python 3
- npm
- Git

Check the installations:

python --version
npm --version
git --version

## Clone the Repository

git clone https://github.com/navin-mk/Ai_Monitoring_system.git
cd AI-Monitoring-Project

## Backend Setup

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

After activation, the terminal should show:

(venv)

If PowerShell blocks activation:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

Then:

venv\Scripts\activate

## Install Backend Dependencies

Install dependencies using requirements.txt:

pip install -r requirements.txt

If requirements.txt is not available:

pip install flask pandas scikit-learn psutil

## requirements.txt

Flask
pandas
scikit-learn
psutil

## Run the Project

The project requires three terminals.

### Terminal 1 - Start System Monitor

Open a terminal from the project root:

cd E:\AI-Monitoring-Project
venv\Scripts\activate
python collector\monitor.py

The monitor collects:

- CPU usage
- Memory usage
- Disk usage

The data is stored in:

data/metrics.csv

Example output:

CPU: 35.4% | Memory: 62.1% | Disk: 71.3%
CPU: 41.2% | Memory: 62.5% | Disk: 71.3%
CPU: 38.7% | Memory: 63.0% | Disk: 71.3%

Keep this terminal running.

### Terminal 2 - Start Flask Backend

Open a second terminal:

cd E:\AI-Monitoring-Project
venv\Scripts\activate
python backend\app.py

The Flask backend runs at:

http://127.0.0.1:5000

Do not use Uvicorn because this project uses Flask, not FastAPI.

Keep this terminal running.

### Terminal 3 - Start React Frontend

Open a third terminal:

cd E:\AI-Monitoring-Project\frontend
npm install
npm start

The React dashboard runs at:

http://localhost:3000

Open http://localhost:3000 in your browser.

## Complete Run Commands

Terminal 1:

cd E:\AI-Monitoring-Project
venv\Scripts\activate
python collector\monitor.py

Terminal 2:

cd E:\AI-Monitoring-Project
venv\Scripts\activate
python backend\app.py

Terminal 3:

cd E:\AI-Monitoring-Project\frontend
npm start

Then open:

http://localhost:3000

## Flask API Endpoints

### Home

GET /

URL:

http://127.0.0.1:5000/

Returns:

AI Monitoring Backend Running

### Latest Metrics

GET /metrics

URL:

http://127.0.0.1:5000/metrics

Returns the latest CPU, memory, and disk metrics.

### Historical Metrics

GET /history

URL:

http://127.0.0.1:5000/history

Returns historical monitoring data used by the dashboard charts.

### CPU Prediction

GET /predict

URL:

http://127.0.0.1:5000/predict

Returns the predicted CPU utilization, alert status, and scaling recommendation.

Example response:

{
    "predicted_cpu": 82.45,
    "alert": "High CPU usage expected!",
    "scaling": "Scale UP resources"
}

## Machine Learning

The prediction module uses historical CPU utilization data to generate a CPU usage prediction.

Prediction flow:

Historical CPU Metrics
        |
        v
Data Processing
        |
        v
Machine Learning Model
        |
        v
Predicted CPU Usage
        |
        v
Scaling Decision

## Auto-Scaling Recommendation

The project provides intelligent scaling recommendations based on CPU utilization.

The current implementation provides recommendations only. It does not automatically create or terminate cloud resources.

Decision logic:

Predicted CPU > 80%
        |
        v
Scale UP Resources

Predicted CPU < 20%
        |
        v
Scale DOWN Resources

20% - 80%
        |
        v
No Scaling Needed

## Email Alerts

When predicted CPU usage crosses the configured high-CPU threshold, the system can trigger an email alert.

Example:

High CPU predicted: 85.7%

Do not store email passwords, Gmail App Passwords, API keys, or other credentials directly in the source code.

Use environment variables for sensitive information.

Example:

EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
RECEIVER_EMAIL=receiver@gmail.com

## Environment Variables

If email alerts are enabled, create a .env file in the project root.

Example:

EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
RECEIVER_EMAIL=receiver@gmail.com

Never upload .env to GitHub.

## .gitignore

Create a .gitignore file in the project root:

venv/
__pycache__/
*.pyc
.env
node_modules/

## Application Flow

1. monitor.py collects CPU, memory, and disk metrics.
2. The collected metrics are stored in data/metrics.csv.
3. The Flask backend reads the monitoring data.
4. The REST APIs provide current and historical metrics.
5. The machine learning module predicts CPU utilization.
6. The auto-scaling module generates a scaling recommendation.
7. The React frontend requests the data from the Flask backend.
8. The dashboard displays metrics, charts, predictions, scaling recommendations, and alerts.

## Dashboard

The dashboard displays:

- Current CPU usage
- Current memory usage
- Current disk usage
- Predicted CPU usage
- Scaling recommendation
- CPU history chart
- Memory history chart
- Disk history chart
- Alert information

## GitHub Setup

Initialize Git:

git init

Check the files:

git status

Add all files:

git add .

Commit the project:

git commit -m "Initial commit"

Connect the GitHub repository:

git remote add origin <YOUR_GITHUB_REPOSITORY_URL>

Set the main branch:

git branch -M main

Push the project:

git push -u origin main

## Updating the Repository

After making changes:

git add .
git commit -m "Update monitoring dashboard"
git push

## Troubleshooting

### Python module not found

Activate the virtual environment:

venv\Scripts\activate

Then install dependencies:

pip install -r requirements.txt

### Flask not found

pip install flask

### Pandas not found

pip install pandas

### Scikit-learn not found

pip install scikit-learn

### Psutil not found

pip install psutil

### React dependencies are missing

Navigate to the frontend:

cd frontend

Install dependencies:

npm install

Start React:

npm start

### Dashboard shows no data

Make sure the monitor is running:

python collector\monitor.py

Check that:

data/metrics.csv

contains monitoring records.

Then open:

http://127.0.0.1:5000/metrics

### Dashboard cannot connect to backend

Make sure Flask is running:

python backend\app.py

Test:

http://127.0.0.1:5000/

Expected response:

AI Monitoring Backend Running

### Port 5000 is already in use

Stop the existing Flask process or change the Flask port in backend/app.py.

Example:

app.run(debug=True, port=5001)

If the backend port is changed, update the API URL used by the React frontend.

### Port 3000 is already in use

React may automatically ask whether another port should be used. Accept the available port or stop the process using port 3000.

## Development Scope

This project is designed to run locally.

The current implementation does not require:

- Docker
- Kubernetes
- Kafka
- FastAPI
- WebSockets
- AWS
- Cloud deployment

The auto-scaling module currently provides scaling recommendations rather than actually provisioning cloud resources.

## Future Improvements

- Docker containerization
- Kubernetes deployment
- Prometheus integration
- Grafana dashboards
- Cloud-based auto-scaling
- WebSocket-based live updates
- Database-based metric storage
- Advanced anomaly detection
- Distributed monitoring
- AWS deployment
- Event-driven architecture

## Project Objective

The objective of this project is to combine real-time system monitoring, machine learning-based CPU prediction, intelligent scaling recommendations, REST APIs, and an interactive React dashboard into a complete full-stack monitoring solution.

The project demonstrates:

- Full-stack development
- Python backend development
- Flask REST API development
- Machine learning integration
- System resource monitoring
- Data collection and processing
- Data visualization
- Predictive monitoring
- Intelligent scaling recommendations
- Git and GitHub workflow

video link:  https://drive.google.com/file/d/1KDwRm1J8pqSujdoKG9X6LCN0xYGvAP67/view?usp=sharing

## License

This project is developed for educational and portfolio purposes.