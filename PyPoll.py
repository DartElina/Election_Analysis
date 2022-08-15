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
#open the election results and read the file.
with open(file_to_load) as election_data:
    #read the file object with the reader function.
    file_reader= csv.reader(election_data)
    #Print header row
    headers= next(file_reader)
    print(headers)
        
#create a file name variable to a direct ot indirect path to the file 
file_to_save = os.path.join("analysis","election_analysis.txt")
#Using the open() function with the 'w' mode we will write data to the file. 
with open(file_to_save, "w") as txt_file:
#write data to the file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")



