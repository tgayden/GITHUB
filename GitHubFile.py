import csv

f = open("7-100_Sales-Records.csv", 'rt')

reader = csv.reader(f)
counter=0
i = 0
total = 0
for row in reader:
    if row[0] == "Europe":
        counter+=1
    if i !=0:
        total+=int(row[8])
    i+=1

print("No of Europe is %d" %counter)
print("total number of items sold is %d" %total)

X = hello world
print (X)
