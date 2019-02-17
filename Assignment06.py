#----------------------------------------------------------------------------------------------#
# Title: Functions, Class, Methods
# Dev:   Letha
# Date:  Feb 17, 2019
# ChangeLog: (Who, When, What)
#   Letha, 02/17/2019, Created script based on RRoot's Assignment05 answer script
#   Letha, 02/17/2019, Changed name of strData to lstData
#   Letha, 02/17/2019, Changed prompt for menu number from 4 to 5
#   Letha, 02/17/2019, Removed path to file
#   Letha, 02/17/2019, Reorganized script into functions
#   Letha, 02/17/2019, Put all functions in a class
#   Letha, 02/17/2019, Made the functions methods
#----------------------------------------------------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# lstData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Steps --#
# Step 1
# When the program starts, load the any data you have
# in a text file called Todo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the Todo.txt file

# Step 7
# Exit program

#-------------------------------1

objFileName = "Todo.txt"
lstData = ""
dicRow = {}
lstTable = []

#  -- processing code --
#  Create a Class to hold a list of functions
class ProcessToDoList(object):
    """ This class contains methods for managing a to-do list """


    # Processing for step 1
    # When the program starts, load the any data you have
    # in a text file called Todo.txt into a python Dictionary.
    # This step is entirely processing.
    '''This function shows reads a file, collects data in a dictionary, and writes it to a list table'''
    @staticmethod
    def ReadFileData(FileName):
        objFile = open(FileName, "r")
        for line in objFile:
            lstData = line.split(",") # readline() reads a line of the data into 2 elements
            dicRow = {"Task":lstData[0].strip(), "Priority":lstData[1].strip()}
            lstTable.append(dicRow)
        objFile.close()
        return lstTable


    # Processing for step 2
    # Display a menu of choices to the user
    # The processing portion of this is defining the text to display.
    '''This function shows the menu of options'''
    @staticmethod
    def ShowMenu():
        print ("""
            Menu of Options
            1) Show current data
            2) Add a new item.
            3) Remove an existing item.
            4) Save Data to File
            5) Exit Program
            """)

    # Processing for step 3
    # Display all todo items to user
    # Processing portion is collecting the information to show to the user
    '''This function collects the todo list to show to the user'''
    @staticmethod
    def ShowTaskList():
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

    # Processing for step 4
    # Add a new item to the list/Table
    '''This function takes the user's new task and adds it to the list'''
    @staticmethod
    def AddTask(strNewTask,strNewPriority):
        strTask = strNewTask
        strPriority = strNewPriority
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)

    # Processing for step 5
    # Remove a new item to the list/Table
    '''This function tries to remove a task from the list'''
    @staticmethod
    def RemoveTask(strTaskToRemove):
        # 5a-Allow user to indicate which row to delete
        strKeyToRemove = strTaskToRemove
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        while (intRowNumber < len(lstTable)):
            if (strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])):  # the values function creates a list!
                del lstTable[intRowNumber]
                blnItemRemoved = True
            # end if
            intRowNumber += 1
        # end for loop
        # 5b-Update user on the status
        if (blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

    # Processing for step 6
    # Save tasks to the Todo.txt file
    '''This function saves the current list data to the file.'''
    @staticmethod
    def SaveToFile(FileName):
        objFile = open(FileName, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()

    # Processing for step 7
    # Exit program


#-- Presentation --#
# Presentation for step 1
# When the program starts, load the any data you have
# in a text file called Todo.txt into a python Dictionary.
# Step 1 is entirely processing.
lstTable = ProcessToDoList.ReadFileData(objFileName)

# Step 2
# Display a menu of choices to the user
while(True):
    ProcessToDoList.ShowMenu()
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  #adding a new line

    # Step 3
    # Show the current items in the table
    if (strChoice.strip() == '1'):
        ProcessToDoList.ShowTaskList()

    # Step 4
    # Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strNewTask = str(input("What is the task? - ")).strip()
        strNewPriority = str(input("What is the priority? [high|low] - ")).strip()
        ProcessToDoList.AddTask(strNewTask,strNewPriority)
        ProcessToDoList.ShowTaskList()

    # Step 5
    # Remove a new item to the list/Table
    elif(strChoice == '3'):
        strTaskToRemove = input("Which TASK would you like removed? - ")
        ProcessToDoList.RemoveTask(strTaskToRemove)
        ProcessToDoList.ShowTaskList()

    # Step 6
    # Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        #5a Show the current items in the table
        ProcessToDoList.ShowTaskList()
        #5b Ask if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            ProcessToDoList.SaveToFile(objFileName)
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue #to show the menu

    # Step 7
    # Save tasks to the ToDo.txt file
    elif (strChoice == '5'):
        break #and Exit the program

