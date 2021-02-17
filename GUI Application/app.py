from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import matplotlib.pyplot as plt 
import datetime
import sys

sys.path.append('../DataBase/')
from db import Management

class Ui_workHoursAnalysis(object):

    def __init__(self):
        self.database = Management()
        self.data = self.database.returnData()
        self.data.sort(key=lambda x: datetime.datetime.strptime(x[0], '%Y-%m-%d'))
        self.weekNos = len(self.data) // 7
        self.weekNoCurr = self.weekNos
        self.analyse()

    def setupUi(self, workHoursAnalysis):
        workHoursAnalysis.setObjectName("workHoursAnalysis")
        workHoursAnalysis.resize(800, 603)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        workHoursAnalysis.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(workHoursAnalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.graph = QtWidgets.QLabel(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(170, 140, 461, 400))
        self.graph.setText("")
        self.graph.setTextFormat(QtCore.Qt.PlainText)
        self.graph.setPixmap(QtGui.QPixmap("plot.png"))
        self.graph.setScaledContents(True)
        self.graph.setObjectName("graph")

        self.weekDate = QtWidgets.QLabel(self.centralwidget)
        self.weekDate.setGeometry(QtCore.QRect(210, 540, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.weekDate.setFont(font)
        self.weekDate.setAlignment(QtCore.Qt.AlignCenter)
        self.weekDate.setObjectName("weekDate")

        self.avgWorkedLabel = QtWidgets.QLabel(self.centralwidget)
        self.avgWorkedLabel.setGeometry(QtCore.QRect(590, 410, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avgWorkedLabel.setFont(font)
        self.avgWorkedLabel.setObjectName("avgWorkedLabel")
        self.avgWastedLabel = QtWidgets.QLabel(self.centralwidget)
        self.avgWastedLabel.setGeometry(QtCore.QRect(590, 430, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avgWastedLabel.setFont(font)
        self.avgWastedLabel.setObjectName("avgWastedLabel")
        self.sumWorkedLabel = QtWidgets.QLabel(self.centralwidget)
        self.sumWorkedLabel.setGeometry(QtCore.QRect(590, 450, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sumWorkedLabel.setFont(font)
        self.sumWorkedLabel.setObjectName("sumWorkedLabel")
        self.sumWastedLabel = QtWidgets.QLabel(self.centralwidget)
        self.sumWastedLabel.setGeometry(QtCore.QRect(590, 470, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sumWastedLabel.setFont(font)
        self.sumWastedLabel.setObjectName("sumWastedLabel")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 781, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.date = QtWidgets.QLabel(self.frame)
        self.date.setGeometry(QtCore.QRect(10, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.date.setFont(font)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName("date")

        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName("dateEdit")
        today = datetime.date.today()
        self.dateEdit.setDate(today)
        self.workEdit = QtWidgets.QSpinBox(self.frame)
        self.workEdit.setGeometry(QtCore.QRect(230, 60, 181, 41))
        self.workEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.workEdit.setObjectName("workEdit")
        self.wasteEdit = QtWidgets.QSpinBox(self.frame)
        self.wasteEdit.setGeometry(QtCore.QRect(430, 60, 181, 41))
        self.wasteEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.wasteEdit.setObjectName("wasteEdit")

        self.work = QtWidgets.QLabel(self.frame)
        self.work.setGeometry(QtCore.QRect(230, 20, 181, 31))
        self.work.setAlignment(QtCore.Qt.AlignCenter)
        self.work.setObjectName("work")
        self.waste = QtWidgets.QLabel(self.frame)
        self.waste.setGeometry(QtCore.QRect(430, 20, 181, 31))
        self.waste.setAlignment(QtCore.Qt.AlignCenter)
        self.waste.setObjectName("waste")

        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setGeometry(QtCore.QRect(650, 10, 121, 41))
        self.addButton.setObjectName("addButton")
        self.updateButton = QtWidgets.QPushButton(self.frame)
        self.updateButton.setGeometry(QtCore.QRect(650, 60, 121, 41))
        self.updateButton.setObjectName("updateButton")

        self.preWeek = QtWidgets.QPushButton(self.centralwidget)
        self.preWeek.setGeometry(QtCore.QRect(170, 540, 41, 31))
        self.preWeek.setObjectName("preWeek")
        self.nextWeek = QtWidgets.QPushButton(self.centralwidget)
        self.nextWeek.setGeometry(QtCore.QRect(590, 540, 41, 31))
        self.nextWeek.setObjectName("nextWeek")

        workHoursAnalysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(workHoursAnalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        workHoursAnalysis.setMenuBar(self.menubar)

        self.retranslateUi(workHoursAnalysis)
        QtCore.QMetaObject.connectSlotsByName(workHoursAnalysis)

        self.addButton.clicked.connect(lambda: self.add_clicked(self.dateEdit.date(), self.workEdit.value(), self.wasteEdit.value()))
        self.updateButton.clicked.connect(lambda: self.update_clicked(self.dateEdit.date(), self.workEdit.value(), self.wasteEdit.value()))
        self.preWeek.clicked.connect(self.pre_clicked)
        self.nextWeek.clicked.connect(self.next_clicked)

        if self.weekNoCurr == 1:
            self.preWeek.setEnabled(False)
        if self.weekNoCurr == self.weekNos:
            self.nextWeek.setEnabled(False)

    def retranslateUi(self, workHoursAnalysis):
        _translate = QtCore.QCoreApplication.translate
        workHoursAnalysis.setWindowTitle(_translate("workHoursAnalysis", "Work Hour Analysis"))
        
        d1 = self.data[-7][0]
        d1 = d1[8:10] + '/' + d1[5:7] + '/' + d1[0:4]
        d2 = self.data[-1][0]
        d2 = d2[8:10] + '/' + d2[5:7] + '/' + d2[0:4]
        self.weekDate.setText(_translate("workHoursAnalysis", d1 + " - " + d2))
        self.avgWorkedLabel.setText(_translate("workHoursAnalysis", " "*10 + "Avg Work:\t{}".format(self.avgWorked)))
        self.avgWorkedLabel.adjustSize()
        self.avgWastedLabel.setText(_translate("workHoursAnalysis", " "*10 + "Avg Waste:\t{}".format(self.avgWasted)))
        self.avgWastedLabel.adjustSize()
        self.sumWorkedLabel.setText(_translate("workHoursAnalysis", " "*10 + "Total Work:\t{}".format(self.sumWorked)))
        self.sumWorkedLabel.adjustSize()
        self.sumWastedLabel.setText(_translate("workHoursAnalysis", " "*10 + "Total Waste:\t{}".format(self.sumWasted)))
        self.sumWastedLabel.adjustSize()
        self.date.setText(_translate("workHoursAnalysis", "Date"))
        self.work.setText(_translate("workHoursAnalysis", "Work Hours"))
        self.waste.setText(_translate("workHoursAnalysis", "Waste Hours"))
        self.addButton.setText(_translate("workHoursAnalysis", "Add"))
        self.updateButton.setText(_translate("workHoursAnalysis", "Update"))
        self.preWeek.setText(_translate("workHoursAnalysis", "<"))
        self.nextWeek.setText(_translate("workHoursAnalysis", ">"))

    def add_clicked(self, dateVal, workVal, wasteVal):
        dateVal = datetime.datetime(dateVal.year(), dateVal.month(), dateVal.day())
        record = self.database.checkData(str(dateVal.strftime('%Y-%m-%d')))
        if not record:
            self.database.insertData([str(dateVal.strftime('%Y-%m-%d')), workVal, wasteVal])
        else:
            self.show_popup_recordExist(record[0])
        self.update()
        self.weekNos = len(self.data) // 7
        self.weekNoCurr = self.weekNos
        if self.weekNoCurr == self.weekNos:
            self.nextWeek.setEnabled(False)
        if self.weekNoCurr > 1:
            self.preWeek.setEnabled(True)
    
    def update_clicked(self, dateVal, workVal, wasteVal):
        dateVal = datetime.datetime(dateVal.year(), dateVal.month(), dateVal.day())
        record = self.database.checkData(str(dateVal.strftime('%Y-%m-%d')))
        if record:
            self.database.updateData([str(dateVal.strftime('%Y-%m-%d')), workVal, wasteVal])
        else:
            self.show_popup_recordDoesntExist()
        self.update()
    
    def pre_clicked(self):
        """Plot of previous week"""
        self.weekNoCurr -= 1
        dateRange = self.weekDate.text().split(' ')
        lDate = datetime.datetime.strptime(dateRange[0], '%d/%m/%Y') - datetime.timedelta(days=7)
        rDate = datetime.datetime.strptime(dateRange[-1], '%d/%m/%Y') - datetime.timedelta(days=7)
        self.weekDate.setText(lDate.strftime('%d/%m/%Y') + ' - ' + rDate.strftime('%d/%m/%Y'))
        if self.weekNoCurr == 1:
            self.preWeek.setEnabled(False)
        if self.weekNoCurr < self.weekNos:
            self.nextWeek.setEnabled(True)
        self.update()
    
    def next_clicked(self):
        """Plot of previous week"""
        self.weekNoCurr += 1
        dateRange = self.weekDate.text().split(' ')
        lDate = datetime.datetime.strptime(dateRange[0], '%d/%m/%Y') + datetime.timedelta(days=7)
        rDate = datetime.datetime.strptime(dateRange[-1], '%d/%m/%Y') + datetime.timedelta(days=7)
        self.weekDate.setText(lDate.strftime('%d/%m/%Y') + ' - ' + rDate.strftime('%d/%m/%Y'))
        if self.weekNoCurr == self.weekNos:
            self.nextWeek.setEnabled(False)
        if self.weekNoCurr > 1:
            self.preWeek.setEnabled(True)
        self.update()

    def update(self):
        """Update the plot with every addition or updation"""
        self.data = self.database.returnData()
        self.data.sort(key=lambda x: datetime.datetime.strptime(x[0], '%Y-%m-%d'))
        
        self.analyse()
        self.graph.setPixmap(QtGui.QPixmap("plot.png"))

        self.avgWorkedLabel.setText(" "*10 + "Avg Work:\t{}".format(self.avgWorked))
        self.avgWorkedLabel.adjustSize()
        self.avgWastedLabel.setText(" "*10 + "Avg Waste:\t{}".format(self.avgWasted))
        self.avgWastedLabel.adjustSize()
        self.sumWorkedLabel.setText(" "*10 + "Total Work:\t{}".format(self.sumWorked))
        self.sumWorkedLabel.adjustSize()
        self.sumWastedLabel.setText(" "*10 + "Total Waste:\t{}".format(self.sumWasted))
        self.sumWastedLabel.adjustSize()

    def analyse(self):
        """Plotting the data that was extracted from the database"""
        if self.weekNos == self.weekNoCurr:
            data = np.array(self.data[-7:]).T
        else:
            data = np.array(self.data[-7 * (self.weekNos - self.weekNoCurr + 1): -7 * (self.weekNos - self.weekNoCurr)]).T
        X = np.array(data[1:3]).astype('float64')
        self.avgWorked = np.round(np.average(X[0]), 2)
        self.avgWasted = np.round(np.average(X[1]), 2)
        self.sumWorked = np.sum(X[0])
        self.sumWasted = np.sum(X[1])
        for i,v in enumerate(data[0]):
            data[0][i] = v[5:]

        plt.plot(data[0], X[0], c='blue')
        plt.plot(data[0], X[1], c='orange')
        plt.plot(data[0], [self.avgWorked] * 7, '--', c='blue', label='Avg Work Hours')
        plt.plot(data[0], [self.avgWasted] * 7, '--', c='orange', label='Avg Waste Hours')
        plt.legend()
        plt.savefig('plot.png')
        plt.clf()

    def show_popup_recordExist(self, details):
        msg = QMessageBox()
        msg.setWindowTitle('Error')
        msg.setText('The record already exists.')
        msg.setIcon(QMessageBox.Warning)
        msg.setInformativeText('Only a single entry can be added per date.')

        msg.setDetailedText('The existing values are\nWork Hours:\t{}\nWasted Hours:\t{}\nUse the UPDATE button if you want to update the record.\nDate: {}'.format(details[1], details[2], details[0]))

        x = msg.exec_()

    def show_popup_recordDoesntExist(self):
        msg = QMessageBox()
        msg.setWindowTitle('Error')
        msg.setText('The record does not exists.')
        msg.setIcon(QMessageBox.Warning)
        msg.setInformativeText('Use the ADD button to add the record.')

        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    workHoursAnalysis = QtWidgets.QMainWindow()
    ui = Ui_workHoursAnalysis()
    ui.setupUi(workHoursAnalysis)
    workHoursAnalysis.show()
    sys.exit(app.exec_())
