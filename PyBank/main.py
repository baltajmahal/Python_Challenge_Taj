import os, csv
from pathlib import Path 
input_file = Path("Resources", "budget_data.csv")

totalmonths = []
totalprofit = []
profitchange = []

with open(input_file,newline="", encoding="utf-8") as budget:
    csvreader = csv.reader(budget,delimiter=",") 
    header = next(csvreader)  
    for row in csvreader: 
        totalmonths.append(row[0])
        totalprofit.append(int(row[1]))
    for i in range(len(totalprofit)-1):
        profitchange.append(totalprofit[i+1]-totalprofit[i])
max_increase_value = max(profitchange)
max_decrease_value = min(profitchange)
max_increase_month = profitchange.index(max(profitchange)) + 1
max_decrease_month = profitchange.index(min(profitchange)) + 1 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(totalmonths)}")
print(f"Total: ${sum(totalprofit)}")
print(f"Average Change: {round(sum(profitchange)/len(profitchange),2)}")
print(f"Greatest Increase in Profits: {totalmonths[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {totalmonths[max_decrease_month]} (${(str(max_decrease_value))})")


output_file = Path("Financial_Analysis_Summary.txt")
with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(totalmonths)}")
    file.write("\n")
    file.write(f"Total: ${sum(totalprofit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profitchange)/len(profitchange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {totalmonths[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {totalmonths[max_decrease_month]} (${(str(max_decrease_value))})")