import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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

    mse = mean_squared_error(y_test, y_pred)

    print("\n---- model evluation ----")
    print(f"Mean Squared Error: {mse:.4f}")

    print("\n---- Model Coefficients ---- ")
    for feature, coef in zip(x.columns, model.coef_):
        print(f"{feature}: {coef:.4f}")
    
    print(f"Intercept: {model.intercept_:.4f}")

    comparison = x_test.copy()
    comparison["actual_hours"]      = y_test.values
    comparison["predicted_hours"]   = y_pred

    print("\n---- Prediction vs Actuals ----")
    print(comparison)

    


if __name__ == "__main__":
    main()