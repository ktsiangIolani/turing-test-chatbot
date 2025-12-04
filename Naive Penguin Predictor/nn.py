# 1_2 Penguins NN
# Name: Tanner Young
# Period: 2


# In this assignment, you'll implement a simple nearest neighbor algorithm to classify penguins
# Make sure this file is in the same directory as penguins.csv

import pandas as pd
import numpy as np

"""
TODO 1: Implement a function called euclidean_distance which takes in two penguins 
and computes the Euclidean distance between them.

Recall that we can compute the Euclidean distance between two points with n-dimensions using the formula:
d(p, q) = sqrt( (p1 - q1)^2 + (p2 - q2)^2 + ... + (pn - qn)^2 )

Compute the distance bewtween two penguins based on their numerical features
(culmen_length_mm, culmen_depth_mm, flipper_length_mm, body_mass_g).

Return the distance as a float.

Hint 1: You can access the features of a penguin using indexing, e.g. penguin1["culmen_length_mm"]
Hint 2:You can use the functions np.square and np.sqrt from the numpy library to help you out.
"""
def euclidean_distance(penguin1, penguin2):
    distance = 0

    distance = np.sqrt(np.square(penguin1["culmen_length_mm"] - penguin2["culmen_length_mm"]) + np.square(penguin1["culmen_depth_mm"] - penguin2["culmen_depth_mm"]) + np.square(penguin1["flipper_length_mm"] - penguin2["flipper_length_mm"]) + np.square(penguin1["body_mass_g"] - penguin2["body_mass_g"]))
    return distance










"""
TODO 2: Using the euclidean_distance function you just wrote, implement a function called nearest_neighbor
which takes in some features about an unknown penguin and matches it to the nearest penguin in our dataset.

Hint: you can loop through each penguin in the dataset and access its features like this:

for index, row in data.iterrows():
    row["culmen_length_mm"] # accesses culmen_length_mm of the current penguin
"""
def nearest_neighbor(unknown_penguin):
    data = pd.read_csv("penguins.csv").dropna()
    closest_row = None
    closest_distance = 1000000000000
    
    for index, row in data.iterrows():
        distance = euclidean_distance(unknown_penguin, row)
        if distance < closest_distance:
            closest_distance = distance
            closest_row = row
        print(closest_distance)
    return closest_row
        



















# To run the test cases below, run this file with `python nn.py`
# --------------- test cases --------------------
print("\n---------- Testing euclidean_distance function:----------\n")

expected = 0.0
print(f"Test case 1: expected distance = {expected}")
penguin1 = pd.Series({'culmen_length_mm': 39.1, 'culmen_depth_mm': 18.7, 'flipper_length_mm': 181.0, 'body_mass_g': 3750.0})
penguin2 = pd.Series({'culmen_length_mm': 39.1, 'culmen_depth_mm': 18.7, 'flipper_length_mm': 181.0, 'body_mass_g': 3750.0})
actual = euclidean_distance(penguin1, penguin2)
assert np.isclose(actual, expected), f"\033[91mExpected {expected} but got {actual}\033[0m"
print("\033[92mTest case 1 passed!\033[0m")

expected = 1250.6301011889966
print(f"Test case 2: expected distance = {expected}")
penguin1 = pd.Series({'culmen_length_mm': 39.1, 'culmen_depth_mm': 18.7, 'flipper_length_mm': 181.0, 'body_mass_g': 3750.0})
penguin2 = pd.Series({'culmen_length_mm': 45.5, 'culmen_depth_mm': 15.0, 'flipper_length_mm': 220.0, 'body_mass_g': 5000.0})
actual = euclidean_distance(penguin1, penguin2)
assert np.isclose(actual, expected), f"\033[91mExpected {expected} but got {actual}\033[0m"
print("\033[92mTest case 2 passed!\033[0m")

expected = 1750.3491223181734
print(f"Test case 3: expected distance = {expected}")
penguin1 = pd.Series({'culmen_length_mm': 46.8, 'culmen_depth_mm': 16.1, 'flipper_length_mm': 215.0, 'body_mass_g': 5500.0})
penguin2 = pd.Series({'culmen_length_mm': 39.1, 'culmen_depth_mm': 18.7, 'flipper_length_mm': 181.0, 'body_mass_g': 3750.0})
actual = euclidean_distance(penguin1, penguin2)
assert np.isclose(actual, expected), f"\033[91mExpected {expected} but got {actual}\033[0m"
print("\033[92mTest case 3 passed!\033[0m")


print("\n---------- Testing nearest_neighbor function:----------\n")

print("Test case 1:")
actual = nearest_neighbor(pd.Series({'culmen_length_mm': 39.2, 'culmen_depth_mm': 18.7, 'flipper_length_mm': 181, 'body_mass_g': 3750}))
expected = pd.Series({'species': 'Adelie', 'island': 'Torgersen', 'culmen_length_mm': 39.1, 'culmen_depth_mm': 18.7, 'flipper_length_mm': 181.0, 'body_mass_g': 3750.0, 'sex':"MALE"})
assert actual.equals(expected), f"Expected {expected} but got {actual}"
print("\033[92mTest case 1 passed!\033[0m")

print("Test case 2:")
actual = nearest_neighbor(pd.Series({'culmen_length_mm': 45.5, 'culmen_depth_mm': 15, 'flipper_length_mm': 220, 'body_mass_g': 5000}))
expected = pd.Series({'species': 'Gentoo', 'island': 'Biscoe', 'culmen_length_mm': 45.5, 'culmen_depth_mm': 15, 'flipper_length_mm': 220.0, 'body_mass_g': 5000.0, 'sex':"MALE"})
assert actual.equals(expected), f"Expected {expected} but got {actual}"
print("\033[92mTest case 2 passed!\033[0m")


# -------------------------- Try it out ---------------------------
"""
Comment out your implementation of predict_penguin in naive_penguins.ipynb and then 
copy and paste the code below into the same code cell to test your nearest neighbor algorithm.

import nn_answers as nn
def predict_penguin(island, culmen_length_mm, culmen_depth_mm, flipper_length_mm, body_mass_g, sex):
    penguin = pd.Series({'culmen_length_mm':culmen_length_mm, 'culmen_depth_mm':culmen_depth_mm, 'flipper_length_mm':flipper_length_mm, 'body_mass_g':body_mass_g})
    predicted = nn.nearest_neighbor(penguin)
    if predicted is None:
        return "Unknown"
    return predicted["species"]
"""