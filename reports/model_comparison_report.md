# Automotive Price Intelligence & Prediction
## Model Comparison Report — Evaluation Improvements

### Evaluation Design
- Dataset records: 201
- Training records: 160
- Independent holdout records: 41
- Model-selection method: repeated 5-fold cross-validation (2 repeats)
- Hyperparameter search: 8 sampled configurations per tuned model
- The holdout set was used only once, after model selection.

### Selected Model
**Gradient Boosting**

Selected using the lowest repeated-CV MAE among the tuned candidates.

### Final Performance

| Metric | Result |
|---|---:|
| Repeated-CV MAE | 1535.23 |
| Repeated-CV MAE standard deviation | 215.06 |
| Holdout MAE | 1506.68 |
| Holdout RMSE | 2275.75 |
| Holdout R² | 0.9577 |
| Holdout MAPE | 9.55% |

### Bootstrap Intervals
The empirical 95% bootstrap intervals are reported in the notebook. They are based on resampling the small holdout set and should be interpreted cautiously.

### Selected Estimator Parameters

The selected Gradient Boosting model uses:

- Learning rate: 0.05
- Number of estimators: 250
- Maximum tree depth: 2
- Minimum samples per leaf: 2
- Subsample fraction: 0.9

These parameters were selected through training-only cross-validation.

### Metric Interpretation
MAE is the average absolute prediction error in the dataset's price units. RMSE gives larger errors greater influence. MAPE expresses average relative error but can be unstable for observations with very small actual prices.

### Limitations
The dataset contains only 201 historical records. It represents an older automobile-import market and does not establish accuracy for current vehicle prices. Feature importance describes predictive association, not causation. External validation on a larger, current dataset is required before operational use.
