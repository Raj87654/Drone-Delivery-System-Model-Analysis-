import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

np.random.seed(42)
n = 500

distance = np.random.uniform(1, 20, n)
weight = np.random.uniform(0.5, 5, n)
wind = np.random.uniform(0, 20, n)


battery = (distance * 2.5) + (weight * 5) + (wind * 1.5)
battery = battery + np.random.normal(0, 2, n)


data = pd.DataFrame({
    "distance": distance,
    "weight": weight,
    "wind": wind,
    "battery": battery
})
print(data.head())

data["energy_load"] = data["distance"] * data["weight"]


X = data[["distance", "weight", "wind", "energy_load"]]
y = data["battery"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print("Model Trained Successfully")
print("Mean Absolute Error:", round(mae, 2))


def predict_battery(distance, weight, wind):
    energy_load = distance * weight

    input_data = pd.DataFrame({
        "distance": [distance],
        "weight": [weight],
        "wind": [wind],
        "energy_load": [energy_load]
    })

    prediction = model.predict(input_data)
    return prediction[0]



sample_prediction = predict_battery(10, 2, 10)

print("\n Sample Prediction:")
print("Distance=10km, Weight=2kg, Wind=10km/h")
print("Predicted Battery Usage:", round(sample_prediction, 2), "%")


def drone_decision(distance, weight, wind, available_battery):
    required_battery = predict_battery(distance, weight, wind)

    print("\n Decision Analysis:")
    print("Required Battery:", round(required_battery, 2), "%")
    print("Available Battery:", available_battery, "%")

    if required_battery > available_battery:
        return " Delivery Rejected: Not enough battery"

    if wind > 25:
        return " Delivery Rejected: Wind too strong"

    if weight > 5:
        return " Delivery Rejected: Overweight package"

    return " Delivery Approved"



result = drone_decision(10, 2, 10, 60)
print("\n Final Decision:", result)