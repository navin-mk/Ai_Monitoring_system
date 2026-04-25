import pandas as pd

FILE = "data/metrics.csv"

def predict_cpu():
    try:
        df = pd.read_csv(FILE)

        if len(df) < 5:
            return {"error": "Not enough data"}

        # simple prediction (average of last 5)
        predicted = df["cpu"].tail(5).mean()

        return {
            "predicted_cpu": round(predicted, 2)
        }

    except Exception as e:
        return {"error": str(e)}