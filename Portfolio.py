# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Portfolio.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(483, 417)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("#Dialog {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 30, 331, 351))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("#widget {\n"
"border-radius : 20px ;\n"
"border : 2px solid black ;\n"
"background-color: #448ccb ;\n"
"}")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(40, -30, 271, 291))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet("#widget_2 {\n"
"    image: url(:/Mes images/maphoto.png);\n"
"border-radius : 60px  ;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.line = QtWidgets.QFrame(self.widget_2)
        self.line.setGeometry(QtCore.QRect(50, 230, 161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setGeometry(QtCore.QRect(70, 240, 121, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(50, 250, 241, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255,0.5);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "YASSI FREDERIC HENRI JUNIOR \n"
" DEVELOPPEUR D\'APPLICATIONS \n"
" email : yassifrederic@gmail.com \n"
" Tel : (+225) 0767515643"))
        self.label_2.setText(_translate("Dialog", "AUTEUR"))
import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
