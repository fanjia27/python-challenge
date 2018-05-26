import os
import csv

os.chdir("C:/Users/lovel/LearnPython/python-challenge/PyPoll")
#rewrite 'election_data_1.csv' if we need to see the results of the other given dataset
csv_election=os.path.join('..','PyPoll','election_data_1.csv')
with open(csv_election,newline='',encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
# skip the headers
    csv_header=next(csvfile)
    
    vote_cast=[]
    candidate=[]
    
    print("Election Results")
    print("-----------------------")
    
    for row in csvreader:
        vote_cast.append(row[0])
        candidate.append(row[2])
    print("Total Votes:",len(vote_cast))
    print("-----------------------")
    
    #find out all candidate:
    candidate_list=list(set(candidate))
    # print(candidate_list)
    
    dic1={g:0 for g in candidate_list}
    
    #calculate the total number of votes each candidate won
    for i in candidate:
        for j in candidate_list:
            if i == j:
                dic1[j]+=1
    #print(dic1)
    
    #calculate the percentage of votes each candidate won
    for i in dic1:
        print(i,":",int(dic1[i])/len(vote_cast)*100,"%"," (",dic1[i],")",sep='')
    print("-----------------------")
    
    #find the winner   
    max=0
    winner=i
    for i in dic1:
        if (dic1[i]>max):
            max=dic1[i]
            winner=i
    print("Winner:",winner)
    a=("Winner:"+str(winner))
    
    
    output_path=os.path.join('..','PyPoll','PyPoll.txt')
    with open(output_path,'w',newline='',encoding='utf-8') as f:
        f.write("Election Results")
        f.write("-----------------------")
        f.write("Total Votes:"+str(len(vote_cast)))
        for i in dic1:
            f.write(i+":"+str(int(dic1[i])/len(vote_cast)*100)+"%"+" ("+str(dic1[i])+")")
        f.write("-----------------------")
        f.write(a)
        
        
      


            
    
    
    
    
        
    
    
    
         

    
    

        
    
            
        
        
        
        
