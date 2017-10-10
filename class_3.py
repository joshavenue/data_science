# Add an instance method print_data() that takes in a num_rows argument.
# This method should print out data up to the given amount of rows.
# Create an instance of the Dataset class and initialize with the nfl_data. nfl_data is already loaded for you.
# Assign it to the variable nfl_dataset.
# Call the print_data method, setting the num_rows parameter to 5.

class Dataset:
    def __init__(self, data):
        self.data = data
    
    def print_data(self, num_rows):
        print(self.data[:num_rows])


nfl_dataset = Dataset(nfl_data)
nfl_dataset.print_data(5)
