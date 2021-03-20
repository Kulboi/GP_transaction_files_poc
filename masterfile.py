import sys
import json

MASTER_FILE = open(sys.argv[0], "r")

def fileParser():
  master_dump_array = []
  for line in MASTER_FILE:
    master_dump_array.append({
      "chn": line[0:15].strip(), 
      'names': line[15:45].strip(),
      'address1': line[55:120].strip(),
      'address2': line[120:200].strip(),
      'country': line[200:243].strip()[0:3],
      'bank': line[200:243].strip()[3:],
      'bvn': line[243:273].strip(),
      'email': line[273:313].strip(),
      'phone_number': line[313:353].strip(),
      "next_of_kin": line[353:380].strip()
    })

  return json.dumps(master_dump_array)


fileParser()