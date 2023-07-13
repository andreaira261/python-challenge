import csv

csvpath = '/Users/andreaaguilar/python-challenge/PyBank/Resources/budget_data.csv'

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    csvreader_list = list(csvreader)

    print("Total Months: " + str(len(csvreader_list)))