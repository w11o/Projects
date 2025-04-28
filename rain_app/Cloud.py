from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QSpinBox, QLabel, QDialog, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt, QTimer, QRect
import random
from CloudSettingsWindow import CloudSettingsWindow

class Cloud:
    def __init__(self, x_pos, y_pos, is_paused, update_func):
        self.x = x_pos
        self.y = y_pos
        self.width = 120
        self.height = 80
        self.drop_density = 150
        self.drop_speed = 5
        self.form_type = 1

        self.drops = []
        self.is_paused = is_paused
        self.update_func = update_func
        self.is_dragging = False
        self.initialize_drops()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_drops)
        if not is_paused:
            self.timer.start(20)

    def draw_cloud(self, painter):
        painter.setPen(QPen(Qt.white, 2))
        if self.form_type == 1:
            painter.drawRect(self.x, self.y, self.width - 1, self.height - 1)
        elif self.form_type == 2:
            painter.drawEllipse(self.x, self.y, self.width - 1, self.height - 1)
        elif self.form_type == 3:
            pixmap = QPixmap("винни-пух-тучка2.png")
            painter.drawPixmap(QRect(self.x, self.y, self.width - 1, self.height - 1), pixmap)

        for drop in self.drops:
            painter.drawLine(drop[0], drop[1], drop[0], drop[1] + drop[2])

    def initialize_drops(self):
        self.drops = [[random.randint(self.x + 10, self.x + self.width - 10),
                       random.randint(self.y + self.height, self.y + self.height + 50),
                       random.randint(20, 30),
                       random.randint(0, 3),
                       random.randint(self.drop_speed, 3 * self.drop_speed)] for _ in range(self.drop_density)]

    def change_cloud_settings(self):
        current_size = (self.width, self.height)
        rain_settings = (self.drop_density, self.drop_speed)
        settings_window = CloudSettingsWindow(current_size, rain_settings, self.form_type)
        if settings_window.exec_() == CloudSettingsWindow.Accepted:
            new_values = settings_window.get_values()
            self.width, self.height, self.drop_density, self.drop_speed, self.form_type = new_values
            self.initialize_drops()
            self.update_func()

    def update_drops(self):
        for drop in self.drops:
            drop[1] += drop[4]
            if drop[1] + drop[2] > 690:
                drop[1] = random.randint(self.y + self.height, self.y + self.height + 50)
                drop[0] = random.randint(self.x + 10, self.x + self.width - 10)
        self.update_func()
