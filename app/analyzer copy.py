def calculate_health(scan_data):
    total_checks = len(scan_data)
    passed_checks = sum(scan_data.values())

    score = (passed_checks / total_checks) * 100

    if score >= 90:
        status = "Excellent"
    elif score >= 75:
        status = "Good"
    elif score >= 50:
        status = "Moderate"
    else:
        status = "Poor"

    return {
        "score": round(score, 2),
        "status": status
    }