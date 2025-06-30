# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PROYECTOwIKRwG.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 900)
        icon = QIcon()
        icon.addFile(u":/images/humano.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"<resources>\n"
"  <color name=\"primaryColor\">#2979ff</color>\n"
"  <color name=\"primaryLightColor\">#75a7ff</color>\n"
"  <color name=\"secondaryColor\">#f5f5f5</color>\n"
"  <color name=\"secondaryLightColor\">#ffffff</color>\n"
"  <color name=\"secondaryDarkColor\">#e6e6e6</color>\n"
"  <color name=\"primaryTextColor\">#3c3c3c</color>\n"
"  <color name=\"secondaryTextColor\">#555555</color>\n"
"</resources>\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 60, 701, 71))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(480, 580, 201, 91))
        self.pushButton_2.setStyleSheet(u"font: 15pt \"Segoe UI\";")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(900, 580, 201, 91))
        self.pushButton_3.setStyleSheet(u"font: 15pt \"Segoe UI\";")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(690, 310, 201, 91))
        self.pushButton_4.setStyleSheet(u"font: 15pt \"Segoe UI\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(570, 310, 101, 91))
        self.label_2.setStyleSheet(u"border-image: url(:/iconos/RECONO.png);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(790, 580, 101, 91))
        self.label_3.setStyleSheet(u"border-image: url(:/iconos/SENAS.png);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(348, 580, 121, 95))
        self.label_4.setStyleSheet(u"border-image: url(:/iconos/positividad.png);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MENU DE RECONOCIMIENTO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700; font-style:italic; color:#ffffff;\">MEN\u00da DE RECONOCIMIENTO</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"EMOCIONES", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"SE\u00d1AS", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"ROSTROS", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
    # retranslateUi

