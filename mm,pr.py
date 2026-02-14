from sklearn.preprocessing import StandardScaler

# Scaling the features (for KNN, Lasso, Ridge, Elastic Net)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Polynomial Regression Scaling
X_train_poly_scaled = scaler.fit_transform(X_train_poly)
X_test_poly_scaled = scaler.transform(X_test_poly)

# Re-train models where scaling is needed
lasso.fit(X_train_scaled, y_train)
ridge.fit(X_train_scaled, y_train)
elastic.fit(X_train_scaled, y_train)
knn.fit(X_train_scaled, y_train)

# Update polynomial regression training
poly_reg.fit(X_train_poly_scaled, y_train)

# Improved Plot Function
def evaluate_model(model, title):
    y_pred = model.predict(X_test_scaled if 'Poly' not in title else X_test_poly_scaled)
    
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f'{title}:\nMSE: {mse:.4f}, MAE: {mae:.4f}, R2: {r2:.4f}\n')

    # Plot
    plt.figure(figsize=(6, 6))
    plt.scatter(y_test, y_pred, color='blue', alpha=0.6, label='Predicted vs Actual')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', lw=2, linestyle='dashed', label='Perfect Fit')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
