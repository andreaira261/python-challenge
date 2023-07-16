import csv
import os

#csvpath = '/Users/andreaaguilar/python-challenge/PyBank/Resources/budget_data.csv'
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'Resources', 'budget_data.csv')

months_list = []
total_list = []

with open (file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        months_list.append(row[0])

        total_list.append(int(row[1]))

months = len(months_list)
total = sum(total_list)

greatest_inc = 0
greatest_dec = 0
avg_change_list = []

for i in range(len(total_list)-1):
    diff = total_list[i+1] - total_list[i]
    avg_change_list.append(diff)
    if diff > greatest_inc:
        greatest_inc = diff
        greatest_inc_row = i+1
    elif diff < greatest_dec:
        greatest_dec = diff
        greatest_dec_row = i+1

avg_change = round(sum(avg_change_list) / len(avg_change_list),2)

print("Financial Analysis")
print ("-------------------------")

print(f"Total Months: {months}")

print(f"Total: ${total}")

print(f"Average Change: ${avg_change}")

print (f"Greatest Increase in Profits: {months_list[greatest_inc_row]} (${greatest_inc})")

print (f"Greatest Decrease in Profits: {months_list[greatest_dec_row]} (${greatest_dec})")

output_file = "/Users/andreaaguilar/python-challenge/PyBank/Analysis/results.txt"

with open(output_file, "w") as resultfile:
    resultfile.write("Financial Analysis\n")
    resultfile.write("-------------------------\n")

    resultfile.write(f"Total Months: {months}\n")

    resultfile.write(f"Total: ${total}\n")

    resultfile.write(f"Average Change: ${avg_change}\n")

    resultfile.write(f"Greatest Increase in Profits: {months_list[greatest_inc_row]} (${greatest_inc})\n")

    resultfile.write(f"Greatest Decrease in Profits: {months_list[greatest_dec_row]} (${greatest_dec})\n")
