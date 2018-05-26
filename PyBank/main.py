import os
import csv

# open the csv file
os.chdir("C:/Users/lovel/LearnPython/python-challenge/PyBank")
# rewrite "budget_data_2.csv' if we want to see the results of the other given dataset
csv_finance=os.path.join('..','PyBank','budget_data_1.csv')
# if we want to read both dataset, we can rewrite line 7 as:
# filename=["budget_data_1.csv","budget_data_2.csv"]
# for budgetdata in filename:
# csv_finance=os.path.join('..','PyBank',budgetdata)
with open(csv_finance,newline='',encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
# skip the headers
    csv_header=next(csvfile)

# calculation
    rev=[]
    rev_change=[]
    date=[]
   
    for row in csvreader:
        rev.append(int(row[1]))
        date.append(row[0])
    
    print("Financial Analysis")
    print("-----------------------")
    print("Total Months:", len(date))
    a="Total Months:" +str(len(date))
    print("Total Revenue:", sum(rev))
    b="Total Revenue:"+str(sum(rev))
    
    for i in range(1,len(rev)):
        rev_change.append(rev[i]-rev[i-1])
        average_change=sum(rev_change)/len(rev_change)
        max_change=max(rev_change)
        max_change_date=str(date[rev_change.index(max(rev_change))])
        min_change=min(rev_change)
        min_change_date=str(date[rev_change.index(min(rev_change))])
        
    print("Average Revenue Change: $", round(average_change))
    c="Average Revenue Change:$"+str(round(average_change))
    
    print("Greatest Increase in Revenue:",max_change_date,"($",max_change,")")
    d="Greatest Increase in Revenue:"+str(max_change_date)+" ($"+str(max_change)+")"
    print("Greatest Decrease in Revenue:",min_change_date,"($",min_change,")")
    e="Greatest Decrease in Revenue:"+str(min_change_date)+" ($"+str(min_change)+")"
    
    output_path=os.path.join('..','PyBank','PyBank.txt')
    with open(output_path,'w',newline='',encoding='utf-8') as f:
        f.write("Financial Analysis")
        f.write("-----------------------")  
        f.write(a)
        f.write(b)
        f.write(c)
        f.write(d)
        f.write(e)

 

        
        
        
        
        