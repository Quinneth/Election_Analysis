# The data we need to retrieve.
# adds dependencies
import csv

#delcares variable for the file to load, connect the 0s.path submodule with joint() function AKA chaining
import os
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    # Read the file object with ther reader function
    #references the file object stored in memory-->pullin dat by iterating through file reader
    #then printing each row, including headers or column names
    file_reader = csv.reader(election_data)
    # print each row in the CSv file
    headers = next(file_reader)
    print(headers)
# 1. The total number of votes cast
## initialize a total vote counter
total_votes = 0

# candidate options and candidate votes

candidate_options =[]
candidate_votes = {}

# 2. A complete list of candidates who received votes

#track winning candidate, vote count, and percentafe

winning_candidate = ""
winning_count = 0
winning_percentage = 0
#open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read header row
    headers = next(file_reader)
    #print each row in the csv file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1
        # get candidate name from each row
        candidate_name = row[2]
        # If candidate does not mathc existing cadidate, and candidate to list
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # and begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
        # add a vote to that cadidate's count
        candidate_votes[candidate_name] += 1
#Save the resutls to text file
with open(file_to_save, "w") as txt_file:
    #print final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)
    for candidate in candidate_votes:
        #retrieve vote count and percentage
        votes = candidate = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
        f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        # save candidate results to text file
        txt_file.write(candidate_results)
        #determine winning vote count, winning percentage, and winning candidate
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
    # print winning candidate's results to the terminal
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)
    # save winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
    




# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote