import csv

with open("table_in.csv", newline="\n") as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)
