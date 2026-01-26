"""
Day 015 – First Predictive Model (Linear Regression)
Objective: Train and evaluate a simple regression model
"""
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score



def main():
    filepath = "daily/day_015/data/week.csv"
    df = pd.read_csv(filepath)

    print("\n---- Data set ----")
    print(df)

    x = df[["day"]]
    print(x)


    df["is_weekend"] = df["day"].isin([6,7]).astype(int)
    x = df[["day", "is_weekend"]]
    y = df["hours"]

    print(x)
    print("\ny:\n", y)

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=42
                                                        )
    #model training
    model = DecisionTreeRegressor(
        random_state=42,
        max_depth=3  # keeps the model from overfitting
    )
    model.fit(x_train, y_train)


    # -----------------------------
    # 4. Make Predictions
    # -----------------------------

    y_pred = model.predict(x_test)

    # -----------------------------
    # 5. Evaluate Model Performance
    # -----------------------------

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"R² Score: {r2:.4f}")

    df.plot(x="day", y="hours", kind="scatter")
    plt.show()

    plt.scatter([1, 2, 3], [4, 5, 6])
    plt.show()

    
    # -----------------------------
    # Train Linear Regression
    # -----------------------------
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    y_pred_lr = lr.predict(x_test)

    # -----------------------------
    # Train Decision Tree
    # -----------------------------
    dt = DecisionTreeRegressor(random_state=42, max_depth=3)
    dt.fit(x_train, y_train)
    y_pred_dt = dt.predict(x_test)

    # -----------------------------
    # Evaluate Both Models
    # -----------------------------
    results = {
        "Model": ["Linear Regression", "Decision Tree"],
        "MSE": [
            mean_squared_error(y_test, y_pred_lr),
            mean_squared_error(y_test, y_pred_dt)
        ],
        "MAE": [
            mean_absolute_error(y_test, y_pred_lr),
            mean_absolute_error(y_test, y_pred_dt)
        ],
        "R²": [
            r2_score(y_test, y_pred_lr),
            r2_score(y_test, y_pred_dt)
        ]
    }

    comparison_df = pd.DataFrame(results)
    print(comparison_df)    


if __name__ == "__main__":
    main()