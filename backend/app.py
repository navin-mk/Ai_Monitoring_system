import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, jsonify
import pandas as pd

from model.predict import predict_cpu
from backend.email_alert import send_email_alert
from backend.autoscale import get_scaling_decision

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
FILE = "data/metrics.csv"


@app.route("/")
def home():
    return "AI Monitoring Backend Running 🚀"


@app.route("/metrics")
def get_metrics():
    try:
        df = pd.read_csv(FILE)
        latest = df.tail(1).to_dict(orient="records")[0]

        cpu = latest["cpu"]

        # Prediction
        pred_result = predict_cpu()
        if "error" in pred_result:
            return jsonify(pred_result)

        predicted = pred_result["predicted_cpu"]

        # Auto scaling
        scaling = get_scaling_decision(cpu, predicted)

        # Email Alert only
        if scaling["action"] == "scale_up":
            msg = f"⚠️ High CPU! Current: {cpu}%, Predicted: {predicted}%"
        

        return jsonify({
            "current": latest,
            "predicted_cpu": predicted,
            "scaling": scaling
        })

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/history")
def get_history():
    try:
        df = pd.read_csv(FILE)
        data = df.tail(20).to_dict(orient="records")
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/predict")
def predict():
    result = predict_cpu()
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)