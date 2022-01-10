import csv

with open('goodreads.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for quote in csv_reader:
        print(quote)
