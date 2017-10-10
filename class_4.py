# Add the extract_header() code to the initializer and set the header data to self.header.
# Create a variable called nfl_header and set it to the header attribute

class Dataset:
    def __init__(self,data):        # Somehow extract_header() becomes __init__()
        self.header = data[0]
        self.data = data[1:]
        
nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header
