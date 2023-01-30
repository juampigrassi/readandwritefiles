import csv

EMPLOYEE_PAY = 'EmployeePay.csv'

infile = open(EMPLOYEE_PAY, 'r', newline = '')
reader = csv.reader(infile)
fields = next(reader)

for row in reader:
    print(row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3] + ' ' + row[4])