# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv(r'D:\Coding\Machine Learning\Mobile Price Predictor\test.csv')
df = df.drop('id', axis=1)

# Add price_range if not present
def classify_price(row):
    score = row['ram']*0.3 + row['battery_power']*0.2 + row['px_height']*0.1 + row['px_width']*0.1
    if score < 2500:
        return 0
    elif score < 4500:
        return 1
    else:
        return 2

df['price_range'] = df.apply(classify_price, axis=1)

# Split
X = df.drop('price_range', axis=1)
y = df['price_range']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
