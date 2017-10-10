class Dataset:
    def __init__(self,data):
        self.header = data[0]
        self.data = data[1:]
        
    def column(self,label):   # Add a method named column that takes in a label argument, finds the index of the header, and returns a list of the column data.
        if label not in self.header:
            return None       # If the label is not in the header, you should return None.
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
                
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')      # Create a variable called year_column and set it to the return value of column('year').
player_column = nfl_dataset.column('player')  # Create a variable called player_column and set it to the return value of column('player').
