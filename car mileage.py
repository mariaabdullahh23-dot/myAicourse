import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_csv("car_mileage.csv")
print(df.shape)
print(df.head())

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Feature Correlation with Mileage")
plt.show()
print(input("Wait for me..."))

X = df.drop(columns=['Mileage_kmpl', 'Car_ID'])
Y = df['Mileage_kmpl']

X = pd.get_dummies(X, drop_first=True)

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42, train_size=0.8)
print("Train/Test Split:", x_train.shape[0], "/", x_test.shape[0])

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = RandomForestRegressor(random_state=42, n_estimators=100)
model.fit(x_train_scaled, y_train)


y_pred = model.predict(x_test
