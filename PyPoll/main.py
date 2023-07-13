import csv

csvpath = '/Users/andreaaguilar/python-challenge/PyPoll/Resources/election_data.csv'

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")