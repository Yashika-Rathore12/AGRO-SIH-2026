def generate_advisory(data):
    crop = data.crop
    moisture = data.soil_moisture
    n, p, k = data.nitrogen, data.phosphorus, data.potassium
    temp, humidity = data.temperature, data.humidity

    actions = []
    severity = "Good"

    if moisture < 25:
        actions.append("Irrigation suggested: soil moisture is below the 25% threshold.")
        severity = "Action"
    elif moisture > 75:
        actions.append("Avoid irrigation now: soil moisture is already high.")
    else:
        actions.append("Irrigation can be scheduled after checking the next rainfall window.")

    if n < 40:
        actions.append("Nitrogen is low: consider a soil-test-based nitrogen plan.")
        severity = "Action"
    if p < 20:
        actions.append("Phosphorus is low: consider a soil-test-based phosphorus correction.")
    if k < 30:
        actions.append("Potassium is low: consider a soil-test-based potassium correction.")

    if humidity > 80 and temp > 24:
        actions.append("Disease-risk watch: warm and humid conditions can favor fungal pressure.")
        severity = "Watch"

    score = max(0, min(100, 100 - max(0, 40-n)*0.8 - max(0, 25-p)*0.5 - max(0, 35-k)*0.5))
    return {
        "crop": crop,
        "health_score": round(score, 1),
        "severity": severity,
        "actions": actions,
        "note": "Thresholds are advisory defaults. Final fertilizer/chemical decisions should use a local soil test and agronomist guidance."
    }
