# Lab: creating a dynamic website

## Exercise 1:
Load the CSV in data/ folder a list of dictionaries in the data variable

## Exercise 2:
Render a row per stock in the index page.

## Exercise 3:
Create a new route that accepts the ticker of a stock as a path parameter, and render only their:
- all time highest
- all time lowest
- average volume
- name

## Exercise 4:

Modify the second exercise, and add pagination.  For this you'll need to:
1. render only N rows at a time
2. capture a `page` parameter from path
3. start reading at the row `N * page`
4. add buttons for next and previous page
