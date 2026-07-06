#working on csv file
import csv
with open("student.csv","r")as f:
    data=csv.reader(f)
    print(data)
    for row in data:
        print(row)
       
#skip a header line 
import csv
with open("student.csv","r")as f:
    data=csv.reader(f)
    print(data)
    next(data)
    for row in data:
        print(row)
