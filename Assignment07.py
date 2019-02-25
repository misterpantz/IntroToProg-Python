#----------------------------------------------------------------------------------------------#
# Title: Pickling, Exceptions
# Dev:   Letha
# Date:  Feb 24, 2019
# ChangeLog: (Who, When, What)
#   Letha, 02/24/2019, Created script
#----------------------------------------------------------------------------------------------#


# Import the Pickle module so that I can pickle and unpickle data
import pickle

# Declare variable
lstPagerDuty = []

# Unpickle data from pagerduty.dat file using pickle.load method
# Use exception handling
try:
    objFile = open("pagerduty.dat", "rb")
    objFileData = pickle.load(objFile)
    objFile.close()
    print("Current pager duty assignment: \n")
    print(objFileData)

# Exception in case there is no pagerduty.dat file or no data
except:
    print("Pager duty isn't yet assigned.\n")

# Identify who is on pager duty this week
strName = input("Who is on pager duty next? ")
strPhone = input("What's their phone number? ")

lstPagerDuty = [strName, strPhone]
print("Pager duty assigned: \n")
print(lstPagerDuty)
print("\n")

# Store the data using the pickle.dump method
objFile = open("pagerduty.dat", "wb")
pickle.dump(lstPagerDuty, objFile)
objFile.close()

# End this script
input ("\n\nPress the Enter key to exit.")