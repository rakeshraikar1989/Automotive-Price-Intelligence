# Automotive Price Intelligence & Prediction
## Challenges Faced and Methodology Improvements

### Dataset Size and Scope
The supplied dataset contains 201 records and represents historical automobile imports. Small samples limit the precision and generalisability of model estimates.

### Missing Data
Missing feature values are handled inside the model pipeline: median imputation for numerical columns and most-frequent imputation for categorical columns. The imputer is fitted separately within each training fold.

### Mixed Feature Types
A ColumnTransformer applies numerical scaling and categorical one-hot encoding. Unknown categories are handled without failing prediction.

### Outliers and Skew
Potential outliers are identified with the IQR rule and reviewed rather than automatically deleted. IQR flags unusual observations; it does not prove that a record is erroneous.

### Leakage Prevention
The preprocessor is not fitted before cross-validation. Each pipeline fits preprocessing only on the training portion of each fold. The independent holdout is not used for model selection or permutation importance.

### Model Selection and Validation
Candidate models and tuned parameters are compared using repeated 5-fold cross-validation on the training data. The selected model is chosen programmatically using the lowest repeated-CV MAE. Only that selected model is evaluated on the independent holdout.

### Uncertainty
Bootstrap intervals are calculated from the final holdout predictions. With only 41 holdout records, these intervals are approximate and may be unstable.

### Feature Importance
Permutation importance is calculated on training-data validation folds. It measures predictive dependence, not causal impact. Correlated features may share or mask importance.

### Operational Limitations
The selected model is a learning and demonstration prototype. It should not be deployed for current commercial pricing without current market data, external validation, uncertainty analysis, monitoring and fairness review.
