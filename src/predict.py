from pathlib import Path

import joblib
import pandas as pd


MODEL_PATH = (
    Path(__file__).resolve().parents[1]
    / "models"
    / "automotive_price_prediction_model.joblib"
)


def load_model():
    """Load the saved vehicle price prediction model."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

    return joblib.load(MODEL_PATH)


def predict_vehicle_price(vehicle_data, model=None):
    """
    Predict vehicle price from a dictionary or a single-row DataFrame.
    """

    if isinstance(vehicle_data, dict):
        input_df = pd.DataFrame([vehicle_data])
    elif isinstance(vehicle_data, pd.DataFrame):
        input_df = vehicle_data.copy()
    else:
        raise TypeError("Input must be a dictionary or pandas DataFrame.")

    if len(input_df) != 1:
        raise ValueError("Please provide exactly one vehicle record.")

    if model is None:
        model = load_model()

    expected_columns = list(model.feature_names_in_)

    missing_columns = set(expected_columns) - set(input_df.columns)
    extra_columns = set(input_df.columns) - set(expected_columns)

    if missing_columns or extra_columns:
        raise ValueError(
            f"Missing columns: {sorted(missing_columns)}. "
            f"Unexpected columns: {sorted(extra_columns)}."
        )

    input_df = input_df[expected_columns]

    predicted_price = float(model.predict(input_df)[0])

    return round(predicted_price, 2)
