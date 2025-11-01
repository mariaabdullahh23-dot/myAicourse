import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("Hospital Beds Management.csv")
print(df.shape)
print(df.head())

graph = sns.countplot(x='Emergency_Available', data=df)
graph.figure.suptitle("Emergency Availability Distribution")
graph.figure.show()
print(input("Wait for me..."))

X = df.drop(columns=['Emergency_Available', 'Hospital_ID', 'Hospital_Name'])
Y = df['Emergency_Available']

X = pd.get_dummies(X, drop_first=True)

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42, train_size=0.8)
print("Train/Test split:", x_train.shape[0], x_test.shape[0])

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = RandomForestClassifier(random_state=42)
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_test_scaled)

acc = accuracy_score(y_test, y_pred)
print("Accuracy score:", round(acc, 3))

cr = classification_report(y_test, y_pred)
print("Classification report:\n", cr)

cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix:\n", cm)

plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Emergency Prediction')
plt.show()

print(input("Wait for me..."))
