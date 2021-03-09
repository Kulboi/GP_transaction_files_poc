import re
import sys
import json

# TRANSACTION_FILE = open("CAPs6.txt", "r")
TRANSACTION_FILE = sys.argv

def dataParser():
  transaction_dump_array = []
  for line in TRANSACTION_FILE:
      columns = line.split()  # Split columns using space as delimiter
      # Get the date from column three
      date_chars_arr = re.findall('[0-9]', columns[2])
      # Get the company code from column three
      company_code = re.findall('[A-Z]', columns[2])
      symbol_split = re.split('[A-Z]', columns[4])
      transaction_dump_array.append({
          'column_one': columns[0],
          'column_two': columns[1],
          'date': ''.join(date_chars_arr),
          'company_code': ''.join(company_code),
          'column_five': columns[3],
          'column_six': re.split('[-+]', columns[4])[0],
          'type': re.split('[0]', symbol_split[0])[1],  # Transaction type
          'column_eight': re.split('[-+]', columns[4])[1]
      })

  return json.dumps(transaction_dump_array)

dataParser()
