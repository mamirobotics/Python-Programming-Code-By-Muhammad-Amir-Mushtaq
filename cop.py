import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load dataset
file_path = r'C:\Users\Acer\Desktop\Semester 6 Data\Himself work\Health_conditions_among_children_under_age_18__by_selected_characteristics__United_States.csv'
data = pd.read_csv(file_path)

# Drop rows with missing target values
data = data.dropna(subset=['ESTIMATE'])

# Selecting relevant features and target
X = data[['PANEL_NUM', 'UNIT_NUM', 'STUB_NAME_NUM', 'STUB_LABEL_NUM', 'YEAR_NUM', 'AGE_NUM', 'SE']]
y = data['ESTIMATE']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling for scaling-required models
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Polynomial Features (degree=2)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Function to Evaluate and Plot Results
def evaluate_model(model, title, X_test_used):
    y_pred = model.predict(X_test_used)
    
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f'{title}:\nMSE: {mse:.4f}, MAE: {mae:.4f}, R2: {r2:.4f}\n')

    plt.figure(figsize=(6, 6))
    plt.scatter(y_test, y_pred, color='blue', alpha=0.6, label='Predicted vs Actual')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', lw=2, linestyle='dashed', label='Perfect Fit')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Models and evaluation
models = [
    (LinearRegression(), 'Multiple Linear Regression', X_test),
    (LinearRegression(), 'Polynomial Regression', X_test_poly),
    (Lasso(alpha=0.1), 'Lasso Regression', X_test_scaled),
    (Ridge(alpha=1.0), 'Ridge Regression', X_test_scaled),
    (ElasticNet(alpha=0.1, l1_ratio=0.5), 'Elastic Net Regression', X_test_scaled),
    (KNeighborsRegressor(n_neighbors=5), 'KNN Regression', X_test_scaled),
]

for model, title, X_used in models:
    model.fit(X_train_scaled if 'scaled' in title.lower() else (X_train_poly if 'Polynomial' in title else X_train), y_train)
    evaluate_model(model, title, X_used)
