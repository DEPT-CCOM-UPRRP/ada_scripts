#!/usr/bin/env python3

# Israel O. Dilan
# Script para arreglar cuentas sin home en ada en bulk usando un csv con los email 

from os import system
from sys import argv
import csv

# Try to read input file
try:
    f = argv[1]
# Check if it's a CSV file
    # if (csv.Sniffer().has_header(csvfile)):
    if (f.split(".")[-1] != "csv"):
        raise TypeError("Not CSV file")
# Not a csv error
except TypeError:
    print ("Please input a .csv file")
    raise
# No input file given
except IndexError:
    print ("Usage: ./fix_Cuentas_Ada.py <csv-file>\
    \n\tAlso remember $ chmod +x fix_Cuentas_Ada.py")
    print ("Usage: python fix_Cuentas_Ada.py <csv-file>")
    raise

users = []
# Read CSV File and Store username from email field
with open(f) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        users.append(row['email'].split('@')[0])


# Send command to system per User
for i in users:
    home = "/home/estudiantes/{}".format(i)
    cmd = "usermod -d {} {}".format(home, i)
    system(cmd)
