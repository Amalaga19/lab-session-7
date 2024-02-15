from flask import Flask, render_template
import csv

app = Flask(__name__)

# Exercise 1:
# Load the CSV in data/ folder a list of dictionaries in the data variable
data = []

# Open the file and read the data into the data variable
with ("data/all_stocks_5yr.csv", r) as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)
    



# Exercise 2:
# Render the list of dictionaries in the index
@app.route("/")
def index():
    return render_template("index.html", data=data)
    filtered_data = []
    latest_ticker_seen = None
    # Similar to a group by in SQL
    #Iterating through the data and only appending the first row of each ticker
    for row in data:
        if row["ticker"] != latest_ticker_seen:
            filtered_data.append(row)
            latest_ticker_seen = row["ticker"]
    return render_template("index.html", data=filtered_data)

# Exercise 3:
# Create a new route that accepts the ticker of a stock as a path parameter, and render only their:
# - all time highest
# - all time lowest
# - average volume
# - name
# - a table with all the records
@app.route("/stock/<stock>")
def get_stock(stock):
    return "change me"


app.run(debug=True)
