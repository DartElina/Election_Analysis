print("Hello World")

counties_dict={'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")
    
#for county, voters in counties_dict.items():
 #   print(f"{county} county has {voters:,} registered voters")

voting_data=[]
voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
voting_data.append({'county':'Denver', 'registered_voters': 463353})
voting_data.append({'county':'Jefferson', 'registered_voters':432438})
print(voting_data)
#candidate_votes =int(input("How many votes did the candidate get in the election?"))
#total_votes = int(input("What is the total number of votes in the election?"))
#message_to_candidate = (
 #   f"You recieved {candidate_votes} votes. "
  #  f"The total number of votes in the election was {total_votes}. "
   # f"You recieved {candidate_votes/total_votes*100}% of the total votes.")
#print(message_to_candidate)