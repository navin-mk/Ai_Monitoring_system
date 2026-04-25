def get_scaling_decision(current_cpu, predicted_cpu):
    if predicted_cpu > 80:
        return {
            "action": "scale_up",
            "message": "⬆️ Scale UP (High Load Expected)"
        }

    elif predicted_cpu < 20:
        return {
            "action": "scale_down",
            "message": "⬇️ Scale DOWN (Low Usage)"
        }

    else:
        return {
            "action": "no_action",
            "message": "⚖️ System Stable"
        }