import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
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

# Fit Multiple Linear Regression Model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predictions
y_pred = lr.predict(X_test)

# Model Evaluation
print(f'MSE: {mean_squared_error(y_test, y_pred):.4f}')
print(f'MAE: {mean_absolute_error(y_test, y_pred):.4f}')
print(f'R² Score: {r2_score(y_test, y_pred):.4f}')

# Scatter Plot: Actual vs Predicted
plt.scatter(y_test, y_pred, color='blue', alpha=0.6, label='Predicted vs Actual')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', lw=2, linestyle='dashed', label='Perfect Fit')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Multiple Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
