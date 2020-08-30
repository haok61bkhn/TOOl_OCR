# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QFileDialog,QInputDialog , QShortcut
from PyQt5.QtGui import QIcon, QPixmap ,QKeySequence
import glob
import os
class Ui_OCR_TOOL(QtWidgets.QMainWindow):
    def setupUi(self, OCR_TOOL):
        OCR_TOOL.setObjectName("OCR_TOOL")
        OCR_TOOL.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(OCR_TOOL)
        self.centralwidget.setObjectName("centralwidget")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(0, 20, 481, 421))
        self.img.setObjectName("img")
        self.path = QtWidgets.QLabel(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(600, 20, 161, 41))
        self.path.setObjectName("path")
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(100, 480, 88, 34))
        self.prev.setObjectName("prev")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(270, 480, 88, 34))
        self.next.setObjectName("next")
        self.label = QtWidgets.QTextEdit(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 90, 181, 41))
        self.label.setObjectName("label")
        self.lb = QtWidgets.QLabel(self.centralwidget)
        self.lb.setGeometry(QtCore.QRect(540, 100, 58, 18))
        self.lb.setObjectName("lb")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(640, 160, 88, 34))
        self.ok.setObjectName("ok")
        OCR_TOOL.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OCR_TOOL)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuFILE = QtWidgets.QMenu(self.menubar)
        self.menuFILE.setObjectName("menuFILE")
        OCR_TOOL.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OCR_TOOL)
        self.statusbar.setObjectName("statusbar")
        OCR_TOOL.setStatusBar(self.statusbar)
        self.open = QtWidgets.QAction(OCR_TOOL)
        self.open.setCheckable(False)
        self.open.setChecked(False)
        self.open.setObjectName("open")
        self.menuFILE.addAction(self.open)
        self.menubar.addAction(self.menuFILE.menuAction())
        self.retranslateUi(OCR_TOOL)
        
        self.next.setShortcut("D")
        self.prev.setShortcut("A")
        # self.ok.setShortcut("Space")
        self.open.setShortcut("Ctrl+O")
        shortcut = QShortcut(QKeySequence("W"), self.label)
        shortcut.activated.connect(self.slot)
        shortcut = QShortcut(QKeySequence("Ctrl+S"), self.label)
        shortcut.activated.connect(self.disslot)
        # shortcut = QShortcut(QKeySequence("Del"))
        # shortcut.activated.connect(self.disslot)

        self.list_img=[]
        self.id=0
        self.check=False
        QtCore.QMetaObject.connectSlotsByName(OCR_TOOL)
    def slot(self):
        self.label.setFocus()
    def disslot(self):
        self.label.clearFocus()
        self.event_ok()

    def show_image(self,path):
        try:
            label = open(path.split(".")[0]+".txt").read()
        except:
            label =""
        self.label.setText(label)
        self.path.setText(path.split("/")[-1])
        pixmap = QPixmap(path)
        self.img.setPixmap(pixmap)
        self.img.setScaledContents(False)
        self.check=True
    
    def showdialog(self):
        self.check=False
        folderPath = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select folder')
        self.list_img=glob.glob(folderPath+"/*.jpg")+glob.glob(folderPath+"/*.png")+glob.glob(folderPath+"/*.jpeg")
        self.id=0
        if(len(self.list_img)>0):
            self.show_image(self.list_img[0])
        
    def event_ok(self):
        if(self.check):
            lb=self.label.toPlainText()
            path=self.list_img[self.id]
            label = open(path.split(".")[0]+".txt","w+")
            label.write(lb)
            label.close()

    def event_next(self):
        if(self.id <len(self.list_img)-1):
            self.id +=1
            self.show_image(self.list_img[self.id])
    def event_prev(self):
        if(self.id>0):
            self.id -=1
            self.show_image(self.list_img[self.id])

    def retranslateUi(self, OCR_TOOL):
        _translate = QtCore.QCoreApplication.translate
        OCR_TOOL.setWindowTitle(_translate("OCR_TOOL", "OCR_TOOL"))
        self.img.setText(_translate("OCR_TOOL", "img"))
        self.path.setText(_translate("OCR_TOOL", "Path"))
        self.prev.setText(_translate("OCR_TOOL", "Previous"))
        self.next.setText(_translate("OCR_TOOL", "Next"))
        self.lb.setText(_translate("OCR_TOOL", "Label"))
        self.ok.setText(_translate("OCR_TOOL", "OK"))
        self.menuFILE.setTitle(_translate("OCR_TOOL", "FILE"))
        self.open.setText(_translate("OCR_TOOL", "OPEN"))
        
        self.open.triggered.connect(self.showdialog)
        self.next.clicked.connect(self.event_next)
        self.prev.clicked.connect(self.event_prev)
        self.ok.clicked.connect(self.event_ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OCR_TOOL = QtWidgets.QMainWindow()
    ui = Ui_OCR_TOOL()
    ui.setupUi(OCR_TOOL)
    OCR_TOOL.show()
    sys.exit(app.exec_())
