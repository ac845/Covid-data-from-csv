import csv
import copy
import random

cats = {
    "date" : "<empty>",
    "new_cases" : "0",
    "deaths" : "0",
    "recovered" : "0",
    }

for key, value in cats.items():
    print("{} : {}".format(key,value))

myInventoryList = []

with open(r'C:\Users\dci-student\Documents\Python\Py_Projects\Py_Proj_02_Covid data\covid_data.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0
    new_cases = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'Date: {row[0]} New cases: {row[1]}, Deaths: {row[2]}, Recovered: {row[3]}')  
            currentDate = copy.deepcopy(cats)  
            currentDate["date"] = row[0]  
            currentDate["new_cases"] = row[1]
            new_cases = int(row[1]) + new_cases
            currentDate["deaths"] = row[2]  
            currentDate["recovered"] = row[3]  
            myInventoryList.append(currentDate)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

avg_newcases = new_cases / (lineCount -1)
print("\nThe average of new cases per day is: ", avg_newcases)

rand_day = random.choice(myInventoryList)

print("\nThis is the data of a random day:\n")
for key, value in rand_day.items():
    print("{} : {}".format(key,value))
