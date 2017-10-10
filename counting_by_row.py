# First, import the CSV module
import csv

# Then, open our file in `r` mode

f = open("nfl.csv", "r")

# Use the csv module to read the file, and convert the result
# to a list

nfl = list(csv.reader(f))

# Start our count at 0

patriots_wins = 0

# Loop through our data set, counting the rows with "New England Patriots"
# as the winner

for row in nfl:
    if row[2] == "New England Patriots":
        patriots_wins += 1
