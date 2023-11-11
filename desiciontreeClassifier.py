#import needed libraries
from csv import reader
import math
#load csv file as dataset
def load_dataset(filename):
    #function will return the dataset,list containing all the attributes value(column names),list contain all columns unique values,number yes and no count
    dataset=[]
    with open(filename,'r') as file:    #open the file in read format
        csv_reader=reader(file)         #read the file
        for row in csv_reader:
            if not row:                 #if the row contain no record discard it
                continue
            dataset.append(row)         #append all the rows into dataset
    attr_list=dataset[0]                #first row in csv file denote attributes name
    del dataset[0]                      #delete the attributes name from the dataset
    #unique values for each attribute
    attribute_unique=[]
    for i in range(len(dataset[0])):      #loop runs through all the column
        col=[row[i] for row in dataset]  #get one column values fully
        set_list=list(set(col))            #get unique values from the column
        if(i==len(dataset[0])-1):          #if that column is last column(label column)
            #the string values like yes,no should be in same case as that of in csv file
            yes=col.count("yes")           #count the number of yes and number of no values
            no=col.count("no")
        attribute_unique.append(set_list)   #append the unique values of single column as list into main list that contain all columns unique values
    return dataset,attr_list,attribute_unique,yes,no 

def entropy(no_yes,no_no,tot):      #function that calculate entropy
    #formula=-p_postive*log2(p_positive)-p_neagtive*log2(p_neagtive)
    p_yes=no_yes/tot                
    p_no=no_no/tot
    return round(-p_yes*math.log2(p_yes)-p_no*math.log2(p_no),4) #round the values into 4 digits 

def numOfYesNoClac(data,attr_num,unique_vals): 
    #function will return a table that consists of uniques values of a column and count of those values
    #function parameters are dataset,column number,list of unique values of the column
    y="yes"     #the string values like yes,no should be in same case as that of in csv file
    l1=[] 
    for i in range(len(unique_vals)): #for each unique value
        l1.append([unique_vals[i],0,0]) #our table list will consists of lists in formant [uniquevalue,yescount,nocount]
    for i in range(len(data)):
        ind=unique_vals.index(data[i][attr_num]) #this will get the index of the table value by matching the column value with its respective unique value
        if(y in data[i]):           #increment yescount in list if the column value's respective label is yes
            l1[ind][1]=l1[ind][1]+1
        else:
            l1[ind][2]=l1[ind][2]+1 #increment nocount in list if the column value's respective label is no
    return l1 #return the list

filename='Buy_Computer.csv'
tennis_data,attributeList,attributeUniqueValue,yescnt,nocnt=load_dataset(filename)
Entropy_tot=entropy(yescnt,nocnt,yescnt+nocnt) #calculate the total entropy using label column
numRows=len(tennis_data) #total length of the dataset
print("Yes:",yescnt)
print("No:",nocnt)
print("Entroy(",attributeList[len(attributeList)-1],"):",Entropy_tot) 
cnt=0
gain_list=[]
for i in range(len(tennis_data[0])-1): #for each column except final label column
    info=0
    entropy_list=[]
    print("-----------",attributeList[i],"--------------") #print the column name
    table_attr=numOfYesNoClac(tennis_data,i,attributeUniqueValue[i]) #calculate the attribute table
    print("Attribute values Yes\tNo")
    for j in range(len(table_attr)): #for each unique values in table calculate entropy
        yes=table_attr[j][1]
        no=table_attr[j][2]
        tot=table_attr[j][1]+table_attr[j][2]
        if(table_attr[j][1]==0 or table_attr[j][2]==0): #in any unique value if yescount or nocount is zero entropy will be zero
            en=0
        else:
            en=entropy(yes,no,tot)  
        entropy_list.append(en)     #append the entropy values of paticular column table
        print(table_attr[j][0],"\t\t",table_attr[j][1],"\t",table_attr[j][2]) #print the unique value and respective yes and no count
        info=info+tot/numRows*en #calculate total entropy of that column (refer notes for formula)
    for k in range(len(entropy_list)):
        print("Entropy(",table_attr[k][0],")=",entropy_list[k]) #print entropy of each unique value in column
    gain=round(Entropy_tot-info,4)  #calculate the total gain of the column
    gain_list.append(gain)  #append it in gain list
    print("Info(before split):",Entropy_tot)
    print("Total Entropy(",attributeList[i],")=",round(info,4))
    print("Gain(",attributeList[i],")=",gain)
    print("")  
    
print("--------------Gain--------------")
print("Attributes\t Information Gain")
for i in range(len(attributeList)-1):
    print(attributeList[i],"\t",gain_list[i]) #print column name and their respective gain value
print("The root split node with highest information gain node is ",attributeList[gain_list.index(max(gain_list))]) #choose column with high gain value