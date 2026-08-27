# ============================================================
# King County House Price Prediction
# Using sklearn - Training and Testing with 5 Regression Algorithms
# ============================================================

# Importing required libraries
import numpy as np                  # For numerical operations
import pandas as pd                 # For handling datasets

# ------------------------------------------------------------
# Step 1: Load dataset
# ------------------------------------------------------------
dataset = pd.read_csv("kc_house_data.csv")   # Read CSV file
print(dataset.head())                         # Display first 5 rows
print('-'*80)
print(dataset.info())

# ------------------------------------------------------------
# Step 2: Selecting features (X) and target (y)
# ------------------------------------------------------------
# We drop columns that aren't useful as numeric predictors:
# 'id'   -> just a unique identifier, no predictive value
# 'date' -> text date, would need special processing to be useful
# 'price'-> this is our target, not a feature
features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
            'waterfront', 'view', 'condition', 'grade', 'sqft_above',
            'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
            'lat', 'long', 'sqft_living15', 'sqft_lot15']


# Fill any missing values with the column median (e.g. sqft_above had 2 NaNs)
dataset[features] = dataset[features].fillna(dataset[features].median())

X = dataset[features].values
y = dataset['price'].values

# Display shape of data
print('-'*80)
print(f'Shape of X is {X.shape}\nShape of y is {y.shape}')

# ------------------------------------------------------------
# Step 3: Splitting dataset into training and testing sets
# ------------------------------------------------------------
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

print('-'*80)
print(f"Length of X_train: {len(X_train)}\nLength of X_test: {len(X_test)}")
print(f"Length of y_train: {len(y_train)}\nLength of y_test: {len(y_test)}")

# ------------------------------------------------------------
# Step 4: Feature Scaling
# ------------------------------------------------------------
# Price prediction features have very different ranges
# (e.g. sqft_living: 300-13000, waterfront: 0-1, lat: ~47)
# Scaling puts everything on the same footing (mean=0, std=1)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)   # learn mean/std from training data, then scale
X_test = sc.transform(X_test)         # scale test data using the SAME mean/std (no re-fit)

# ------------------------------------------------------------
# Step 5: Helper function to evaluate each model
# ------------------------------------------------------------
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_model(name, model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)                 # Train model
    y_pred = model.predict(X_test)               # Predict on test data

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print('\n' + '-'*20 + f'{name}' + '-'*20)
    print(f"RMSE: {rmse:,.2f}")
    print(f"MAE:  {mae:,.2f}")
    print(f"R2 Score: {r2:.4f}")
    return {'Model': name, 'RMSE': rmse, 'MAE': mae, 'R2': r2}

results = []

# ============================================================
# 1. Linear Regression
# ============================================================
# Fits a straight-line relationship between features and price.
# Simple, fast, and a good baseline for regression problems.
from sklearn.linear_model import LinearRegression
results.append(evaluate_model('Linear Regression', LinearRegression(),
                               X_train, y_train, X_test, y_test))

# ============================================================
# 2. Ridge Regression
# ============================================================
# Like Linear Regression but adds a penalty (regularization) to
# shrink coefficients and reduce overfitting on correlated features.
from sklearn.linear_model import Ridge
results.append(evaluate_model('Ridge Regression', Ridge(),
                               X_train, y_train, X_test, y_test))

# ============================================================
# 3. Decision Tree Regressor
# ============================================================
# Splits data into branches based on feature values (like a flowchart)
# to predict price. Captures non-linear relationships.
from sklearn.tree import DecisionTreeRegressor
results.append(evaluate_model('Decision Tree Regressor', DecisionTreeRegressor(random_state=0),
                               X_train, y_train, X_test, y_test))

# ============================================================
# 4. Random Forest Regressor
# ============================================================
# Builds many decision trees and averages their predictions.
# Usually more accurate and less prone to overfitting than a single tree.
from sklearn.ensemble import RandomForestRegressor
results.append(evaluate_model('Random Forest Regressor', RandomForestRegressor(random_state=0, n_estimators=100),
                               X_train, y_train, X_test, y_test))

# ============================================================
# 5. Gradient Boosting Regressor
# ============================================================
# Builds trees sequentially, where each tree corrects the errors
# of the previous ones. Often gives strong accuracy on tabular data.
from sklearn.ensemble import GradientBoostingRegressor
results.append(evaluate_model('Gradient Boosting Regressor', GradientBoostingRegressor(random_state=0),
                               X_train, y_train, X_test, y_test))

# ------------------------------------------------------------
# Step 6: Compare all models side by side
# ------------------------------------------------------------
results_df = pd.DataFrame(results).sort_values(by='R2', ascending=False)
print('\n' + '='*60)
print('MODEL COMPARISON (sorted by R2 Score)')
print('='*60)
print(results_df.to_string(index=False))
