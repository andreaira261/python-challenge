import csv
import os

# File path for csv
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'Resources', 'election_data.csv')

# List to store data for total number of votes cast
candidates = []

# with open as csvfile: 
with open (file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Store header
    csv_header = next(csvreader)

    for row in csvreader: 
        # Store candidates row in a list
        candidates.append(row[2])

# Calculate total number of votes cast
total_votes = len(candidates)

# List to store candidates who received votes 
candidates_list = []

for i in candidates:
    # Stores unique candidates in list 
    if i not in candidates_list:
        candidates_list.append(i)

# Lists to store data for total number of votes each candidate won and percentage of votes each candidate won 
candidates_votes = []
vote_percent = []

# Loops through range of number of unique candidates
for i in range(len(candidates_list)):
    # Counts number of times each candidate received by matching names in 'candidates_list'
    votes = candidates.count(candidates_list[i])
    
    # Stores total number of votes for each candidate
    candidates_votes.append(votes)

    # Calculates percentage of votes each candidate won
    percent = round((candidates_votes[i] / total_votes)*100,3)
    
    # Stores percentage of votes for each candidate
    vote_percent.append(percent)

# Index for candidate who received the most number of votes 
winner_index = (candidates_votes.index(max(candidates_votes)))

# Print results to terminal
print ("Election Results")
print ("-------------------------")

print (f"Total Votes: {total_votes}")
print ("-------------------------")

for i in range(len(candidates_list)):
    print(f"{candidates_list[i]}: {vote_percent[i]}% ({candidates_votes[i]})")
print ("-------------------------")

print (f"Winner: {candidates_list[winner_index]}")

print ("-------------------------")

# Variable and path to output file for printing results to text file     
output_file_path = os.path.join(current_directory, 'Analysis', 'results.txt')

# Print results in text file
with open(output_file_path, "w") as resultfile:
    resultfile.write("Election Results\n")
    resultfile.write("-------------------------\n")

    resultfile.write(f"Total Votes: {total_votes}\n")
    resultfile.write("-------------------------\n")

    for i in range(len(candidates_list)):
        resultfile.write(f"{candidates_list[i]}: {vote_percent[i]}% ({candidates_votes[i]})\n")
    resultfile.write("-------------------------\n")

    resultfile.write(f"Winner: {candidates_list[winner_index]}\n")
    resultfile.write("-------------------------\n")