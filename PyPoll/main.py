import csv
import os

#csvpath = '/Users/andreaaguilar/python-challenge/PyPoll/Resources/election_data.csv'
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'Resources', 'election_data.csv')

candidates = []

with open (file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader: 

        candidates.append(row[2])

total_votes = len(candidates)

candidates_list = []
for i in candidates:
    if i not in candidates_list:
        candidates_list.append(i)

candidates_votes = []
vote_percent = []
for i in range(len(candidates_list)):
    votes = candidates.count(candidates_list[i])
    candidates_votes.append(votes)
    percent = round((candidates_votes[i] / total_votes)*100,3)
    vote_percent.append(percent)
 
winner_index = (candidates_votes.index(max(candidates_votes)))

print ("Election Results")
print ("-------------------------")

print (f"Total Votes: {total_votes}")
print ("-------------------------")

for i in range(len(candidates_list)):
    print(f"{candidates_list[i]}: {vote_percent[i]}% ({candidates_votes[i]})")
print ("-------------------------")

print (f"Winner: {candidates_list[winner_index]}")

print ("-------------------------")
    
output_file = '/Users/andreaaguilar/python-challenge/PyPoll/Analysis/results.txt'

with open(output_file, "w") as resultfile:
    resultfile.write("Election Results\n")
    resultfile.write("-------------------------\n")

    resultfile.write(f"Total Votes: {total_votes}\n")
    resultfile.write("-------------------------\n")

    for i in range(len(candidates_list)):
        resultfile.write(f"{candidates_list[i]}: {vote_percent[i]}% ({candidates_votes[i]})\n")
    resultfile.write("-------------------------\n")

    resultfile.write(f"Winner: {candidates_list[winner_index]}\n")
    resultfile.write("-------------------------\n")