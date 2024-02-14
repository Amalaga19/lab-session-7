from flask import Flask

app = Flask(__name__)

# Exercise 1:
# Load the CSV in data/ folder a list of dictionaries in the data variable
data = []


# Exercise 2:
# Render the list of dictionaries in the index
@app.route("/")
def index():
    return "change me"


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
