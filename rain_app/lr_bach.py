from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QSpinBox, QLabel, QDialog, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt, QTimer, QRect
import json
import random
from CloudSettingsWindow import CloudSettingsWindow
from Cloud import Cloud








class RainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Дождик")
        self.setGeometry(550, 150, 800, 800)
        self.setStyleSheet("background-color: black;")

        self.clouds = []
        self.paused = False
        self.is_deleting = False
        self.dragged_cloud = None

        self.setup_ui()

    def setup_ui(self):
        create_button = QPushButton("Создать тучку", self)
        create_button.setStyleSheet("background-color: green;")
        create_button.resize(180, 60)
        create_button.move(50, 690)
        create_button.clicked.connect(self.create_cloud)

        pause_button = QPushButton("Пауза", self)
        pause_button.setStyleSheet("background-color: yellow;")
        pause_button.resize(180, 60)
        pause_button.move(250, 690)
        pause_button.clicked.connect(self.toggle_pause)

        delete_button = QPushButton("Удалить тучку", self)
        delete_button.setStyleSheet("background-color: red;")
        delete_button.resize(180, 60)
        delete_button.move(450, 690)
        delete_button.clicked.connect(self.delete_cloud)

        self.show()

    def create_cloud(self):
        cloud = Cloud(random.randint(1, 600), 20, self.paused, self.update)
        self.clouds.append(cloud)
        self.update()

    def mousePressEvent(self, event):
        for cloud in self.clouds[::-1]:
            cloud_area = QRect(cloud.x, cloud.y, cloud.width, cloud.height)
            if cloud_area.contains(event.pos()):
                if event.button() == Qt.LeftButton:
                    if self.is_deleting:
                        self.clouds.remove(cloud)
                        self.is_deleting = False
                        self.update()
                    else:
                        cloud.change_cloud_settings()
                elif event.button() == Qt.RightButton:
                    cloud.is_dragging = True
                    self.dragged_cloud = cloud
                break

    def mouseMoveEvent(self, event):
        if self.dragged_cloud and self.dragged_cloud.is_dragging:
            self.dragged_cloud.x, self.dragged_cloud.y = event.pos().x(), event.pos().y()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.dragged_cloud and event.button() == Qt.RightButton:
            self.dragged_cloud.is_dragging = False
            self.dragged_cloud = None

    def toggle_pause(self):
        self.paused = not self.paused
        for cloud in self.clouds:
            if self.paused:
                cloud.timer.stop()
            else:
                cloud.timer.start(20)

    def delete_cloud(self):
        self.is_deleting = True

    def paintEvent(self, event):
        painter = QPainter(self)
        for cloud in self.clouds:
            cloud.draw_cloud(painter)

if __name__ == '__main__':
    app = QApplication([])
    window = RainApp()
    app.exec_()

