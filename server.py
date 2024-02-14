import csv
from flask import Flask, render_template

app = Flask(__name__)

# Exercise 1:
# Load the CSV in data/ folder a list of dictionaries in the data variable
data = []
with open("data/all_stocks_5yr.csv") as file:
    reader = csv.DictReader(file)
    for line in reader:
        data.append(line)


# Exercise 2:
# Render the list of dictionaries in the index
@app.route("/")
def index():
    row_per_stock = []
    latest = None
    for row in data:
        if row["Name"] != latest:
            latest = row["Name"]
            row_per_stock.append(row)

    return render_template("index.html", data=row_per_stock)


# Exercise 3:
# Create a new route that accepts the ticker of a stock as a path parameter, and render only their:
# - all time highest
# - all time lowest
# - average volume
# - name
# - a table with all the records
@app.route("/stock/<stock>")
def get_stock(stock):
    related_rows = []
    all_time_high = 0
    all_time_low = None
    sum_volume = 0
    for row in data:
        if row["Name"] == stock:
            if float(row["high"]) > all_time_high:
                all_time_high = float(row["high"])
            if float(row["low"]) < all_time_low:
                all_time_high = float(row["low"])
            sum_volume += float(row["volume"])
            related_rows.append(row)
    average_volume = sum_volume / len(related_rows)

    return render_template(
        "stock.html",
        stock=stock,
        data=related_rows,
        average=average_volume,
        all_time_high=all_time_high,
        all_time_low=all_time_low,
    )


app.run(debug=True)
