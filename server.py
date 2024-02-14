from flask import Flask

app = Flask(__name__)

# Exercise 1:
# Load the CSV in data/ folder a list of dictionaries in the data variable
data = []


# Exercise 2:
# Render the list of dictionaries in the index
@app.route("/")
def index():
    return "change this"


# Exercise 3:
# Create a new route that accepts the ticker of a stock as a path parameter, and render only their:
# - all time highest
# - all time lowest
# - average volume
# - name
@app.route("/change_this")
def get_stock():
    return "change this"


app.run(debug=True)
