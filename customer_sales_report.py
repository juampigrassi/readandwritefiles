import csv

SALES_FILE = 'sales.csv'
SALES1_FILE = 'salesreport.csv'

infile = open(SALES_FILE, 'r', newline = '')
outfile = open(SALES1_FILE, 'a', newline = '')
reader = csv.reader(infile)
writer = csv.writer(outfile, delimiter = ',')
fields = next(reader)

customer_details = list(reader)

total_250 = 0 
total_251 = 0
total_252 = 0 
total_253 = 0 
total_254 = 0 
total_255 = 0 
total_256 = 0 
total_257 = 0 
total_258 = 0 
total_259 = 0 
total_260 = 0 
total_261 = 0 

for row in customer_details:
    customer_id = int(row[0])   
    subtotal = float(row[3])
    tax = float(row[4])
    freight = float(row[5])
    if customer_id == 250:
        total_250 += subtotal
        total_250 += tax
        total_250 += freight
    if customer_id == 251:
        total_251 += subtotal 
        total_251 += tax
        total_251 += freight
    if customer_id == 252:
        total_252 += subtotal
        total_252 += tax
        total_252 += freight
    if customer_id == 253:
        total_253 += subtotal
        total_253 += tax
        total_253 += freight
    if customer_id == 254:
        total_254 += subtotal
        total_254 += tax
        total_254 += freight
    if customer_id == 255:
        total_255 += subtotal
        total_255 += tax
        total_255 += freight
    if customer_id == 256:
        total_256 += subtotal
        total_256 += tax
        total_256 += freight
    if customer_id == 257:
        total_257 += subtotal
        total_257 += tax
        total_257 += freight
    if customer_id == 258:
        total_258 += subtotal
        total_258 += tax
        total_258 += freight
    if customer_id == 259:
        total_259 += subtotal
        total_259 += tax
        total_259 += freight
    if customer_id == 260:
        total_260 += subtotal
        total_260 += tax
        total_260 += freight
    if customer_id == 261:
        total_261 += subtotal
        total_261 += tax
        total_261 += freight
    
list_updated = [['CustomerID', 'Total'],['250', format(total_250, '.2f')],['251', format(total_251,'.2f')],['252', format(total_252, '.2f')],['253', format(total_253,'.2f')],['254', format(total_254,'.2f')],
                ['255', format(total_255,'.2f')],['256', format(total_256, '.2f')], ['257', format(total_257, '.2f')], ['258', format(total_258, '.2f')],['259', format(total_259,'.2f')],
                ['260', format(total_260,'.2f')], ['261', format(total_261,'.2f')]]

for row in list_updated:
    writer.writerow(row)

infile.close()
outfile.close()



    


    
        


    




