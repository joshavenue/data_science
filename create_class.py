# Create a class called Dataset.
# Inside the class, create a type attribute. Assign the value "csv" to it.
# Create an instance of the Dataset class, and assign it to the variable dataset.
# Print the type attribute of the dataset instance.

class Dataset:
    def __init__(self):
        self.type = 'csv'
        
dataset = Dataset()
print(dataset.type)
        
