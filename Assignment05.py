# -----------------------------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Letha, 2/10/2019, Added code to complete assignment 5.
#                     I'm so close! But I have a problem with option 3.
#   Letha, 2/11/2019, Solved my option 3 problem by adding a break.
# https://www.tutorialspoint.com/python/python_dictionary.htm
# -----------------------------------------------------------------------#

# -- Data --#
# declare variables and constants

# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
dicRow = {}

# lstTable = A dictionary that acts as a 'table' of rows
lstTable = []

# strMenu = A menu of user options
strMenu = ""

# strChoice = Capture the user option selection
strChoice = ""

# -- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# -- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called todo.txt into a python Dictionary.
objFile = open("todo.txt","r")
for line in objFile.readlines():    # this for loop reads each line in todo.txt
    row = line.split(',')
    dicRow = {"Task": row[0], "Priority": row[1].rstrip('\n')} # rstrip removes line break
    lstTable.append(dicRow) # adds each dictionary row to lstTable list
objFile.close()

# Step 1.5 Show the user what we're starting with
print("Let's manage your to-do list. This is your starting list:")
for dicRow in lstTable:
    print("{}({})".format(dicRow["Task"],dicRow["Priority"]))

# Step 2
# Display a menu of choices to the user
while (True):
    print("""
    ******************************
    Menu of Options
    1) Show current to-do list
    2) Add a new item to the list
    3) Remove an item from the list
    4) Save the to-do list to a file
    5) Exit program
    ******************************
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] \n"))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print("These are the tasks in your to-do list:\n")
        for dicRow in lstTable:
            print("{}({})".format(dicRow["Task"], dicRow["Priority"]))
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task1 = input("What task do you want to add?\n ")
        priority1 = input("What is the priority, low or high?\n ")
        dicRow = {"Task": task1, "Priority": priority1}
        lstTable.append(dicRow)
        print("Now your to-do list is:")
        for dicRow in lstTable:
            print("{}({})".format(dicRow["Task"], dicRow["Priority"]))
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice == '3'):
        print("These are the tasks in your to-do list:\n")
        for dicRow in lstTable:
            print("{}({})".format(dicRow["Task"], dicRow["Priority"]))
        # for loop checks each dictionary in the list for the string typed
        print("What task do you want to remove?")
        strRemoveChoice = input("Please type it exactly as you see it above (but without the priority).")
        for dicRow in range(0, len(lstTable)):
            if lstTable[dicRow].get('Task') == strRemoveChoice: # This if isn't working the way I want!
                del lstTable[dicRow]
                print("Removed task {}.".format(strRemoveChoice))
                break
        else:
                print("I couldn't find that task. \n")
    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        objFile = open("todo.txt", "w")
        for dicRow in lstTable:
            # clean bad characters from strings so new file matches format of old file
            # Goes through the list
            # writes clean values to to-do list txt
            # .join() puts them together, separated by a comma
            # .get() retrieves the values
            objFile.write(",".join([dicRow.get('Task'), dicRow.get('Priority') + "\n"]))
        objFile.close()
        print("Data saved to file")
    elif (strChoice == '5'):
        break  # and Exit the program

