import re
import sys
import json

TRANSACTION_FILE = open(sys.argv[0], "r")

def fileParser():
  transaction_dump_array = []
  for line in TRANSACTION_FILE:
      columns = line.split()  # Split columns using space as delimiter
      date_chars_arr = re.findall('[0-9]', columns[2]) # Get the date from column three
      company_code = re.findall('[A-Z]', columns[2]) # Get the company code from column three
      symbol_split = re.split('[A-Z]', columns[4])
      
      transaction_dump_array.append({
          'transaction_id': columns[0],
          'control_id': columns[1],
          'date': ''.join(date_chars_arr),
          'company_code': ''.join(company_code),
          'units': columns[3],
          'sell': re.split('[-+]', columns[4])[0],
          'type': re.split('[0]', symbol_split[0])[1],
          'chn': re.split('[-+]', columns[4])[1]
      })

  return json.dumps(transaction_dump_array)

fileParser()
