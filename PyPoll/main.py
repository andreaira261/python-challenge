import csv

csvpath = '/Users/andreaaguilar/python-challenge/PyPoll/Resources/election_data.csv'

id_list = []
candidates = []

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        id_list.append(row[0])

        candidates.append(row[2])

total_votes = len(id_list)

candidates_list = []
for i in candidates:
    if i not in candidates_list:
        candidates_list.append(i)

candidates_votes = []
for i in range(len(candidates_list)):
    votes = candidates.count(candidates_list[i])
    candidates_votes.append(votes)

vote_percent = []
for i in range(len(candidates_list)):
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
    

    





