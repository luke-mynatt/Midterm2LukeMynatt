import yfinance as yf
import datetime

# Set the ticker symbol for the stock
ticker_symbol = 'AAPL'

# Set the end date to today's date and start date to five years ago
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=5*365)

# Download the historical data for the past five years
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Save the data to a CSV file
data.to_csv('AAPL_stock_data.csv')

print("Data saved to 'AAPL_stock_data.csv'")
