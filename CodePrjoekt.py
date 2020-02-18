# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Erfassung.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import concurrent.futures
from datetime import datetime
import subprocess

def get_timestamp(t):
    return datetime.now().strftime(t)

def memorylocation(measurement):
    name_beginning = 'Messstelle_'
    name_mid = measurement + ': '
    name_end = get_timestamp('%d.%m.%Y_%H.%M.%S')
    location_beginning = '/home/pi/Desktop/alone/Messstelle_'
    location_mid = measurement
    location_end = '/'
    datatype = '.csv'
    memory = location_beginning + location_mid + location_end + name_beginning + name_mid + name_end + datatype
    return memory

def get_sensordata(i2caddress, analogchannel):
    beginstring = '/sys/devices/platform/soc/fe804000.i2c/i2c-1/1-'
    midstring = '/in'
    endstring = '_input'
    completestring = beginstring + i2caddress + midstring + analogchannel + endstring
    analogoutput = subprocess.run(['cat', completestring], stdout=subprocess.PIPE, text=True).stdout
    return analogoutput


def openandwriteCSV_1(location, interval, i2caddress, analogchannel):
    S1 = 1
    while S1 == 1:
        with open(location, 'a') as datei:
            ts = get_timestamp('%d.%m.%Y_%H.%M.%S')
            sd = get_sensordata(i2caddress, analogchannel)
            datei.write(ts +'\t')
            datei.write(sd)
            ui.text_1.append(ts + '\t' + sd)
            time.sleep(interval)

def openandwriteCSV_2(location, interval, i2caddress, analogchannel):
    S1 = 1
    while S1 == 1:
        with open(location, 'a') as datei:
            ts = get_timestamp('%d.%m.%Y_%H.%M.%S')
            sd = get_sensordata(i2caddress, analogchannel)
            datei.write(ts +'\t')
            datei.write(sd)
            ui.text_2.append(ts + '\t' + sd)
            time.sleep(interval)

def openandwriteCSV_3(location, interval, i2caddress, analogchannel):
    S1 = 1
    while S1 == 1:
        with open(location, 'a') as datei:
            ts = get_timestamp('%d.%m.%Y_%H.%M.%S')
            sd = get_sensordata(i2caddress, analogchannel)
            datei.write(ts +'\t')
            datei.write(sd)
            ui.text_3.append(ts + '\t' + sd)
            time.sleep(interval)

def openandwriteCSV_4(location, interval, i2caddress, analogchannel):
    S1 = 1
    while S1 == 1:
        with open(location, 'a') as datei:
            ts = get_timestamp('%d.%m.%Y_%H.%M.%S')
            sd = get_sensordata(i2caddress, analogchannel)
            datei.write(ts +'\t')
            datei.write(sd)
            ui.text_4.append(ts + '\t' + sd)
            time.sleep(interval)

class Ui_Fenster(object):
    def setupUi(self, Fenster):
        Fenster.setObjectName("Fenster")
        Fenster.setEnabled(True)
        Fenster.resize(800, 480)
        Fenster.setMaximumSize(QtCore.QSize(800, 452))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("HenkelLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Fenster.setWindowIcon(icon)
        Fenster.setWindowOpacity(1.0)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Fenster)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 3, 781, 443))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        #Textfeld_1
        self.text_1 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.text_1.setObjectName("text_1")
        self.verticalLayout.addWidget(self.text_1)
        #self.text_1.isReadOnly()
        #---------------------------------------------------------
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #IntervallButton1
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(10)
        #---------------------------------------------------------
        self.verticalLayout_2.addWidget(self.spinBox)
        #self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        #self.pushButton.setObjectName("pushButton")
        #self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        #StartButton oben links
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked[bool].connect(self.Button_2_clicked)
        #---------------------------------------------------------
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        #Textfeld_2
        self.text_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.text_2.setObjectName("text_2")
        self.verticalLayout_5.addWidget(self.text_2)
        #---------------------------------------------------------
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        #IntervallButton2
        self.spinBox_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setValue(10)
        #---------------------------------------------------------
        self.verticalLayout_6.addWidget(self.spinBox_3)
        #self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        #self.pushButton_5.setObjectName("pushButton_5")
        #self.verticalLayout_6.addWidget(self.pushButton_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        #StartButton oben rechts
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.clicked[bool].connect(self.Button_6_clicked)
        #---------------------------------------------------------
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        #Textfeld_3
        self.text_3 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.text_3.setObjectName("textr_3")
        self.verticalLayout_7.addWidget(self.text_3)
        #---------------------------------------------------------
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        #IntervallButton3
        self.spinBox_4 = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_4.setValue(10)
        #---------------------------------------------------------
        self.verticalLayout_8.addWidget(self.spinBox_4)
        #self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        #self.pushButton_7.setObjectName("pushButton_7")
        #self.verticalLayout_8.addWidget(self.pushButton_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        #StartButton unten links
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_6.addWidget(self.pushButton_8)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.clicked[bool].connect(self.Button_8_clicked)
        #---------------------------------------------------------
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        #Textfeld_4
        self.text_4 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.text_4.setObjectName("text_4")
        self.verticalLayout_9.addWidget(self.text_4)
        #---------------------------------------------------------
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        #IntervallButton4
        self.spinBox_5 = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_5.setValue(10)
        #---------------------------------------------------------
        self.verticalLayout_10.addWidget(self.spinBox_5)
        #self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        #self.pushButton_9.setObjectName("pushButton_9")
        #self.verticalLayout_10.addWidget(self.pushButton_9)
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        #StartButton unten rechts
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_7.addWidget(self.pushButton_10)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.clicked[bool].connect(self.Button_10_clicked)
        #---------------------------------------------------------
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.retranslateUi(Fenster)
        QtCore.QMetaObject.connectSlotsByName(Fenster)
        #Threads
        self.WorkerThread_2 = WorkerThread_2()
        self.WorkerThread_6 = WorkerThread_6()
        self.WorkerThread_8 = WorkerThread_8()
        self.WorkerThread_10 = WorkerThread_10()

    def retranslateUi(self, Fenster):
        _translate = QtCore.QCoreApplication.translate
        Fenster.setWindowTitle(_translate("Fenster", "Messdatenerfassung"))
        self.label.setText(_translate("Fenster", "Messstelle 1"))
        #self.pushButton.setText(_translate("Fenster", "Apply"))
        self.pushButton_2.setText(_translate("Fenster", "Start"))
        self.label_3.setText(_translate("Fenster", "Messstelle 2"))
        #self.pushButton_5.setText(_translate("Fenster", "Apply"))
        self.pushButton_6.setText(_translate("Fenster", "Start"))
        self.label_4.setText(_translate("Fenster", "Messstelle 3"))
        #self.pushButton_7.setText(_translate("Fenster", "Apply"))
        self.pushButton_8.setText(_translate("Fenster", "Start"))
        self.label_5.setText(_translate("Fenster", "Messstelle 4"))
        #self.pushButton_9.setText(_translate("Fenster", "Apply"))
        self.pushButton_10.setText(_translate("Fenster", "Start"))

    def Button_2_clicked(self, down):
        if down:
            print('Start')
            global thread2
            thread2 = WorkerThread_2()
            thread2.start()
        else: 
            print('Stop')
            thread2.terminate()
    
    def Button_6_clicked(self, down):
        if down:
            print('Start')
            global thread6
            thread6 = WorkerThread_6()
            thread6.start()
        else: 
            print('Stop')
            thread6.terminate()

    def Button_8_clicked(self, down):
        if down:
            print('Start')
            global thread8
            thread8 = WorkerThread_8()
            thread8.start()
        else: 
            print('Stop')
            thread8.terminate()

    def Button_10_clicked(self, down):
        if down:
            print('Start')
            global thread10
            thread10 = WorkerThread_10()
            thread10.start()
        else: 
            print('Stop')
            thread10.terminate()

class WorkerThread_2(QThread):
    def __init__(self, parent = None):
        super(WorkerThread_2, self).__init__(parent)
            
    def run(self):
        openandwriteCSV_1(memorylocation('1'), ui.spinBox.value(), '0048', '4')

class WorkerThread_6(QThread):
    def __init__(self, parent = None):
        super(WorkerThread_6, self).__init__(parent)
    
    def run(self):
        openandwriteCSV_2(memorylocation('2'), ui.spinBox_3.value(), '0048', '5')

class WorkerThread_8(QThread):
    def __init__(self, parent = None):
        super(WorkerThread_8, self).__init__(parent)
    
    def run(self):
        openandwriteCSV_3(memorylocation('3'), ui.spinBox_4.value(), '0048', '6')

class WorkerThread_10(QThread):
    def __init__(self, parent = None):
        super(WorkerThread_10, self).__init__(parent)
    
    def run(self):
        openandwriteCSV_4(memorylocation('4'), ui.spinBox_5.value(), '0048', '7')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fenster = QtWidgets.QDialog()
    ui = Ui_Fenster()
    ui.setupUi(Fenster)
    Fenster.show()
    sys.exit(app.exec_())
    
