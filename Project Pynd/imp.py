from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import sqlite3

###############################################################################################################

class dbRetriever:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        print(f"successfully opened {database}\n--------------------")
        self.cursor = self.conn.cursor()

    def indexItems(self):
        self.itemNames = self.cursor.execute("SELECT name FROM items")
        self.itemList = []
        for i in self.itemNames:
            self.itemList.append(i)

        return self.itemList

    def openDescription(self, item):
        self.desc = self.cursor.execute("SELECT desc FROM items WHERE name = ?", (item,))
        self.desc2 = []
        for i in self.desc:
            self.desc2.append(i)

        with open(f'item_descriptions/{self.desc2[0][0]}', 'r') as f:
            contents = f.read()
            return contents

    def openType(self, item):
        self.type = self.cursor.execute("SELECT type FROM items WHERE name = ?", (item,))
        return self.type

    def openDmg(self, item):
        self.dmg = self.cursor.execute("SELECT dmg FROM items WHERE name = ?" , (item,))
        return self.dmg

###############################################################################################################

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__() 
        #xpos, ypos, width, height
        self.setGeometry(200, 200, 500, 750)
        self.setWindowTitle("Pynd")

        self.inst = dbRetriever('databases/itemsheet.db')
        self.itemIndex = 0

        self.initUI()

    def initUI(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("item")
        self.label1.move(250, 100)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("desc") #set label to the currently selected property
        self.label2.move(150, 500)

        #button to cycle item
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Next Item")
        self.b1.clicked.connect(self.cycleItem) #when the button is clicked, change label1 to the currently selected item
        self.b1.move(20, 100)

        #buttons to select properties
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Type")
        self.b2.clicked.connect(self.displayType) #when the button is clicked, change label1 to the currently selected item
        self.b2.move(100, 250)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Damage")
        self.b3.clicked.connect(self.displayDamage) #when the button is clicked, change label1 to the currently selected item
        self.b3.move(200, 250)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Description")
        self.b4.clicked.connect(self.displayDescription) #when the button is clicked, change label1 to the currently selected item
        self.b4.move(300, 250)

    def cycleItem(self):
        self.itemList = self.inst.indexItems()

        if self.itemIndex == (len(self.itemList))-1:
            self.itemIndex = 0
        else:
            self.itemIndex += 1

        self.selectItem = self.itemList[self.itemIndex][0]
        self.label1.setText(self.selectItem)

        self.update()

    def update(self):
        self.label1.adjustSize()
        self.label2.adjustSize()


    #Buttons for displaying properties

    def displayType(self):
        self.type = self.inst.openType(self.selectItem)
        displaytype = []

        for i in self.type:
            displaytype.append(i)
        
        self.label2.setText(displaytype[0][0])

        self.update()
        

    def displayDamage(self):

        self.damage = self.inst.openDmg(self.selectItem)
        displaydamage = []

        for i in self.damage:
            displaydamage.append(i)
        
        self.label2.setText(str(displaydamage[0][0]))
        self.update()

    def displayDescription(self):

        self.desc = self.inst.openDescription(self.selectItem)
        displaydesc = []
        for i in self.desc:
            displaydesc.append(i)

        print(self.desc)
        self.label2.setText(self.desc)
        self.update()

###############################################################################################################

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()