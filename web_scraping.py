# load the libraries
from bs4 import BeautifulSoup
import requests
import csv

with open('Popular_Quotes.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

csv_file = open('goodreads.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['quote'])
for quoteText in soup.find_all('div', class_="quoteText"):
    quote = quoteText.text
    print(quote)
    print()

    csv_writer.writerow([quote])
csv_file.close()