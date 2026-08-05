from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np

ARTIFACT_DIR = Path(__file__).resolve().parent / "artifacts"

# Models are loaded once, at import time, not on every call - loading a
# .pkl file from disk is relatively slow, and the same model object can
# safely serve many predictions.
_spam_model = joblib.load(ARTIFACT_DIR / "spam_model.pkl")
_vectorizer = joblib.load(ARTIFACT_DIR / "vectorizer.pkl")
_priority_model = joblib.load(ARTIFACT_DIR / "priority_model.pkl")

# Must exactly match the column order used in src/train_priority.py /
# src/priority_features.py - if these drift apart, the model will silently
# read "reply_rate" values into what it thinks is "sender_frequency", etc.
_PRIORITY_FEATURE_ORDER = ["sender_frequency", "reply_rate", "has_urgent_keyword", "hour_of_day"]


def predict_spam(subject: str, body: str) -> bool:
    """Return True if the email looks like spam, else False.

    subject/body are combined into one string because that's how the
    model was trained (see data_loader.py's `text` column) - the
    vectorizer's vocabulary was learned on subject+body concatenated, so
    inference must feed it text in the same shape.
    """
    text = f"{subject or ''} {body or ''}".strip()
    vector = _vectorizer.transform([text])  # reuses vectorizer's learned vocabulary
    prediction = _spam_model.predict(vector)[0]  # 0 or 1
    return bool(prediction)


def predict_priority(features: dict) -> float:
    """Return a priority score in [0, 1] - higher means show near the top
    of the inbox.

    Raises ValueError if `features` is missing a required key, so a
    backend/ML contract mismatch fails loudly at integration time instead
    of silently corrupting predictions.
    """
    missing = [k for k in _PRIORITY_FEATURE_ORDER if k not in features]
    if missing:
        raise ValueError(f"predict_priority() missing required feature(s): {missing}")

    vector = np.array([[features[k] for k in _PRIORITY_FEATURE_ORDER]], dtype=float)
    raw_score = _priority_model.predict(vector)[0]
    return float(np.clip(raw_score, 0.0, 1.0))