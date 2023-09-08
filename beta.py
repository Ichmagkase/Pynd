from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import sqlite3

# called by MyWindow.__init__() with one argument
class dbRetriever:
    #initialize sqlite3 with the database
    def __init__(self, database):
        self.databaseName = database
        self.conn = sqlite3.connect(database)
        print(f"successfully opened {database}\n--------------------")
        self.cursor = self.conn.cursor() 


    #index names from table into a list
    def indexItems(self):
        self.itemNames = self.cursor.execute(f"SELECT name FROM {self.databaseName[:-3]}") # ignore .db suffix 
        self.itemList = []
        for i in self.itemNames:
            self.itemList.append(i)
        return self.itemList

    #open the description of an item if the item has a description .txt associated with it. Otherwise return None
    def openDescription(self, item):
        self.desc = self.cursor.execute(f"SELECT desc FROM {self.databaseName[:-3]} WHERE name = ?", (item,))
        self.desc2 = []
        for i in self.desc:
            self.desc2.append(i)

        if self.desc2[0][0] == "None":
            return "None"

        with open(f'item_descriptions/{self.desc2[0][0]}', 'r') as f:
            contents = f.read()
            return contents

    # return the 'type' property of the selected item
    def openType(self, item):
        self.type = self.cursor.execute(f"SELECT type FROM {self.databaseName[:-3]} WHERE name = ?", (item,))
        return self.type

    # return the 'dmg' property of the selected item
    def openDmg(self, item):
        self.dmg = self.cursor.execute(f"SELECT dmg FROM {self.databaseName[:-3]} WHERE name = ?" , (item,))
        return self.dmg


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__() 
        #xpos, ypos, width, height, of the window
        self.setGeometry(200, 200, 550, 750)
        self.setWindowTitle("Pynd")

        #BETA TESTING ONLY: Initialize the app with a .db file within the command line arguments at runtime
        try:
            self.instanceDatabase = sys.argv[1]
        except:
            print("Missing argv[1], please include a .db file to be opened")
            exit()
        self.inst = dbRetriever(self.instanceDatabase)
        self.itemIndex = 0

        self.initUI()

    def initUI(self):
        #create a label with default text 'item'
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("item")
        self.label1.move(250, 100)

        #create a label with default text 'desc'
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("desc") #set label to the currently selected property
        self.label2.move(150, 500)

        #button to cycle item
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Next Item")
        self.b1.clicked.connect(self.cycleItem) #when the button is clicked, call cycleItem()
        self.b1.move(20, 100)

        #buttons to select properties
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Type")
        self.b2.clicked.connect(self.displayType) #when the button is clicked, call displayType()
        self.b2.move(100, 250)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Damage")
        self.b3.clicked.connect(self.displayDamage) #when the button is clicked, call displayDamage()
        self.b3.move(200, 250)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Description")
        self.b4.clicked.connect(self.displayDescription) #when the button is clicked, call displayDescription()
        self.b4.move(300, 250)

        

    #cycle through itemList list and display it to label1
    def cycleItem(self):
        self.itemList = self.inst.indexItems()
        if self.itemIndex == (len(self.itemList))-1:
            self.itemIndex = 0
        else:
            self.itemIndex += 1

        self.selectItem = self.itemList[self.itemIndex][0]
        self.label1.setText(self.selectItem)

        self.update()

    #Update the labels to fit the new text
    def update(self):
        self.label1.adjustSize()
        self.label2.adjustSize()

    #call openType() from dbRetriever() and display the return value to label2
    def displayType(self):
        try:
            self.type = self.inst.openType(self.selectItem)
        except:
            print("Please select 'Next Item' before selecting the item type, damage, or description. This will be fixed in the future.")
            exit()
        displaytype = []

        for i in self.type:
            displaytype.append(i)
        
        self.label2.setText(displaytype[0][0])

        self.update()
        
    #call openDmg() from dbRetriever and display the return value to label2
    def displayDamage(self):
        try:
            self.damage = self.inst.openDmg(self.selectItem)
        except:
            print("Please select 'Next Item' before selecting the item type, damage, or description. This will be fixed in the future.")
            exit()
        displaydamage = []

        for i in self.damage:
            displaydamage.append(i)
        
        self.label2.setText(str(displaydamage[0][0]))
        self.update()

    #call openDescription() from dbRetriever() and display the return value to label2
    def displayDescription(self):
        try:
            self.desc = self.inst.openDescription(self.selectItem)
        except:
            print("Please select 'Next Item' before selecting the item type, damage, or description. This will be fixed in the future.")
            exit()
        displaydesc = []
        for i in self.desc:
            displaydesc.append(i)

        self.label2.setText(self.desc)
        self.update()

#main function call that starts and exits the app
def window():
    app = QApplication(sys.argv) 
    win = MyWindow() 

    win.show()
    sys.exit(app.exec_())

window()