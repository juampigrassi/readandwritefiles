
import csv


CUSTOMERS_FILE = 'customers.csv'
CUSTOMER1_FILE = 'customer_country.csv'


infile = open(CUSTOMERS_FILE, 'r', newline = '')
outfile = open(CUSTOMER1_FILE, 'a', newline = '')
reader = csv.reader(infile)
writer = csv.writer(outfile, delimiter = ',')
fields = next(reader)

for row in reader:    
    first_name = row[1]
    last_name = row[2]
    country = row[4]
    writer.writerow([first_name, last_name, country])
    
    

infile.close()
outfile.close()


