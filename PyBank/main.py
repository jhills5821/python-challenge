import os
import csv

months = []
pnls=[]

changes = []
losstest = 0
profittest = 0

bank_csv_path = os.path.join(".", "Input File", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

with open(bank_csv_path, newline="") as csvfile:
    csv_read = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_read)
    for row in csv_read:
        month = row[0]
        months.append(month)
        pnl=row[1]
        pnls.append(int(pnl))
    total_months=len(months)
    total = sum(pnls)
    x = len(pnls)-1
    for i in range(x):
        changes_value= pnls[i+1]-pnls[i]
        changes.append(changes_value)
        avgchange=sum(changes)/x
        pnl_variable = changes[i]
        if pnl_variable <0:
            if pnl_variable < losstest:
                losstest = pnl_variable
                lossloc = i
        if pnl_variable >0:
            if pnl_variable > profittest:
                profittest = pnl_variable
                profitloc = i
    print("Total Months: ", total_months)
    print("Total: $", str(total))
    print("Average Change: $", avgchange)
    print("Greatest Increase in Profits: ",months[profitloc+1]," (",changes[profitloc],")")
    print("Greatest Decrease in Profits: ",months[lossloc+1]," (",changes[lossloc],")")