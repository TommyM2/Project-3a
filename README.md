# Stock Data Visualizer

This project is a web application built using Flask that allows users to visualize stock data over different time periods (daily, weekly, or monthly). The data is retrieved from the Alpha Vantage API and displayed as either a line or bar chart.

## Features

- Users can enter a stock symbol to retrieve stock data.
- The user can select the time series (Daily, Weekly, or Monthly).
- The user can choose the type of chart (Line or Bar).
- Users can specify a start and end date for the stock data they want to visualize.
- Displays the chart dynamically based on user input.

## Requirements

Before running the application, ensure you have the required Python libraries installed. You can install them using pip:

```bash
pip install -r requirements.txt
The required libraries are:

Flask==2.3.3

requests==2.31.0

pygal==3.0.4

Setup
Clone this repository:

git clone https://github.com/GMast3rs/Project_3-_Stock_Data_Visualizer.git
cd Project_3-_Stock_Data_Visualizer
Install the necessary dependencies:

pip install -r requirements.txt

To run the application, use:

python app.py

The app will be available at http://127.0.0.1:5000/.

GitHub Repository
You can access the complete project code in the GitHub repository:
Project_3_Stock_Data_Visualizer

Features
Stock Symbol
Input the stock symbol of any publicly traded company (e.g., "AAPL" for Apple, "GOOGL" for Google).

Time Series
Choose between three different time series options:

Daily: Daily stock prices.

Weekly: Weekly stock prices.

Monthly: Monthly stock prices.

Chart Type
Choose between two types of charts to display:

Line: A line chart representing stock prices over time.

Bar: A bar chart representing stock prices over time.

Date Range
Input the start and end dates for which you want to see the stock data. The dates should be in the YYYY-MM-DD format.

API Key
In order to use the Alpha Vantage API, you need to get a free API key. You can obtain it from the Alpha Vantage API.

How to Use Your API Key:
Get your free API key from Alpha Vantage.

Open app.py in your project folder.

Find the line that says:

python
Copy
Edit
api_key = "your_api_key_here"
Replace "your_api_key_here" with your actual API key.

Notes
This application uses the Alpha Vantage API to fetch stock data, so there might be rate limits for requests (check Alpha Vantage's documentation for more details).

The chart is generated using the Pygal library and displayed in the browser.
