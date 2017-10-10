# Add a data parameter to the __init__() method, and set the value to the self.data attribute.
# Read the data from nfl.csv and set it to the variable nfl_data.
# Make an instance of the class, passing in nfl_data to the __init__() method (when you call Dataset(...)).
# Assign the result to the variable nfl_dataset.
# Use the data attribute to access the underlying data for nfl_dataset and assign the result to the variable dataset_data.

import csv

class Dataset:
    def __init__(self):
        self.type = 'csv'
class Dataset:
    def __init__(self,data):
        self.data = data
        
f = open('nfl.csv','r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data
