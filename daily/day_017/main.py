"""
Day 017 – Model Evaluation & Validation
Objective: Evaluate regression models using standard metrics
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def main():
    df = pd.read_csv("daily/day_016/data/week.csv")

    print("\n ---- raw data ----")
    print(df)

    # Features and target
    x = df[["day", "is_workday", "prev_day_hours"]]
    y = df["hours"]
    
    x_train, x_test, y_train, y_test = train_test_split(
        x,y, test_size=0.3, random_state=42
    )
    
    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    #Evaluation Metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\n--- Evaluation Metrics (Test Set) ---")
    print(f"MSE : {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE : {mae:.4f}")
    print(f"R²  : {r2:.4f}")

    cv_scores = cross_val_score(
        model, x, y, cv=5, scoring="neg_mean_squared_error"
    )
    cv_rmse = np.sqrt(-cv_scores)
    print("\n--- Cross-Validation RMSE ---")
    print(f"Mean RMSE: {cv_rmse.mean():.4f}")
    print(f"Std RMSE : {cv_rmse.std():.4f}")


if __name__ == "__main__":
    main()
