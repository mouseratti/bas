# https://docs.python.org/3/library/csv.html
import csv

with open('csv.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(
        csvfile,
        delimiter=',',
        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    csv_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
