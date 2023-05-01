import os
import csv

#CSV reader/writer module
csvpath = os.path.join('Resources/budget_data.csv')
#csvpath_output = ('Python-Challenge/budget_data.txt')

#Variables
total_months = 0
total_profits = 0
previous_profit_loss = None
changes = []

#Display number of months
with open('budget_data.csv') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  for row in reader:
      total_months += 1

#Display net total profit
      total_profits += int(row[1])

#Display average $$ change
      current_profit_loss = int(row[1])
      if previous_profit_loss is not None:
          change = current_profit_loss - previous_profit_loss
          changes.append(change)
      previous_profit_loss = current_profit_loss
  average_change = sum(changes) / len(changes)
  average_change = round(average_change,2)

#Display greatest profit increase over time


#Display greatest profit decrease over time




print("Financial Analysis")
print("----------------------------------")
print("Total Months:", total_months)
print("Total Profits: $",total_profits)
print("Average change: $", average_change)

#with open(csvpath_output, 'w') as txt_file:
#    txt_file.write("Total Months:", total_months)
#    txt_file.write("Total Profits: $",total_profits)
#    txt_file.write("Average change: $", average_change)