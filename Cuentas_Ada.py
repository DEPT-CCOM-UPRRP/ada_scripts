#!/usr/bin/env python3

# Israel O. Dilan
# Script para crear cuentas en bulk usando un csv con los emails

from os import system, urandom
from sys import argv
# from secrets import token_urlsafe
import crypt
import time
import csv
import base64

# Secrets alternative
DEFAULT_ENTROPY = 32  # bytes

def token_bytes(nbytes=None):
    if nbytes is None:
        nbytes = DEFAULT_ENTROPY
    return urandom(nbytes)

def token_urlsafe(nbytes=None):
    tok = token_bytes(nbytes)
    return base64.urlsafe_b64encode(tok).rstrip(b'=').decode('ascii')

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
    print ("Usage: ./Cuentas_Ada.py <csv-file>\
    \n\tAlso remember $ chmod +x Cuentas_Ada.py")
    print ("Usage: python Cuentas_Ada.py <csv-file>")
    raise

users = []
name = []
randpass = []
cypher = []
# Read CSV File and Store username from email field and name if available 
with open(f) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        key = token_urlsafe(8)
        randpass.append(key)
        passw = crypt.crypt(key, salt=crypt.METHOD_SHA512)
        cypher.append(passw)
        users.append(row['email'].split('@')[0])
        name.append(row['name'] if (row['name'] != '-') else row['email'].split('@')[0])

#  Store token to file
t = time.strftime("%d-%b-%Y_%I:%M:%S%p")
with open ("New_Accounts-{}.csv".format(t), "w+", newline='') as Accounts:
    writer = csv.writer(Accounts)
    writer.writerow(("Users", "Passwords"))
    writer.writerows(zip(users, randpass))

# Get Date functions
def get_date():
    return time.strptime(input("Please input custom expiration date in format YYYY-MM-DD: "), "%Y-%m-%d")

y = time.strftime("%Y")
m = time.strftime("%m")
d = time.strftime("%d")
date = "{}-{}-{}".format(y, m, d)
print ("Current_date: {}".format(date)) 
expdate = ""
# Default expiration date
if (int(m) < 6): 
    expdate = "{}-05-29".format(y)
else:
    expdate = "{}-12-29".format(y)
print ("Default_expiration_date: {}".format(expdate))
sure = input("Do you agree with this expiration date? (y/n) ")
if (sure in "Yyes"):
    pass
else:
    new_date = get_date()
    date = time.strptime(date,  "%Y-%m-%d") 
    while (new_date <= date):
        new_date = get_date()
    else:
        expdate = time.strftime("%Y-%m-%d", new_date)
        print("New_expiration_date: " + expdate)


# Send command to system per new_user
sh = "/bin/bash"
skel = "/etc/skel"
for i, j, k in zip(cypher, users, name):
    home = "/home/estudiantes/{}".format(j)
    cmd = "useradd -s {} -c \"{}\" -d {} -m -k {} -e {} -p '{}' {}".format(sh, k, home, skel, expdate, i, j)
    system("echo " + cmd)
    system("echo " + 'chage -d 0 {}'.format(j))
