# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:22:45 2017

@author: pmcfarlane9
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

def buildWindow():
    """ This function constructs the interface for Maria's tool to generate
    ticker add statistics by analyst over time. This tool takes a file or path
    as input and outputs a file with the relevant statistics. 
    """
    # This function builds and launches a GUI to prompt the user for the information needed.
    
    
    # Opens Windows explorer    
    @pyqtSlot()
    def on_click1():
        filename = QFileDialog.getOpenFileName(w, 'Open File', '/')
        textbox1.setText(filename)
    
    # Closes tool and application continues
    @pyqtSlot()
    def on_click2():
        w.close()
        
    # initialize application    
    a = QApplication(sys.argv)
    
    # w is the handle for the main window of the application
    w = QMainWindow()
    w.resize(320, 100)

    w.setWindowTitle("Ticker Add Stats Tool v1.0")
    

    # The following label1, btn1, and textbox1 defines the area for which
    # the input file will be input to the interface    
    label1 = QLabel(w)
    label1.setText('Path to Ticker Add File (Must be .xlsx)')
    label1.move(15,7)
    label1.adjustSize()
    btn1 = QPushButton('Upload',w)
    btn1.move(250,20)
    btn1.resize(60,20)
    textbox1 = QLineEdit(w)
    textbox1.move(5, 20)
    textbox1.resize(230,20)
    
    # checkbox1 provides a binary output that indicates whether the user
    # would like visualization of the statistics
    checkbox1 = QCheckBox(w)
    checkbox1.setChecked(True)
    checkbox1.move(150,50)
    checkbox1.setText('Generate charts')
    
    # Upload action for btn1
    btn1.clicked.connect(on_click1)

    # Close GUI and continue application 
    btn2 = QPushButton('Run',w)
    btn2.move(5,50)
    btn2.resize(120,40)

    btn2.clicked.connect(on_click2)
    
    
    w.show()

    a.exec_()
    
    # returns the file path and the checkbox1 boolean
    return str(textbox1.text()), checkbox1.isChecked()