import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# XOR Data
X, y = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]), np.array([[0], [1], [1], [0]])

# Model definition
model = Sequential([
    Dense(2, input_dim=2, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10000, verbose=0)
print("Accuracy:", model.evaluate(X, y, verbose=0)[1])

# Predictions
print("Predictions:", np.round(model.predict(X)).astype(int).flatten())
