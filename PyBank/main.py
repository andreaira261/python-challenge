import csv
import os

# File path for csv
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'Resources', 'budget_data.csv')

# Lists to store data for total number of months and net total amount of "Profit/Losses"
months_list = []
total_list = []

# with open as csvfile: 
with open (file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Store months in a list
        months_list.append(row[0])

        # Store "Profit/Losses" from each month in a list
        total_list.append(int(row[1]))

# Caluculate total number of months
months = len(months_list)

# Calculate net total amount of "Profit/Losses" over the entire period 
total = sum(total_list)

# Set initial values for calculating greatest increase and decrease in profits 
greatest_inc = 0
greatest_dec = 0

# List for storing changes in "Profit/Losses" over the entire period
avg_change_list = []

# Loops through each month in dataset 
for i in range(len(total_list)-1):
    # Calculate changes in "Profit/Losses" on month by month basis
    diff = total_list[i+1] - total_list[i]

    # Store changes in "Profit/Losses" on month by month basis in list 
    avg_change_list.append(diff)
    
    # Finds and stores greatest increase in profits 
    if diff > greatest_inc:
        # Greatest increase amount
        greatest_inc = diff
        # Index for month of greatest increase
        greatest_inc_row = i+1
    
    # Finds and stores greatest decrease in profits 
    elif diff < greatest_dec:
        # Greatest decrease amount
        greatest_dec = diff
        # Index for month of greatest decrease
        greatest_dec_row = i+1

# Calculate average of changes in "Profit/Losses" over the entire peiod 
avg_change = round(sum(avg_change_list) / len(avg_change_list),2)

# Print results to terminal
print("Financial Analysis")
print ("-------------------------")

print(f"Total Months: {months}")

print(f"Total: ${total}")

print(f"Average Change: ${avg_change}")

print (f"Greatest Increase in Profits: {months_list[greatest_inc_row]} (${greatest_inc})")

print (f"Greatest Decrease in Profits: {months_list[greatest_dec_row]} (${greatest_dec})")

# Variable and path to output file for printing results to text file     
output_file_path = os.path.join(current_directory, 'Analysis', 'results.txt')

# Print results in text file
with open(output_file_path, "w") as resultfile:
    resultfile.write("Financial Analysis\n")
    resultfile.write("-------------------------\n")

    resultfile.write(f"Total Months: {months}\n")

    resultfile.write(f"Total: ${total}\n")

    resultfile.write(f"Average Change: ${avg_change}\n")

    resultfile.write(f"Greatest Increase in Profits: {months_list[greatest_inc_row]} (${greatest_inc})\n")

    resultfile.write(f"Greatest Decrease in Profits: {months_list[greatest_dec_row]} (${greatest_dec})\n")