import csv

f = open("nfl.csv", 'r')        # Make sure to read the file #
nfl = list(csv.reader(f))

# Define your function here.

def nfl_wins(team):
    count = 0
    for row in nfl:
        if row[2] == team:
            count += 1
    return count
    
cowboys_wins = nfl_wins('Dallas Cowboys')
falcons_wins = nfl_wins('Atlanta Falcons')

# If you wanna count more than one type of data #
