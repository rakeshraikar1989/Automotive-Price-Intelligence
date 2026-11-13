# Automotive Price Intelligence & Prediction
## Model Comparison Report

### 1. Objective

The objective was to compare multiple regression algorithms to predict automobile prices using 25 vehicle attributes. The models were evaluated using five-fold cross-validation, hyperparameter tuning and an independent test dataset.

### 2. Baseline Model

A Dummy Regressor using the training-set mean was used as the baseline.

| Metric | Baseline Result |
|---|---:|
| Test MAE | 8262.03 |
| Test RMSE | 11488.71 |
| Test R² | -0.0788 |

The negative R² indicates that the baseline performed poorly on the test dataset.

### 3. Initial Model Comparison

Five-fold cross-validation results before hyperparameter tuning:

| Model | CV Validation MAE | CV MAE Std | CV RMSE | CV R² |
|---|---:|---:|---:|---:|
| Gradient Boosting | 1547.92 | 182.09 | 2201.28 | 0.88 |
| Extra Trees | 1684.87 | 246.16 | 2477.75 | 0.86 |
| Random Forest | 1700.37 | 203.72 | 2460.36 | 0.85 |
| Ridge Regression | 1811.63 | 232.70 | 2579.97 | 0.85 |
| Lasso Regression | 1814.32 | 252.23 | 2703.97 | 0.82 |
| Linear Regression | 1929.24 | 312.42 | 2660.42 | 0.84 |
| Decision Tree | 2087.68 | 303.20 | 2863.64 | 0.79 |

Gradient Boosting achieved the lowest validation MAE among the initial candidate models.

### 4. Hyperparameter Tuning

RandomizedSearchCV was used with five-fold cross-validation and 12 parameter combinations per candidate model.

| Model | Best CV MAE |
|---|---:|
| Gradient Boosting | 1464.09 |
| Random Forest | 1603.99 |
| Extra Trees | 1614.13 |
| Ridge Regression | 1794.03 |

The tuned Gradient Boosting model used:
- n_estimators: 250
- learning_rate: 0.05
- max_depth: 2
- min_samples_leaf: 2
- subsample: 0.9
- random_state: 42

### 5. Final Test-Set Comparison

The tuned models were evaluated on the independent test set containing 41 records.

| Model | Test MAE | Test RMSE | Test R² | Test MAPE |
|---|---:|---:|---:|---:|
| Gradient Boosting | 1506.68 | 2275.75 | 0.96 | 9.55% |
| Extra Trees | 1572.99 | 2610.51 | 0.94 | 9.01% |
| Random Forest | 1905.28 | 2978.94 | 0.93 | 10.45% |
| Ridge Regression | 2485.84 | 3742.38 | 0.89 | 14.92% |

### 6. Production Model Recommendation

**Recommended model: Tuned Gradient Boosting Regressor**

Reasons:
- Lowest test MAE among the tuned models.
- Lowest test RMSE among the tuned models.
- Highest test R².
- Strong five-fold cross-validation performance.
- Lower prediction error than the other evaluated models on the independent test set.

Extra Trees achieved a slightly lower MAPE, but Gradient Boosting performed better on MAE, RMSE and R². Therefore, Gradient Boosting is selected as the primary model based on the overall evaluation.

### 7. Generalisation and Limitations

The tuned Gradient Boosting model recorded a cross-validation training MAE of 580.91 and validation MAE of 1464.09, giving a generalisation gap of 883.18. This indicates some difference between training and validation performance.

The independent test set contains only 41 records. Results should therefore be interpreted with caution. The dataset represents historical automobile imports from the 1980s and does not establish accuracy for today's automobile market.

External validation on a larger, more recent and representative dataset is recommended before commercial deployment.

### 8. Conclusion

Gradient Boosting provided the strongest overall predictive performance among the evaluated tuned models. It was saved as the final model and its reloaded predictions were verified against the original model predictions.
