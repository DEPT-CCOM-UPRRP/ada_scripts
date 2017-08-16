#!/usr/bin/env python3

# Israel O. Dilan
# Script para arreglar passwords en bulk usando un csv con los Users y Passwords

from os import system
from sys import argv
import csv
import crypt

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
    print ("Usage: ./fix_Cuentas_Ada_Pass.py <csv-file>\
    \n\tAlso remember $ chmod +x fix_Cuentas_Ada_Pass.py")
    print ("Usage: python fix_Cuentas_Ada_Pass.py <csv-file>")
    raise

users = []
passw = []
# Read CSV File and Store username an password from Users and Passwords field
with open(f) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        users.append(row['Users'])
        passw.append(row['Passwords'])


# Set if temporary password or not
temp = input("Is this a temporary password? (y/n) ")

# Send command to system per User
if (temp in ["yYes"]):
	for i, j in zip(users, passw):
	cmd = "usermod -p '{}' {}".format(crypt.crypt(j, salt=crypt.METHOD_SHA512), i)
		system(cmd)
		system('chage -d 0 {}'.format(i))
else:
	for i, j in zip(users, passw):
	cmd = "usermod -p '{}' {}".format(crypt.crypt(j, salt=crypt.METHOD_SHA512), i)
		system(cmd)
