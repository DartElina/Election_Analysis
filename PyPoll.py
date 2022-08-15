#The data we need to retrieve.
#1. total number votes cast
#2. Complete list of candidates
#3. total number of votes per candidate
#4. % of votes each candidate holds
#5. Calculate who won by popular vote
import csv
import os
#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable to a direct ot indirect path to the file 
file_to_save = os.path.join("analysis","election_analysis.txt")
#1. Initialize a total_vote variable to 0 
total_votes = 0 
#2. create candidate list 
candidate_options=[]
#3. create candidate dictionary to count votes by candidate 
candidate_votes={}
#5. Declare the winner, Initialize winning candidate and win counter
winning_candidate=""
winning_count=0
winning_percentage=0
#open the election results and read the file.
with open(file_to_load) as election_data:
    #read the file object with the reader function.
    file_reader= csv.reader(election_data)
    #read the header row
    headers= next(file_reader)
    #print(headers)
    #print each row in the CSV file 
    for row in file_reader:
        #1a.add to total votes counter 
        total_votes+=1
        #2. complete list of candidates
        candidate_name = row[2]
        #If the candidate does not match any exsisting candidate then add to candidate options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #3.b. Begin tracking that candidates vote count
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
#print results
#print(f"{total_votes:,}") 
#print(candidate_votes) 
#4.Determine % votes for each candidate
# first iterate through candidate list  
for candidate_name in candidate_votes:
    #retrieve votes count of candidate
    votes=candidate_votes[candidate_name]
    #calculate % of votes
    vote_percentage=float(votes)/float(total_votes)*100
    #determine if the votes is greater than the winning count 
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name
#to do: print out the winning candidate, vote count and percentage to terminal.
    print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")  
winning_candidate_summary =(
    f"--------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------\n") 
print(winning_candidate_summary)
#Using the open() function with the 'w' mode we will write data to the file. 
with open(file_to_save, "w") as txt_file:
#write data to the file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")



