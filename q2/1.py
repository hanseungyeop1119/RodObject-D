from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QGroupBox, QLabel, QVBoxLayout
import sys


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.group_box = QGroupBox('그룹1')
        self.group_box2 = QGroupBox('그룹2')

        self.button1 = QPushButton('-')
        self.button2 = QPushButton('+')

        self.text_label = QLabel(self)
        self.text_label.setText('3')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.text_label)

        self.group_box2.setLayout(self.text_label)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)

        self.group_box.setLayout(self.hbox_layout)
        self.group_box.setLayout(self.hbox_layout)

        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.hbox_layout, 0, 0, 1, 1)
        self.main_layout.addWidget(self.group_box, 0, 0, 1, 0)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 1)
        self.main_layout.addLayout(self.vbox_layout, 0, 0, 1, 1)

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())