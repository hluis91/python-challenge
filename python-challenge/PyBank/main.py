#Import Dependencis
import csv
import os


#Files to load   PyBank\Resources\budget_data.csv
file_to_load = os.path.join("PyBank/Resources/budget_data.csv")
#Output    
filetooutput = os.path.join("PyBank/analysis/budget_analysis.txt")

#Beginning Parameters 

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 10000000]
total_net = 0
#Read in csv
with open(file_to_load) as financial_data: 
    reader = csv.reader(financial_data)


#Headrow
    header = next(reader)


#Extract first row
    first_row = next(reader)
    total_months += 1 
    total_net += int(first_row[1])
    previous_net = int(first_row[1])


    for row in reader: 


#Track Total
        total_months += 1
        total_net += int(row[1])


#Track Net CHange
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
#Calculate Greatest Increase
        if net_change>greatest_increase[1]:
            greatest_increase[1] = net_change
            greatest_increase[0] = row[0]



#Greatest decrease
        if net_change<greatest_decrease[1]:
            greatest_decrease[1] = net_change
            greatest_decrease[0] = row[0]



#Average in change
average_change = sum(net_change_list)/len(net_change_list)



#Output Summary
output = (f'''
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${average_change}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})

''')



#Print output tot terminal
print(output)



#Export results to text file
with open(filetooutput, "w") as textfile:
    textfile.write(output) 
