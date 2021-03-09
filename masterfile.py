import sys
import json

# MASTER_FILE = open("CAPmast.txt", "r")
MASTER_FILE = sys.argv

def dataParser():
  master_dump_array = []
  for line in MASTER_FILE:
    master_dump_array.append({
      "CHN": line[0:15].strip(), 
      'fullname': line[15:45].strip(),
      'address': line[55:120].strip(),
      'location': line[120:200].strip(),
      'bank': line[200:243].strip(),
      'rand_num': line[243:273].strip(),
      'email': line[273:313].strip(),
      'rand_num_2': line[313:353].strip(),
      "contact": line[353:380].strip()
    })

  return json.dumps(master_dump_array)


dataParser()