# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import VBoxLayout, PushButton, LineEdit

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(581, 543)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 20, 411, 411))
        self.verticalLayout = VBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = LineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setMinimumSize(QSize(0, 80))

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_clear = PushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout_8.addWidget(self.pushButton_clear)

        self.pushButton_back = PushButton(self.layoutWidget)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.horizontalLayout_8.addWidget(self.pushButton_back)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_7 = PushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_7.addWidget(self.pushButton_7)

        self.pushButton_8 = PushButton(self.layoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_7.addWidget(self.pushButton_8)

        self.pushButton_9 = PushButton(self.layoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_7.addWidget(self.pushButton_9)

        self.pushButton_div = PushButton(self.layoutWidget)
        self.pushButton_div.setObjectName(u"pushButton_div")

        self.horizontalLayout_7.addWidget(self.pushButton_div)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_4 = PushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_5 = PushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_6.addWidget(self.pushButton_5)

        self.pushButton_6 = PushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_6.addWidget(self.pushButton_6)

        self.pushButton_mul = QPushButton(self.layoutWidget)
        self.pushButton_mul.setObjectName(u"pushButton_mul")

        self.horizontalLayout_6.addWidget(self.pushButton_mul)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_1 = PushButton(self.layoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout_5.addWidget(self.pushButton_1)

        self.pushButton_2 = PushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_3 = PushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_sub = PushButton(self.layoutWidget)
        self.pushButton_sub.setObjectName(u"pushButton_sub")

        self.horizontalLayout_5.addWidget(self.pushButton_sub)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_0 = PushButton(self.layoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.horizontalLayout.addWidget(self.pushButton_0)

        self.pushButton_dot = PushButton(self.layoutWidget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")

        self.horizontalLayout.addWidget(self.pushButton_dot)

        self.pushButton_cal = PushButton(self.layoutWidget)
        self.pushButton_cal.setObjectName(u"pushButton_cal")

        self.horizontalLayout.addWidget(self.pushButton_cal)

        self.pushButton_add = PushButton(self.layoutWidget)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.horizontalLayout.addWidget(self.pushButton_add)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.pushButton_back.setText(QCoreApplication.translate("Form", u"\u56de\u9000", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_mul.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_cal.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

