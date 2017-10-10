import csv

f = open('nfl.csv')
csvreader = csv.reader(f)

nfl = list(csvreader)
