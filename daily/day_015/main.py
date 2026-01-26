"""
Day 015 – First Predictive Model (Linear Regression)
Objective: Train and evaluate a simple regression model
"""
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


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
    model = LinearRegression()
    model.fit(x_train, y_train)

    #print("\n--- Training Data ---")
    #print(pd.concat([x_train, y_train], axis=1))

    #print("\n--- Test Data ---")
    #print(pd.concat([x_test, y_test], axis=1))


    #predictions
    y_pred = model.predict(x_test)

    # Evaluation
    mse = mean_squared_error(y_test, y_pred)

    print("\n ---- Model Evaluation ----")
    print(f"Mean Squared Error: {mse:.4f}")


    print("\n--- Model Parameters ---")
    print(f"Intercept: {model.intercept_:.4f}")
    print(f"Coefficient (day): {model.coef_[0]:.4f}")

    # Compare Actual vs Predicted
    comparison = pd.DataFrame({
        "day": x_test["day"],
        "Actual Hourse": y_test,
        "predicted hours": y_pred
    })

    df.plot(x="day", y="hours", kind="scatter")
    plt.show()

    plt.scatter([1, 2, 3], [4, 5, 6])
    plt.show()


    print("\n--- Predictions vs Actuals ---")
    print(comparison)
    



if __name__ == "__main__":
    main()