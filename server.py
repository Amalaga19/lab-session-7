import csv
from flask import Flask, render_template

app = Flask(__name__)

# Exercise 1:
# Load the CSV in data/ folder a list of dictionaries in the data variable
data = []
with open("data/all_stocks_5yr.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # {"date": "..", "open": ...}
        data.append(row)


page_size = 20


def unique_rows_by_ticker(rows):
    filtered_data = []
    latest_ticker_seen = None
    # this is similar to a group by in SQL
    # iterate over data
    # check if we've already added a row for this company
    #   add it if we didnt
    #   skip if we did
    for row in data:
        if row["Name"] != latest_ticker_seen:
            filtered_data.append(row)
            latest_ticker_seen = row["Name"]
    return filtered_data


# Exercise 2:
# Render the list of dictionaries in the index
@app.route("/")
def index():
    filtered_data = unique_rows_by_ticker(data)
    page = 0

    rows_for_page = filtered_data[page * page_size : (page + 1) * page_size]

    return render_template("index.html", data=rows_for_page, page=0)


@app.route("/page/<int:page>")
def index_page(page):
    filtered_data = unique_rows_by_ticker(data)

    rows_for_page = filtered_data[page * page_size : (page + 1) * page_size]

    return render_template("index.html", data=rows_for_page, page=page)


# Exercise 3:
# Create a new route that accepts the ticker of a stock as a path parameter, and render only their:
# - all time highest
# - all time lowest
# - average volume
# - name
# - a table with all the records
@app.route("/stock/<stock>")
def get_stock(stock):

    relevant_rows = []
    all_time_low = float("inf")
    all_time_high = -float("inf")
    sum_of_volumes = 0

    for row in data:
        if row["Name"] == stock:
            if float(row["low"]) < all_time_low:
                all_time_low = float(row["low"])
            if float(row["high"]) > all_time_high:
                all_time_high = float(row["high"])
            sum_of_volumes += float(row["volume"])
            relevant_rows.append(row)

    volume_avg = sum_of_volumes / len(relevant_rows)

    return render_template(
        "stock.html",
        volume_avg=volume_avg,
        all_time_high=all_time_high,
        all_time_low=all_time_low,
        data=relevant_rows,
    )


app.run(debug=True, port=5555)
