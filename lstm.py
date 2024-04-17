import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error

# Load data
data_path = './AAPL_stock_data.csv'  # Change this to the path of your CSV file
stock_data = pd.read_csv(data_path)
close_prices = stock_data['Close'].values.reshape(-1, 1)

# Constants for the model
sequence_length = 10
epochs = 10
batch_size = 32

# Scaling the close prices
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_prices = scaler.fit_transform(close_prices)

# Function to create sequences
def create_sequences(data, seq_length):
    xs, ys = [], []
    for i in range(len(data) - seq_length):
        x = data[i:(i + seq_length)]
        y = data[i + seq_length]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

x, y = create_sequences(scaled_prices, sequence_length)

# Split data into training and testing sets
train_size = int(len(x) * 0.8)
x_train, y_train = x[:train_size], y[:train_size]
x_test, y_test = x[train_size:], y[train_size:]

# LSTM model definition
model = Sequential([
    LSTM(50, input_shape=(x_train.shape[1], x_train.shape[2])),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=1)

# Save the model weights
model.save_weights('lstm_model.weights.h5')

# Predict on the test data
predicted_prices = model.predict(x_test)

# Rescale the predictions back to the original price range
predicted_prices = scaler.inverse_transform(predicted_prices)
actual_prices = scaler.inverse_transform(y_test)

# Calculate RMSE
mse = mean_squared_error(actual_prices, predicted_prices)
rmse = np.sqrt(mse)
print("Root Mean Squared Error on Test Set:", rmse)

# Mean Squared Error is 4.544574072617875
# Taking the square root, the predictions were on average $2.13 