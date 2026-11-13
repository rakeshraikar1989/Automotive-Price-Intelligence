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

The tuned Gradient Boosting model was selected as the recommended model.

| Metric | Result |
|---|---:|
| Cross-validation MAE | 1464.09 |
| Test MAE | 1506.68 |
| Test RMSE | 2275.75 |
| Test R² | 0.9577 |
| Test MAPE | 9.55% |

The independent test dataset contained 41 records.

## Key Findings

- Engine size, curb weight, vehicle width and horsepower were among the most important features for the selected model.
- Vehicle characteristics showed different relationships with price.
- Premium and high-performance vehicles formed part of the higher-priced observations.
- Gradient Boosting achieved the strongest overall test-set performance among the tuned models.

Feature importance describes model reliance on predictors and should not be interpreted as proof of causation.

## Project Structure

Automotive-Price-Intelligence/
|
|-- data/
|   |-- raw/
|   |-- processed/
|
|-- notebooks/
|   |-- Automotive_Price_Intelligence_and_Prediction.ipynb
|
|-- src/
|   |-- predict.py
|
|-- models/
|   |-- automotive_price_prediction_model.joblib
|
|-- visualizations/
|
|-- reports/
|   |-- model_comparison_report.md
|   |-- challenges_faced_report.md
|
|-- tests/
|   |-- test_prediction.py
|
|-- documentation/
|
|-- requirements.txt
|-- .gitignore
|-- README.md

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

    notebooks/Automotive_Price_Intelligence_and_Prediction.ipynb

Select the appropriate Python environment and execute the notebook cells in order.

## Making a Prediction

The reusable prediction module is located at:

    src/predict.py

Example usage:

    from src.predict import predict_vehicle_price

    vehicle = {
        # Supply all 25 required vehicle features.
    }

    predicted_price = predict_vehicle_price(vehicle)
    print(predicted_price)

The prediction function validates the supplied feature names and loads the saved model automatically.

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
- Automobile price distribution.

## Limitations

- The dataset is small, containing only 201 supplied records.
- It represents historical automobile imports from the 1980s.
- The independent test set contains only 41 records.
- Results do not establish prediction accuracy for modern automobile markets.
- External validation using larger and more recent datasets is recommended before commercial deployment.

## Conclusion

The project demonstrates an end-to-end machine learning workflow covering exploratory data analysis, data preprocessing, model comparison, hyperparameter optimisation, model evaluation, model persistence, reusable prediction functionality and automated testing.

The tuned Gradient Boosting model demonstrated the strongest overall performance among the evaluated tuned candidates on the independent test dataset.

