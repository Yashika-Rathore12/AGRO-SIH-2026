from pathlib import Path
from PIL import Image
import numpy as np

MODEL_DIR = Path("models")

def _demo_image_screening(image: Image.Image):
    """
    Offline demo adapter.
    It intentionally avoids claiming clinical/field-grade accuracy.
    A production SIH deployment should replace this function with a trained
    PlantVillage/custom field dataset model.
    """
    img = image.convert("RGB").resize((128, 128))
    arr = np.asarray(img).astype(np.float32) / 255.0
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]

    green = float(np.mean(g))
    yellow = float(np.mean((r + g) / 2 - b))
    brown = float(np.mean((r > 0.30) & (g > 0.18) & (g < 0.55) & (b < 0.35)))

    if brown > 0.14 and green < 0.42:
        label, confidence = "Leaf spot / stress pattern", 0.76
        explanation = "The image contains a comparatively high brown/dark pixel ratio. This is a screening signal, not a confirmed diagnosis."
    elif yellow > 0.25 and green < 0.52:
        label, confidence = "Possible nutrient stress", 0.71
        explanation = "Yellowing-like image statistics were detected. Soil NPK telemetry should be checked before treatment."
    else:
        label, confidence = "No strong visible stress signal", 0.68
        explanation = "The image does not show a strong stress pattern under the demo screening rules."

    return {
        "diagnosis": label,
        "confidence": round(confidence * 100, 1),
        "model": "demo-screening-adapter",
        "explanation": explanation,
        "recommended_action": "Re-scan with a clear leaf image and validate with local agronomist advice before applying chemicals."
    }

def analyze_leaf(image: Image.Image):
    return _demo_image_screening(image)
