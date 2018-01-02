#   Initializer Script
#
#
#   https://github.com/SalmonSeasoning/ArpPi.git
#
#   License: MIT

import os

os.system("echo Welcome to ArpPi!")
toContinue = str(input("Enter 'Y' to continue or 'N' to exit! "))
if toContinue == 'N':
    os.system("echo GOODBYE!")
    os._exit(0)
else if toContinue == 'Y':
    os.system("Initializing..")
else:
    os.system("INPUT TYPE IS NOT EQUAL TO 'Y' OR 'N'")
    os.system("ASSUMING EXIT")
    os._exit(0)

