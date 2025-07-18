# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EMOCIONESKcWCTq.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import resources_rc

import sys
import cv2
import mediapipe as mp
import pickle
import numpy as np


model_dict = pickle.load(open("/home/adrien_hs/Documentos/8_IA_RECOGNIZE/model_emociones_prueba.p",'rb'))

model = model_dict['model']

mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils
mp_draw_style = mp.solutions.drawing_styles


face = mp_face.FaceMesh(static_image_mode = True, max_num_faces = 1, min_detection_confidence = 0.3)
labels_dict = {0:'Enojo', 1:'Feliz', 2:'Sorpresa',3:'Triste'}


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1300, 900)
        icon = QIcon()
        icon.addFile(u":/iconos/positividad.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 40, 601, 81))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 150,720,540))
        self.label_2.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(255, 0, 0);")
        
        
        self.capture = None
        self.timer = None
        
        
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(930, 220, 400, 400))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1330, 720, 141, 61))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"EMOCIONES", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; font-style:italic; color:#ffffff;\">RECONOCIMIENTO DE EMOCIONES</span></p></body></html>", None))
        
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">CAMARA</span></p></body></html>", None))
        
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">INFORMACION EMOCIONES</span></p></body></html>", None))
        
        self.pushButton.setText(QCoreApplication.translate("Form", u"REGRESAR", None))
    # retranslateUi


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
            
            results = face.process(frame)
            
            if results.multi_face_landmarks:         
                for face_landmarks in results.multi_face_landmarks:
                    for i in range(len(face_landmarks.landmark)):
                        x = face_landmarks.landmark[i].x
                        y = face_landmarks.landmark[i].y
                
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
                cv2.putText(frame,predicted_char,(x1,y1 - 10),cv2.FONT_HERSHEY_SIMPLEX,1.3,(40,114,51),3,cv2.LINE_AA)
                
        
            q_img = QImage(frame.data, width, height,step, QImage.Format_RGB888)
            self.label_2.setPixmap(QPixmap.fromImage(q_img))
            
            # 0:'Enojo', 1:'Feliz', 2:'Sorpresa',3:'Triste'
            if predicted_char == 'Enojo':
                img_path = "/home/adrien_hs/Documentos/8_IA_RECOGNIZE/INTERFAZGRAFICA/images/emotions/enojito.jpg" 
                img = cv2.imread(img_path)
                
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
                h, w, c = img.shape
                q_i = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_i)
                scaled_pixmap = pixmap.scaled(self.label_3.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.label_3.setPixmap(scaled_pixmap)
                
            elif predicted_char == 'Feliz':
                img_path = "/home/adrien_hs/Documentos/8_IA_RECOGNIZE/INTERFAZGRAFICA/images/emotions/feli.jpg" 
                img = cv2.imread(img_path)
                
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
                h, w, c = img.shape
                q_i = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_i)
                scaled_pixmap = pixmap.scaled(self.label_3.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.label_3.setPixmap(scaled_pixmap)
                
            elif predicted_char == 'Sorpresa':
                img_path = "/home/adrien_hs/Documentos/8_IA_RECOGNIZE/INTERFAZGRAFICA/images/emotions/sorpresita.jpg" 
                img = cv2.imread(img_path)
                
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
                h, w, c = img.shape
                q_i = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_i)
                scaled_pixmap = pixmap.scaled(self.label_3.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.label_3.setPixmap(scaled_pixmap)
                
            elif predicted_char == 'Triste':
                img_path = "/home/adrien_hs/Documentos/8_IA_RECOGNIZE/INTERFAZGRAFICA/images/emotions/tite.jpg" 
                img = cv2.imread(img_path)
                
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
                h, w, c = img.shape
                q_i = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_i)
                scaled_pixmap = pixmap.scaled(self.label_3.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.label_3.setPixmap(scaled_pixmap)
            
            
    def closeEvent(self, event):
        self.capture.release()
        super().closeEvent(event)
