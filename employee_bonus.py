import csv

EMPLOYEE_PAY = 'EmployeePay.csv'

infile = open(EMPLOYEE_PAY, 'r', newline = '')
reader = csv.reader(infile)


for row in reader:
    print(format(row[0], '5') + ' ' + format(row[1], '15') + ' ' + format(row[2], '15') + ' ' + format(row[3], '10') + ' ' + format(row[4], '10'))