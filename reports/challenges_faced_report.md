# Automotive Price Intelligence & Prediction
## Challenges Faced Report

### 1. Dataset Size and Source Differences

**Challenge:**
The supplied CSV contained 201 records and 26 attributes, while the accompanying dataset documentation described 205 instances.

**Solution:**
The actual supplied CSV was treated as the source of truth for implementation. Its dimensions and column structure were verified independently.

**Reason:**
Using the actual supplied data avoids making assumptions about records that were not present.

### 2. Missing Values

**Challenge:**
The dataset contained 51 missing entries across six attributes:
- normalized_losses: 37
- num_of_doors: 2
- bore: 4
- stroke: 4
- horsepower: 2
- peak_rpm: 2

The target variable, price, had no missing values in the supplied CSV.

**Solution:**
Median imputation was used for numerical features, and most-frequent-value imputation was used for categorical features.

**Reason:**
Median imputation is less sensitive to extreme numerical values than mean imputation. Most-frequent-value imputation preserves valid categorical values without introducing artificial categories.

### 3. Mixed Data Types

**Challenge:**
The dataset contained both numerical and categorical variables.

**Solution:**
A ColumnTransformer was used to apply separate preprocessing:
- Numerical features: median imputation and StandardScaler.
- Categorical features: most-frequent imputation and OneHotEncoder with handle_unknown="ignore".

**Reason:**
Regression algorithms require numerical input. One-hot encoding represents categories without imposing an artificial numerical order. Scaling helps scale-sensitive algorithms.

### 4. Potential Outliers

**Challenge:**
IQR analysis identified potential outliers, including 14 high-priced vehicles above the upper price threshold of 29,587.50.

**Solution:**
The high-priced observations were investigated and retained because their specifications were plausible for premium and high-performance vehicles.

**Reason:**
Removing valid luxury vehicles could distort the target distribution and reduce the model's ability to predict higher-priced cars.

### 5. Multicollinearity

**Challenge:**
VIF analysis identified relationships among vehicle dimensions, engine characteristics and fuel-efficiency variables. For example, city_mpg had a VIF of 25.80 and highway_mpg had a VIF of 23.35.

**Solution:**
Multiple model families were evaluated, including Ridge and Lasso regression, tree-based models and ensemble methods.

**Reason:**
Regularised regression can help manage correlated predictors, while tree-based models can capture nonlinear relationships. Features were not removed solely because of high VIF values.

### 6. Nonlinear Relationships

**Challenge:**
The relationship between vehicle specifications and price was not necessarily linear. Different manufacturers, engine configurations and vehicle characteristics can interact.

**Solution:**
Linear regression models were compared with Decision Tree, Random Forest, Extra Trees and Gradient Boosting models.

**Reason:**
Comparing different algorithm families helps identify whether more flexible nonlinear models provide better predictive performance.

### 7. Overfitting and Generalisation

**Challenge:**
Some models showed large differences between training and validation errors. Extra Trees, in particular, showed a large generalisation gap after tuning.

**Solution:**
Five-fold cross-validation, train-validation MAE comparison, hyperparameter tuning and an independent test set were used.

**Reason:**
These methods provide a more reliable assessment of model performance and help identify models that fit training data too closely.

### 8. Small Test Dataset

**Challenge:**
The dataset contained only 201 records, leaving 41 observations in the independent test set after the 80:20 split.

**Solution:**
A fixed random state of 42 was used for reproducibility, and five-fold cross-validation was used during model evaluation and tuning.

**Reason:**
Cross-validation makes better use of the limited training data. However, a small holdout set still introduces uncertainty into performance estimates.

### 9. Model Persistence and Prediction Validation

**Challenge:**
A trained model must be reusable outside the notebook and should reject incomplete input.

**Solution:**
The complete preprocessing and prediction pipeline was saved using Joblib. A separate Python prediction module and automated pytest tests were created.

**Reason:**
Saving the complete pipeline ensures that new data receives the same preprocessing as training data. Input validation prevents incomplete or unexpected records from being passed to the model.

### 10. Historical Dataset Limitations

**Challenge:**
The dataset represents automobile imports from the 1980s and contains a limited number of observations.

**Solution:**
The project documents the historical scope of the dataset and recommends validation with larger and more recent data before real-world commercial use.

**Reason:**
Strong performance on this dataset does not establish that the model can accurately predict prices in today's automobile market.

### 11. Conclusion

The project addressed missing data, mixed feature types, potential outliers, multicollinearity, nonlinear relationships, overfitting and limited dataset size through structured exploratory analysis, preprocessing pipelines, cross-validation, model comparison and automated testing.

The selected Gradient Boosting model demonstrated the strongest overall test-set performance among the tuned candidates. Its limitations have also been documented to ensure that the results are interpreted responsibly.
