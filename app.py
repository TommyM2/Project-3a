import os
import csv
from flask import Flask, render_template, request
import requests
import pygal
from datetime import datetime

app = Flask(__name__)

# Ensure the static folder is available
app.config['STATIC_FOLDER'] = os.path.join(os.getcwd(), 'static')

# Alpha Vantage API key from environment variable
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

# Load stock symbols from the CSV (you can adjust the path to where you extract them)
def load_stock_symbols():
    stock_symbols = []
    try:
        with open('stocks.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header row
            for row in csvreader:
                stock_symbols.append(row[0])  # Assuming stock symbol is the first column
    except Exception as e:
        print(f"Error loading CSV: {e}")
    return stock_symbols

def fetch_stock_data(symbol, series, start_date, end_date):
    if not ALPHA_VANTAGE_API_KEY:
        return None, "Alpha Vantage API key is missing."
    
    if series == 'Daily':
        function = 'TIME_SERIES_DAILY'
    elif series == 'Weekly':
        function = 'TIME_SERIES_WEEKLY'
    else:
        function = 'TIME_SERIES_MONTHLY'

    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return None, "Error fetching data from Alpha Vantage."
    
    data = response.json()
    time_series = data.get(f"Time Series ({series})", {})

    filtered_data = {}
    for date_str, values in time_series.items():
        date = datetime.strptime(date_str, '%Y-%m-%d')
        if start_date <= date <= end_date:
            filtered_data[date_str] = values

    if not filtered_data:
        return None, "No data found for the given date range."

    return filtered_data, None

def generate_chart(data, series):
    chart = pygal.Line() if series == "Daily" else pygal.Bar()
    chart.title = f"{series} Stock Data"
    
    for date_str, values in data.items():
        chart.add(date_str, [float(values['4. close'])])

    chart_uri = f"static/{data}_chart.svg"  # Change to a dynamic path
    chart.render(outfile=chart_uri)
    return chart_uri

@app.route("/", methods=["GET", "POST"])
def index():
    chart_uri = None
    error = None
    stocks = load_stock_symbols()  # Load the symbols from the CSV file

    if request.method == "POST":
        symbol = request.form.get("symbol")
        series = request.form.get("series")
        start_date = datetime.strptime(request.form.get("start"), "%Y-%m-%d")
        end_date = datetime.strptime(request.form.get("end"), "%Y-%m-%d")

        if end_date < start_date:
            error = "End date must be after the start date."
        else:
            stock_data, error = fetch_stock_data(symbol, series, start_date, end_date)
            if stock_data:
                chart_uri = generate_chart(stock_data, series)
    
    return render_template("index.html", chart_uri=chart_uri, error=error, stocks=stocks)

if __name__ == "__main__":
    app.run(debug=True)
