# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pya.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 293)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.openAudioFile)
        self.pushButton_2.clicked.connect(Form.player)
        self.pushButton_3.clicked.connect(Form.pauseAudio)
        self.pushButton_4.clicked.connect(Form.beginAudio)
        self.pushButton_5.clicked.connect(Form.gono)
        self.pushButton_6.clicked.connect(Form.stopAudio)
        self.pushButton_8.clicked.connect(Form.overAudio)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "打开文件"))
        self.pushButton_2.setText(_translate("Form", "播放"))
        self.pushButton_3.setText(_translate("Form", "暂停"))
        self.pushButton_5.setText(_translate("Form", "继续"))
        self.pushButton_6.setText(_translate("Form", "停止"))
        self.pushButton_4.setText(_translate("Form", "录音开始"))
        self.pushButton_8.setText(_translate("Form", "录音结束"))
