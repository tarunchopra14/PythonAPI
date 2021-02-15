import os
import csv

#create paths

filepath = os.path.join('..', "Resources", "election_data.csv")
output_path = os.path.join('..',"analysis","output.txt")

#to read election data first open csvfile.

with open(filepath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    #skip header to read data.
    csv_header = next(csvfile)
    print(f'"header: {csv_header}')

    # To count total no. of votes, taking variable as 'total_vote_cast'
    # To find the complete list of candidates who received votes,
    # we are using 'set', to store candidates name variable as 'candidate_name'.
    # Now create dictionary in which candidate_name as key for votes and count of votes for them as value
    # for this dictionary variable as 'candidate_name_dictionary'

    total_vote_cast = 0
    candidates_name = set()
    candidate_name_dictionary = {}
    


    for vote_row in reader:
        total_vote_cast = total_vote_cast + 1
        
        # Taking temparory variable to hold vote counts 'temp_total_vote' 
        # Using 'if' condition to check whether candidate name is present in the set, 
        # use nested if to check whether its exists in dicytionary or not 
        # If not 'add' in the dictionary and give '1' vote to the new candidate in dictionary.

        temp_total_vote = 0

        candidates_name.add(vote_row[2])

        if vote_row[2] in candidates_name:

            if vote_row[2] in candidate_name_dictionary:

                temp_total_vote = int(candidate_name_dictionary[vote_row[2]])

                temp_total_vote += 1

                candidate_name_dictionary[vote_row[2]] = str(temp_total_vote)

            else:

                candidate_name_dictionary[vote_row[2]] = 1

    
    percentage_of_votes = 0.0

    temp_vote = 0

    vote_percentage_dictionary ={}

    winner = ""

    winner_vote_percent = 0.0



    # for loop for set to access candidate name 
    # to find the total number of vote recived by each candidate
    # x is candidate name in set
    # use dictionary to get the value as total votes using Key as candidate name from set
    
    for x in candidates_name:
        
        temp_vote = int(candidate_name_dictionary[x])

        percentage_of_votes = (temp_vote/total_vote_cast)*100

        percentage_of_votes_round = round(percentage_of_votes, 2)

        vote_percentage_dictionary[x] = percentage_of_votes_round
        
        if percentage_of_votes_round >= winner_vote_percent:

            winner_vote_percent = percentage_of_votes_round

            winner_vote_percent_round = round(winner_vote_percent, 2)

            winner = x

    #print(candidate_name_dictionary["Khan"])
    #print(candidate_name_dictionary["O'Tooley"])
    #print(candidate_name_dictionary["Li"])
    #print(candidate_name_dictionary["Correy"])

    #for percentage of votes
    #print(vote_percentage_dictionary["Khan"])
    #print(vote_percentage_dictionary["O'Tooley"])
    #print(vote_percentage_dictionary["Li"])
    #print(vote_percentage_dictionary["Correy"])

    #print(candidates_name)
    # print(candidate_name_dictionary)
    # print(vote_percentage_dictionary)
    # print(winner_vote_percent_round)   
     
    print('\n==================================================\n')
    print("\n Election Results \n")
    print('\n==================================================\n')
    print("\nTotal Votes: "+" "+ str(total_vote_cast)+"\n")
    print('\n----------------------------------------------------\n')    

    for cand_name in candidate_name_dictionary:
        print("\n"+cand_name+":"+" "+str(vote_percentage_dictionary[cand_name])+"%"+"  ("+str(candidate_name_dictionary[cand_name])+")"+"\n")

    print('\n----------------------------------------------------\n')
    print("\n"+"Winner: "+ winner+"\n")
    print('\n----------------------------------------------------\n')

   
  
  

    

    #export outlet to txt file

    with open(output_path, 'w', newline= '') as txt_output_file:
        
        txt_output_file.write('\n==================================================\n')

        txt_output_file.write("\n Election Results \n")

        txt_output_file.write('\n==================================================\n')

        

        txt_output_file.write("\nTotal Votes: "+" "+ str(total_vote_cast)+"\n")

        txt_output_file.write('\n----------------------------------------------------\n')    

        for cand_name in candidate_name_dictionary:
            txt_output_file.write("\n"+cand_name+":"+" "+str(vote_percentage_dictionary[cand_name])+"%"+"  ("+str(candidate_name_dictionary[cand_name])+")"+"\n")

        txt_output_file.write('\n----------------------------------------------------\n')

        txt_output_file.write("\n"+"Winner: "+ winner+"\n")

        txt_output_file.write('\n----------------------------------------------------\n')


    
    
