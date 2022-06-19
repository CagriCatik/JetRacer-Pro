import copy
#from jetracer.nvidia_racecar import NvidiaRacecar

#works only on jetracer
#
# car = NvidiaRacecar()

import sys
from typing import Union
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QSlider, QCheckBox, QWidget, QDoubleSpinBox,QGridLayout

__manual= Qt.Unchecked
__auto = Qt.Checked


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("JetRacerPro Control Launch")

        self.layout = QGridLayout()
        # automatic checkbox

        self.auto_checkbox = QCheckBox("automatic")
        self.auto_checkbox.setCheckState(Qt.Unchecked)
        self.auto_checkbox.stateChanged.connect(self.show_state)

        #label manual
        self.label_manual = QLabel('Manual mode:')
        self.label_manual.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #label automatic
        self.label_automatic = QLabel('Auto mode:')
        self.label_automatic.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        # manual part
        self.label_speed = QLabel('Set throttle')
        self.label_speed.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_steering = QLabel('Set steering')
        self.label_steering.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_steering_gain = QLabel('Set steering gain')
        self.label_steering_gain.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_steering_offset = QLabel('Set steering offset')
        self.label_steering_offset.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # automatic part
        self.auto_label_speed = QLabel('Throttle')
        self.auto_label_speed.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.auto_label_steering = QLabel('Steering')
        self.auto_label_steering.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.auto_label_steering_gain = QLabel('Steering gain')
        self.auto_label_steering_gain.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.auto_label_steering_offset = QLabel('Steering offset')
        self.auto_label_steering_offset.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)



        self.auto_display_speed = QLabel()
        self.auto_display_speed.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.auto_display_steering = QLabel()
        self.auto_display_steering.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.auto_display_steering_gain = QLabel()
        self.auto_display_steering_gain.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.auto_display_steering_offset = QLabel()
        self.auto_display_steering_offset.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        self.speed_setter = QDoubleSpinBox()
        self.sterring_setter = QDoubleSpinBox()
        self.sterring_gain_setter = QDoubleSpinBox()
        self.sterring_offset_setter = QDoubleSpinBox()

        self.setters = [self.speed_setter, self.sterring_setter, self.sterring_gain_setter, self.sterring_offset_setter]

        for setter in self.setters:
            setter.setMinimum(-1)
            setter.setMaximum(1)
            setter.setSingleStep(0.1)

        # connecting signals
        self.speed_setter.valueChanged.connect(self.speed_changed)
        self.sterring_setter.valueChanged.connect(self.sterring_changed)
        self.sterring_gain_setter.valueChanged.connect(self.sterring_gain_changed)
        self.sterring_offset_setter.valueChanged.connect(self.sterring_offset_changed)


        #adding widgets
        self.layout.addWidget(self.auto_checkbox, 0, 0)
        self.layout.addWidget(self.label_manual, 1, 0)
        self.layout.addWidget(self.label_automatic, 1, 1)
        self.layout.addWidget(self.label_speed, 2, 0)
        self.layout.addWidget(self.auto_label_speed, 2, 1)
        self.layout.addWidget(self.speed_setter, 3, 0)
        self.layout.addWidget(self.auto_display_speed, 3, 1)
        self.layout.addWidget(self.label_steering, 4, 0)
        self.layout.addWidget(self.auto_label_steering, 4, 1)
        self.layout.addWidget(self.sterring_setter, 5, 0)
        self.layout.addWidget(self.auto_display_steering, 5, 1)
        self.layout.addWidget(self.label_steering_gain, 6, 0)
        self.layout.addWidget(self.auto_label_steering_gain, 6, 1)
        self.layout.addWidget(self.sterring_gain_setter, 7, 0)
        self.layout.addWidget(self.auto_display_steering_gain, 7, 1)
        self.layout.addWidget(self.label_steering_offset, 8, 0)
        self.layout.addWidget(self.auto_label_steering_offset, 8, 1)
        self.layout.addWidget(self.sterring_offset_setter, 9, 0)
        self.layout.addWidget(self.auto_display_steering_offset, 9, 1)


        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)




    def speed_changed(self, i):
        # car.throttle = i       #na platformie powinno zadziałac
        print(i)

    def sterring_changed(self, i):
        # car.steering = i       #na platformie powinno zadziałac
        print(i)

    def sterring_gain_changed(self, i):
        # car.steering_gain = i       #na platformie powinno zadziałac
        print(i)

    def sterring_offset_changed(self, i):
        # car.steering_offset = i       #na platformie powinno zadziałac
        print(i)

    def show_state(self, s):
        if(s == Qt.Checked):
            self.auto_display_steering_offset.setText("git")
            for setter in self.setters:
                 setter.blockSignals(True)
        else:
            self.auto_display_steering_offset.setText("")
            pass






app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

