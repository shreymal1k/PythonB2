# write a program that read a csv file and return a list of list

fileName="data.csv"

#function to read csv file and return list
def read_csv(file_name):
    fileHandle=open(file_name,"r")
    data=fileHandle.read()
    fileHandle.close()
   
    
    rows=data.split("\n")
    print(rows)
    
    for i in range(0,len(rows)):
        row=rows[i]
        rows[i]=row.split(",")
    # print("\n")
    # print(data)
    op=rows
    return op # it sholud return list of list
    

receivedData = read_csv(fileName)

print(receivedData[0][2])