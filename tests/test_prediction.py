import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from predict import predict_vehicle_price


def get_valid_vehicle():
    return {
        "symboling": 3,
        "normalized_losses": 122,
        "make": "alfa-romero",
        "fuel_type": "gas",
        "aspiration": "std",
        "num_of_doors": "two",
        "body_style": "convertible",
        "drive_wheels": "rwd",
        "engine_location": "front",
        "wheel_base": 88.6,
        "length": 168.8,
        "width": 64.1,
        "height": 48.8,
        "curb_weight": 2548,
        "engine_type": "dohc",
        "num_of_cylinders": "four",
        "engine_size": 130,
        "fuel_system": "mpfi",
        "bore": 3.47,
        "stroke": 2.68,
        "compression_ratio": 9.0,
        "horsepower": 111,
        "peak_rpm": 5000,
        "city_mpg": 21,
        "highway_mpg": 27
    }


def test_valid_vehicle_prediction():
    prediction = predict_vehicle_price(get_valid_vehicle())

    assert isinstance(prediction, float)
    assert prediction > 0


def test_missing_features_raise_error():
    invalid_vehicle = {
        "make": "toyota",
        "fuel_type": "gas"
    }

    with pytest.raises(ValueError, match="Missing columns"):
        predict_vehicle_price(invalid_vehicle)


def test_invalid_input_type_raises_error():
    with pytest.raises(TypeError):
        predict_vehicle_price("invalid input")
