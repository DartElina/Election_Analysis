# Election_Analysis

## Overview of Election Audit: 
We were provided with raw data containing election data from Colorado. Our code read the csv that held the data and counted the total vote count, the turnout per county, and tallied the results of each candidate, as well as finding the winning results. This code is useful for easily and reliably counting hundreds of thousands of lines of data in seconds.

## Election-Audit Results: 
### Total Votes: 369,711
### County Votes:
  - Denver: 82.8% (306,055)
  - Jefferson: 10.5% (38,855)
  - Arapahoe: 6.7% (24,801) 
### Denver had the highest turnout with 306,055 votes.
### Candidate Breakdown:
   - Diana DeGette: 73.8% (272,892)
   - Charles Casper Stockham: 23.0% (85,213)
   - Raymon Anthony Doane: 3.1% (11,606)
### Winning Results:
  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%

## Election-Audit Summary: 
This code can be used to tally election results in any county. Please be aware that the code has been indexed to the candidate names and the county based on the order that this info was saved in the provided csv. Code should be edited and indexed to the new csv for each election count. Line 9 needs to be edited to the path of the new csv. Lines 48 and 51 must be indexed depending on how data is stored in the new file. Remaining code should work with out further edits. 

