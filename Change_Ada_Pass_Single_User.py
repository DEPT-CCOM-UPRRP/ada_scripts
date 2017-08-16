#!/usr/bin/env python3

# Israel O. Dilan
# Script para cambiar el password de usuario en ada

from os import system
from sys import argv
from getpass import getpass
import crypt

# Try to read username from CLI
user = ""
try:
    user = argv[1]
# Ask for username
except:
    user = input("Please input you ada username: ")

# Send command to system
cmd = "usermod -p '{}' {}".format(crypt.crypt(getpass("Please input new password: "), salt=crypt.METHOD_SHA512), user)
system("echo " + cmd)

# Set if temporary password or not
temp = input("Is this a temporary password? (y/n) ")
if (temp in ["yYes"]):
	system('chage -d 0 {}'.format(i))
else:
	pass
