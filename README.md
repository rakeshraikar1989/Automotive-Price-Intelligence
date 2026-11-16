# Automotive Price Intelligence & Prediction

## Project Overview

Automotive Price Intelligence & Prediction is a machine learning project developed to analyse automobile characteristics and predict vehicle prices using historical automobile import data.

The project explores the relationship between vehicle specifications and pricing, compares multiple regression algorithms, and identifies a suitable predictive model.

## Project Objectives

- Perform exploratory data analysis on automobile specifications.
- Identify important factors associated with vehicle prices.
- Handle missing values and prepare numerical and categorical features.
- Train and compare multiple regression algorithms.
- Optimise model hyperparameters using cross-validation.
- Evaluate model performance on an independent test dataset.
- Develop a reusable prediction module.
- Document modelling challenges and business insights.

## Dataset

- Source: 1985 Auto Imports Database.
- Records supplied: 201.
- Attributes: 26.
- Independent variables: 25.
- Target variable: `price`.

The supplied dataset contains missing values in several independent variables. No target prices were missing.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy
- Statsmodels
- Joblib
- Jupyter Notebook
- Pytest

## Machine Learning Models

The following regression algorithms were evaluated:

1. Dummy Regressor (baseline)
2. Linear Regression
3. Ridge Regression
4. Lasso Regression
5. Decision Tree Regressor
6. Random Forest Regressor
7. Extra Trees Regressor
8. Gradient Boosting Regressor

Hyperparameter optimisation was performed using RandomizedSearchCV with five-fold cross-validation.

## Final Model Performance

The final model was selected programmatically using repeated cross-validation on training data. The independent holdout set was evaluated only after selection.

| Metric | Result |
|---|---:|
| Selected model | Gradient Boosting |
| Repeated-CV MAE | 1535.23 |
| Holdout MAE | 1506.68 |
| Holdout RMSE | 2275.75 |
| Holdout R² | 0.9577 |
| Holdout MAPE | 9.55% |

The holdout contains 41 records. See the model comparison report and notebook for bootstrap intervals and limitations.



Hyperparameter tuning and model selection use the same cross-validation framework. The best CV estimate may therefore be optimistic. The independent holdout provides a separate final performance assessment.

## Key Findings

- curb_weight: mean validation permutation importance 1137.83
- engine_size: mean validation permutation importance 410.98
- horsepower: mean validation permutation importance 319.53
- width: mean validation permutation importance 290.84
- wheel_base: mean validation permutation importance 196.77

These are predictive associations, not causal effects. Importance estimates can be unstable for correlated features and small folds.

## Project Structure

Automotive-Evaluation-Improvements/
- data/raw/auto_imports.csv
- notebooks/Automotive_Price_Intelligence_Improved_Copy.ipynb
- src/predict.py
- models/automotive_price_prediction_model.joblib
- visualizations/ (9 charts)
- reports/model_comparison_report.md
- reports/challenges_faced_report.md
- tests/test_prediction.py
- requirements.txt
- .gitignore
- README.md

## Installation

Clone the repository and navigate to the project directory.

Create a virtual environment:

    python -m venv .venv

Activate the environment in Windows PowerShell:

    .venv\Scripts\Activate.ps1

Install the required dependencies:

    pip install -r requirements.txt

## Running the Notebook

Start Jupyter Notebook:

    jupyter notebook

Open the following notebook:

    notebooks/Automotive_Price_Intelligence_Improved_Copy.ipynb

Select the appropriate Python environment and execute the notebook cells in order.

## Making a Prediction

Run this Python example from the project root:

```python
from src.predict import predict_vehicle_price
from tests.test_prediction import get_valid_vehicle
vehicle = get_valid_vehicle()
predicted_price = predict_vehicle_price(vehicle)
print(f'Predicted vehicle price: {predicted_price:.2f}')
```

## Automated Testing

Run the tests from the project root:

    python -m pytest tests/ -v

The current test suite covers:

- Valid vehicle predictions.
- Missing feature validation.
- Invalid input type validation.

All three tests passed during project verification.

## Reports and Visualisations

The reports directory contains:

- Model Comparison Report.
- Challenges Faced Report.

The visualizations directory contains exploratory data analysis plots, feature importance analysis and final model diagnostic plots.

These visualisations cover:

- Correlation analysis.
- Manufacturer distribution.
- Categorical feature analysis against price.
- Numerical feature distributions.
- Missing value analysis.
- Numerical features against price.
- Final model diagnostics.
- Feature importance.
- Vehicle price by engine type.

## Limitations

- The dataset is small, containing only 201 supplied records.
- It represents historical automobile imports from the 1980s.
- The independent test set contains only 41 records.
- Results do not establish prediction accuracy for modern automobile markets.
- External validation using larger and more recent datasets is recommended before commercial deployment.

## Conclusion

The model selected using training-only repeated cross-validation was **Gradient Boosting**.

On the independent holdout set of 41 records:
- MAE: 1506.68 dataset price units
- RMSE: 2275.75 dataset price units
- R²: 0.9577
- MAPE: 9.55%

This historical, small-sample model is a demonstration prototype, not a current-market commercial pricing tool. It requires recent representative data, external validation, monitoring and fairness assessment before deployment.
