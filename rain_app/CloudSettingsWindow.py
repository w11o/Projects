from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QSpinBox, QLabel, QDialog, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt, QTimer, QRect
import random

widget_settings = [['Ширина:', 1, 800],
                   ['Высота:', 1, 690],
                   ['Плотность капель:', 100, 500, 300],
                   ['Скорость капель:', 4, 8, 5]]

class CloudSettingsWindow(QDialog):
    def __init__(self, cloud_size, rain_settings, cloud_shape):
        super().__init__()
        self.resize(300, 200)

        self.layout = QVBoxLayout()

        self.width_spinbox = QSpinBox(self)
        self.width_spinbox.setRange(widget_settings[0][1], widget_settings[0][2])
        self.width_spinbox.setValue(cloud_size[0])
        self.width_label = QLabel(widget_settings[0][0], self)

        self.height_spinbox = QSpinBox(self)
        self.height_spinbox.setRange(widget_settings[1][1], widget_settings[1][2])
        self.height_spinbox.setValue(cloud_size[1])
        self.height_label = QLabel(widget_settings[1][0], self)

        self.density_spinbox = QSpinBox(self)
        self.density_spinbox.setRange(widget_settings[2][1], widget_settings[2][2])
        self.density_spinbox.setValue(rain_settings[0])
        self.density_label = QLabel(widget_settings[2][0], self)

        self.speed_spinbox = QSpinBox(self)
        self.speed_spinbox.setRange(widget_settings[3][1], widget_settings[3][2])
        self.speed_spinbox.setValue(rain_settings[1])
        self.speed_label = QLabel(widget_settings[3][0], self)

        self.shape_spinbox = QSpinBox(self)
        self.shape_spinbox.setRange(1, 3)
        self.shape_spinbox.setValue(cloud_shape)
        self.shape_label = QLabel(
            'Форма тучки:\n1 - Прямоугольник\n2 - Овал\n3 - Винни-Пух', self)

        apply_button = QPushButton("Применить", self)
        apply_button.clicked.connect(self.accept)

        self.layout.addWidget(self.width_label)
        self.layout.addWidget(self.width_spinbox)
        self.layout.addWidget(self.height_label)
        self.layout.addWidget(self.height_spinbox)
        self.layout.addWidget(self.density_label)
        self.layout.addWidget(self.density_spinbox)
        self.layout.addWidget(self.speed_label)
        self.layout.addWidget(self.speed_spinbox)
        self.layout.addWidget(self.shape_label)
        self.layout.addWidget(self.shape_spinbox)
        self.layout.addWidget(apply_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Настройки тучки')
        self.show()

    def get_values(self):
        return (self.width_spinbox.value(), self.height_spinbox.value(),
                self.density_spinbox.value(), self.speed_spinbox.value(),
                self.shape_spinbox.value())


