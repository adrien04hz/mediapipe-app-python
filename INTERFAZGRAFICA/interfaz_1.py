from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from interfaces.PROYECTO import Ui_MainWindow as Prin
from interfaces.EMOCIONES import Ui_Form as Emocioness
from interfaces.ROSTRO import Ui_Form as Rostross
from interfaces.SENAS import Ui_Form as Senass
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap
import sys
import cv2




# Clase de la ventana de emociones
class Emociones(QWidget, Emocioness):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.capture = None
        
        img_path = "/home/adrien_hs/Documentos/8_IA_RECOGNIZE/INTERFAZGRAFICA/images/Color_negro.jpg"  # Asegúrate de que el archivo tiene una extensión de imagen válida
        img = cv2.imread(img_path)
                
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convertir a RGB
        h, w, c = img.shape
        q_i = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_i)
        scaled_pixmap = pixmap.scaled(self.label_3.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.label_3.setPixmap(scaled_pixmap)
        
        
    def showEvent(self,event):
        self.start_camera()
        super().showEvent(event)
        
        
    def closeEvent(self,event):
        self.stop_camera()
        super().closeEvent(event)


    def start_camera(self):
        if self.capture is None:
            self.capture = cv2.VideoCapture(0)

            self.timer = QTimer()
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(30)
       
            
    def stop_camera(self):
        if self.capture is not None:
            self.capture.release()
            self.capture = None
            self.timer.stop()

        img_path = "/home/adrien_hs/Documentos/8_IA_RECOGNIZE/INTERFAZGRAFICA/images/Color_negro.jpg"
        img = cv2.imread(img_path)
                
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        h, w, c = img.shape
        q_i = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_i)
        scaled_pixmap = pixmap.scaled(self.label_3.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.label_3.setPixmap(scaled_pixmap)


# Clase de la ventana de rostros
class Rostro(QWidget, Rostross):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.capture = None

        img_path = "/home/adrien_hs/Documentos/8_IA_RECOGNIZE/INTERFAZGRAFICA/images/Color_negro.jpg"  # Asegúrate de que el archivo tiene una extensión de imagen válida
        img = cv2.imread(img_path)
                
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convertir a RGB
        h, w, c = img.shape
        q_i = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_i)
        scaled_pixmap = pixmap.scaled(self.label_3.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.label_3.setPixmap(scaled_pixmap)
        
        
    def showEvent(self,event):
        self.start_camera()
        super().showEvent(event)
        
        
    def closeEvent(self,event):
        self.stop_camera()
        super().closeEvent(event)


    def start_camera(self):
        if self.capture is None:
            self.capture = cv2.VideoCapture(0)

            self.timer = QTimer()
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(30)
       
            
    def stop_camera(self):
        if self.capture is not None:
            self.capture.release()
            self.capture = None
            self.timer.stop()

        img_path = "/home/adrien_hs/Documentos/8_IA_RECOGNIZE/INTERFAZGRAFICA/images/Color_negro.jpg"
        img = cv2.imread(img_path)
                
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        h, w, c = img.shape
        q_i = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_i)
        scaled_pixmap = pixmap.scaled(self.label_3.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.label_3.setPixmap(scaled_pixmap)


# Clase de la ventana de senas
class Senia(QWidget, Senass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.capture = None
    
    
    def showEvent(self,event):
        self.start_camera()
        super().showEvent(event)
        
        
    def closeEvent(self,event):
        self.stop_camera()
        super().closeEvent(event)

    def start_camera(self):
        if self.capture is None:
            self.capture = cv2.VideoCapture(0)

            self.timer = QTimer()
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(30)
            
    def stop_camera(self):
        if self.capture is not None:
            self.capture.release()
            self.capture = None
            self.timer.stop()
        

# Clase de la ventana principal
class Principal(QMainWindow, Prin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton_2.clicked.connect(self.mostrar_emociones)
        self.pushButton_3.clicked.connect(self.mostrar_senas)
        self.pushButton_4.clicked.connect(self.mostrar_rostro)
        
        self.rostro_com = Rostro()
        self.sena = Senia()
        self.emotion = Emociones()
        
        
    def mostrar_rostro(self):
        self.rostro_com.showMaximized()
    
    
    def mostrar_senas(self):
        self.sena.showMaximized()
    
    
    def mostrar_emociones(self):
        self.emotion.showMaximized()
        
        


# Script de ejecucion
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Principal()
    window.showMaximized()
    sys.exit(app.exec())