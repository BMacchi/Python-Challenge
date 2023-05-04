import os
import csv

#CSV path and output
csvpath = os.path.join('PyPoll/Resources/election_data.csv') 
csvpath_output = ('PyPoll/Analysis/PyPoll.txt')

#CSV Reader
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

    # Calculate the total number of votes cast
total_votes = len(data)

# Create a set of all unique candidates
candidates = set()
for row in data:
    candidates.add(row["Candidate"])

# Create a dictionary to store each candidate's vote count
candidate_votes = {}

# Loop through the data and tally up the votes for each candidate
for row in data:
    candidate = row["Candidate"]
    if candidate not in candidate_votes:
        candidate_votes[candidate] = 0
    candidate_votes[candidate] += 1

# Calculate the percentage of votes each candidate won and print the results
for candidate, votes in candidate_votes.items():
    vote_percentage = votes / total_votes * 100

# Determine the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_votes:
    vote_percentage = round(candidate_votes[candidate] / total_votes * 100, 3)
    votes = candidate_votes[candidate]
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Create txt file
with open(csvpath_output, 'w') as file:
    print("Election Results", file=file)
    print("-------------------------", file=file)
    print(f"Total Votes: {total_votes}", file=file)
    print("-------------------------", file=file)
    for candidate in candidate_votes:
        vote_percentage = round(candidate_votes[candidate] / total_votes * 100, 3)
        votes = candidate_votes[candidate]
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})", file=file)
    print("-------------------------", file=file)
    print(f"Winner: {winner}", file=file)
    print("-------------------------", file=file)
