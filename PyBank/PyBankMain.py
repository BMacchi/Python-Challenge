import os
import csv

#CSV path and output
csvpath = os.path.join('PyBank/Resources/budget_data.csv')
csvpath_output = ('PyBank/Analysis/PyBank.txt')

#Variables
total_months = 0
total_profits = 0
total_profit_loss = 0
previous_profit_loss = None
profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]
profit_loss_changes = []
average_change = 0
changes = []

#CSV Reader
with open(csvpath) as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
      
      # Display number of months
      total_months += 1

      #Display net total profit
      total_profits += int(row["Profit/Losses"])

      #Display average $$ change
      current_profit_loss = int(row["Profit/Losses"])
      if previous_profit_loss is not None:
          change = current_profit_loss - previous_profit_loss

          if change > greatest_increase[1]:
            greatest_increase[1] = change
            greatest_increase[0] = row["Date"]

          if change <  greatest_decrease[1]:
            greatest_decrease[1] = change
            greatest_decrease[0] = row["Date"]

          changes.append(change)
      previous_profit_loss = current_profit_loss
  average_change = sum(changes) / len(changes)
average_change = round(average_change,2)

#Print finalcial results
print("========================================")
print("Financial Analysis")
print("========================================")
print("Total Months:", total_months)
print("Total Profits: $",total_profits)
print("Average change: $", average_change)
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")")
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
print("========================================")


#Print txt Files
with open(csvpath_output, 'w') as file:
  print("========================================", file=file)
  print("Financial Analysis", file=file)
  print("========================================", file=file)
  print("Total Months:", total_months, file=file)
  print("Total Profits: $",total_profits, file=file)
  print("Average change: $", average_change, file=file)
  print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")", file=file)
  print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")", file=file)
  print("========================================", file=file)