#open pyBank csv file

import os
import csv

#create file folder path to be used for reading file
filepath = os.path.join('..', "Resources", "budget_data.csv")
bank_output_path = os.path.join('..',"analysis","output.txt")

#to read data into directory
#with is used to manage file close on its own
with open(filepath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    #command to skip header
    csv_header = next(csvfile)
    print(f'"Header: {csv_header}')
    
    total_month = 0
    total_amount = 0
    change_month_profit_loss = 0.0
    previous_month_profit_loss = 0.0
    diff_of_each_month_revenue = []
    dictionary_new_profit_loss = {}
    
# loop through each row and keep on adding change_month_profit_loss in the list diff_of_each_month_revenue
# we are using previous_month_profit_loss variable to hold value for previous month
#  We are using dictionary_new_profit_loss to hold change_month_profit_loss as key 
# and Month for which its calculated as Value
    for month_row in reader:
        total_month += 1
        total_amount += (float(month_row[1]))

        change_month_profit_loss = float(month_row[1]) - previous_month_profit_loss
        
        diff_of_each_month_revenue.append(change_month_profit_loss)

        previous_month_profit_loss = float(month_row[1])

        dictionary_new_profit_loss[change_month_profit_loss] = month_row[0]

           

greatest_incr_profit = 0.0
greatest_decr_losses = 0.0
new_total_profit_loss = 0.0

average_change_profit_loss = 0.0

#Now loop through the list diff_of_each_month_revenue to calculate 3 things 
# new_total_profit_loss
# greatest_incr_profit
# greatest_decr_losses
for i in range(len(diff_of_each_month_revenue)):
    if i==0:
        greatest_incr_profit=diff_of_each_month_revenue[i]
        greatest_decr_losses=diff_of_each_month_revenue[i]            
        continue

    if diff_of_each_month_revenue[i] >= greatest_incr_profit:
        greatest_incr_profit = diff_of_each_month_revenue[i]

    if diff_of_each_month_revenue[i] <= greatest_decr_losses:
        greatest_decr_losses = diff_of_each_month_revenue[i]


    new_total_profit_loss += diff_of_each_month_revenue[i]

#get average change profit loss using the variable new_total_profit_loss calculated above
average_change_profit_loss = new_total_profit_loss/(total_month-1)
avg_change = round(average_change_profit_loss,2)

# get value of Month with Greatest increase from dictionary
x = dictionary_new_profit_loss[greatest_incr_profit]

# get value of Month with Greatest decrease from dictionary
y = dictionary_new_profit_loss[greatest_decr_losses]



print('==================================================')
    
print(" Financial Analysis")

print('==================================================')

print("Total months : ", total_month)

print("Total amount : "+"$"+ str(total_amount))

print("Avgrage change : "+"$"+ str(avg_change))

print("greatest increase in profit : "+ str(x) + " " +"("+"$"+ str(greatest_incr_profit)+")")

print("greatest decrese in losses : "+ str(y) + " " +"("+ "$"+str(greatest_decr_losses)+")")

#export outlet to txt file

with open(bank_output_path, 'w', newline= '') as txt_output_file:

    txt_output_file.write('\n==================================================\n')

    txt_output_file.write("\n Financial Analysis \n")

    txt_output_file.write('\n==================================================\n')



    txt_output_file.write("\n"+"Total months : "+ str(total_month)+"\n")

    txt_output_file.write("\n"+"Total amount : "+"$"+ str(total_amount)+ "\n")    

    txt_output_file.write("\nAvgrage change : "+"$"+ str(avg_change)+"\n")

    txt_output_file.write("\ngreatest increase in profit : "+ str(x) + " " +"("+"$"+ str(greatest_incr_profit)+")\n")

    txt_output_file.write("\ngreatest decrese in losses : "+ str(y) + " " +"("+ "$"+str(greatest_decr_losses)+")\n")

    txt_output_file.write('\n==================================================\n')
    


        


        


