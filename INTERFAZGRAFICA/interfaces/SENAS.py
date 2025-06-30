# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SENASVLmBtR.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import cv2
import mediapipe as mp
import pickle
import numpy as np

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import resources_rc


# constantes para deteccion de manos
model_dict = pickle.load(open("/home/adrien_hs/Documentos/8_IA_RECOGNIZE/model_manos.p",'rb'))
model = model_dict['model']

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
mp_draw_style = mp.solutions.drawing_styles


hands = mp_hands.Hands(static_image_mode = True, max_num_hands = 1, min_detection_confidence = 0.3)

labels_dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S',19:'T',20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z',26:'A', 27:'B', 28:'C', 29:'D', 30:'E', 31:'F',32:'G',33:'H',34:'I',35:'J',36:'K',37:'L',38:'M', 39:'N', 40:'O', 41:'P', 42:'Q', 43:'R', 44:'S',45:'T',46:'U', 47:'V', 48:'W', 49:'X', 50:'Y', 51:'Z'}


# clase de la subventana de la opcion de manos

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1300, 900)
        icon = QIcon()
        icon.addFile(u":/iconos/SENAS.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 40, 561, 81))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(860, 270, 571, 370))
        self.label_2.setStyleSheet(u"border-image: url(:/iconos/lenguaje.jpg);")

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 150,720,540))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        
        # captura de video
        self.capture = None

        # setting up timer
        self.timer = None

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1330, 720, 141, 61))
        
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1180, 720, 141, 61))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked.connect(self.toggle_mesh)
        
        self.mesh_enabled = True

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SE\u00d1AS", None))
        
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; font-style:italic; color:#ffffff;\">RECONOCIMIENTO DE SE\u00d1AS</span></p></body></html>", None))
        
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">CAMARA</span></p></body></html>", None))

        self.pushButton.setText(QCoreApplication.translate("Form", u"REGRESAR", None))
        
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"MAYA", None))
    # retranslateUi

    def toggle_mesh(self,valor):
        self.mesh_enabled = not self.mesh_enabled
        if valor:
            self.pushButton_2.setText(QCoreApplication.translate("Form", u"MAYA OFF", None))
        else:
            self.pushButton_2.setText(QCoreApplication.translate("Form", u"MAYA ON", None))
    
    
    def update_frame(self):
        data_aux = []
        x_ = []
        y_ = []
        
        ret, frame = self.capture.read()
        
        if ret:
            frame = cv2.flip(frame,1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            step = channel * width
            
            results = hands.process(frame)
            
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    if self.mesh_enabled:
                        mp_draw.draw_landmarks(
                            frame,hand_landmarks,mp_hands.HAND_CONNECTIONS
                        )
                    
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x)
                        data_aux.append(y)
                        x_.append(x)
                        y_.append(y)
                
                x1 = int(min(x_) * width) - 10
                y1 = int(min(y_) * height) - 10
        
                x2 = int(max(x_) * width) - 10
                y2 = int(max(y_) * height) - 10
                
                prediction = model.predict([np.asarray(data_aux)])
                
                predicted_char = labels_dict[int(prediction[0])]
            
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,0), 4)
                cv2.putText(frame,predicted_char,(x1,y1 - 10),cv2.FONT_HERSHEY_SIMPLEX,1.3,(0,0,0),3,cv2.LINE_AA)
                
            q_img = QImage(frame.data, width, height,step, QImage.Format_RGB888)
            self.label_3.setPixmap(QPixmap.fromImage(q_img))
                   
            
    def closeEvent(self, event):
        self.capture.release()
        super().closeEvent(event)
        
        

    

