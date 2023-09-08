# Pynd
A dnd interface built in Python 3.10 using PyQt5 and Sqlite3 libraries        

!!!HOW TO RUN!!!

To run beta.py (main), run it in the command line with
''''
python beta.py itemsList.db
''''


Description:
------------------------------------------------------------------------------------------------------------------------------
This is my first personal project with the intent to introduce the convinience of modern technology to the age old game: Dungeons and Dragons. While the most popular forms of campaigns are conviniently organized in large DND guides sold in book stores, many home brewed campaigns must rely on methods that make organizing and searching for items and their properties extremely difficult on a larger scale. 

The purpose of this personal project is to learn how to apply Python within a practical application along with learning the process of app platform development and organization and analysis of data along the way.
-------------------------------------------------------------------------------------------------------------------------------

Guide:
-------------------------------------------------------------------------------------------------------------------------------
Databases (directory): holds copies of the database and csv currently not in use by main (beta.py)
Item_descriptions (directory): contains .txt files to be read by main for item descriptions
venv (local python virtual environemnt)

beta.py:
    The main running file of the project, includes PyQt5 and Sqlite3. 
    
    MyWindow() makes and manages the current GUI and calls dbRetriever() using the current active database.

    dbRetriever() reads the current item database into a list to be indexed for use in MyWindow()

csvtodb.py:
    Basic .csv to .db converter made for reading .csv tables exported from Excell or Sheets structured for the purposes of this app into a .db file usable by Sqlite3. Takes 2 command line arguments: The name of the new sqlite3 table, and the CSV file
    to be converted into that table.

itemsList.db: Current active database, a copy of ItemsList.db in /Databases

schema.txt: Used to organize properties of items into tables TO BE CREATED AND IMPLIMENTED into sqlite3.

a TODO list is also included to provide transparancy on what is currently in progress or in the process of brainstorming.