import os
import csv
budget_csv = os.path.join('..','Resources','budget_data.csv')

with open(budget_csv) as csvfile:
    csvreader = csv.reader(budget_csv, delimiter=',')

    months=[]
    profit_loss=[]
    change =[]
    #total= []
    #total = 0
    #print(csvreader)
    #csv_header = next(csvreader)
    #print(f"CSV Header; {csv_header}")
    #cntr = 0
    #for line in csvreader:
        #cntr +=1
        #if cntr ==87:
            #print(line)
    next(csvreader)

    #data=list(csvreader)
    #rowsx=len(data)

    #profit_loss=0
    #for i in range(0, rows):
        #total=total+int(data[i][1])

    for row in budget_csv:

        months.append(row[0])
        profit_loss.append(int(row[1]))

    total_months=len(months)
        #total += int(row[1])
        

        #months.append(row[0])
        #profit_loss.append(row[1])

#def print_percentages(budget_data):
        #month_date = str(budget_data[0])
        #profit_loss = int(budget_data[1])

#month_total = len(months)
#total= sum(profit_loss)

for i in range(len(profit_loss-1)):
    change.append(profit_loss[i+1]-profit_loss[i])
    change_total = sum(change)

average = round((change_total/(total_months-1)),2)

min_profit = min(change)
max_profit = max(change)
max_month = change.index(max_profit)
min_month = change.index(min_profit) 
loss_month= months[min_month+1]
profit_month= months[max_month+1]

print('Financial Analysis')
print('----------------------------')
print(f'Total Months:{str(month_total)}')
print(f'Total: $ {total}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {profit_month} (${max_profit})')
print(f'Greatest Decrease in Profits: {loss_month} (${min_profit})')

financial_analysis = open("financial_analysis.txt","w")
financial_analysis.write('Financial Analysis\n')
financial_analysis.write('----------------------------\n')
financial_analysis.write(f'Total Months:{str(month_total)}\n')
financial_analysis.write(f'Total: $ {total}\n')
financial_analysis.write(f'Average Change: ${average}\n')
financial_analysis.write(f'Greatest Increase in Profits: {profit_month} (${max_profit})\n')
financial_analysis.write(f'Greatest Decrease in Profits: {loss_month} (${min_profit})\n')

financial_analysis.close()