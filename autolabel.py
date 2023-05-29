import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import Qt, QPoint
from PyQt5.uic import loadUi

# class ImageLabel(QLabel):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setPixmap(QPixmap("image.jpg"))
#         self.setScaledContents(True)  # QLabel 크기에 이미지를 맞추기 위해 setScaledContents(True) 설정

#     def mousePressEvent(self, event: QMouseEvent):
#         if event.button() == Qt.LeftButton:
#             cursor_pos = event.pos()
#             print("이미지 클릭 좌표:", cursor_pos.x(), cursor_pos.y())

#     def mouseMoveEvent(self, event: QMouseEvent):
#         cursor_pos = event.pos()
#         print("마우스 이동 좌표:", cursor_pos.x(), cursor_pos.y())

#     def mouseReleaseEvent(self, event: QMouseEvent):
#         cursor_pos = event.pos()
#         print("마우스 릴리스 좌표:", cursor_pos.x(), cursor_pos.y())
            
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Mouse Tracking Example")
#         loadUi("labeling.ui", self)  # UI 파일 불러오기
        
#         self.label = ImageLabel(self)
#         self.label.setAlignment(Qt.AlignCenter)
#         self.label.setGeometry(0, 0, int(1920/2), int(1080/2))

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         loadUi("mainwindow.ui", self)  # UI 파일 로드

#         # QLabel에 이미지 설정
#         image = QPixmap("image.jpg")
#         self.lb_img.setPixmap(image)

#         # QLabel에 이벤트 추가
#         self.lb_img.mousePressEvent = self.labelMousePressEvent

#     def labelMousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             print("이미지 라벨 클릭")

class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap("image.jpg"))
        self.drag_start_pos = None

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            print("이미지 라벨 클릭")
            print("좌표:", event.pos().x(), event.pos().y())

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.LeftButton:
            if self.drag_start_pos is None:
                self.drag_start_pos = event.pos()
                print("드래그 시작 좌표:", self.drag_start_pos.x(), self.drag_start_pos.y())
            else:
                delta = event.pos() - self.drag_start_pos
                self.drag_start_pos = event.pos()
                print("드래그 이동 좌표:", event.pos().x(), event.pos().y())
                print("이동 거리:", delta.x(), delta.y())

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            if self.drag_start_pos is not None:
                self.drag_start_pos = None
                print("드래그 종료")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("labeling.ui", self)  # UI 파일 로드

        # ImageLabel 생성 및 설정
        self.lb_img = ImageLabel(self)
        # self.lb_img.setGeometry(50, 50, 400, 300)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()