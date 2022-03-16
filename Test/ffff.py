from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLabel
import sys


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.text_label1 = QLabel(self)
        self.text_label1.setText('car : ')

        self.text_label2 = QLabel(self)
        self.text_label2.setText('person : ')

        self.text_label3 = QLabel(self)
        self.text_label3.setText('traffic light : ')

        self.text_label4 = QLabel(self)
        self.text_label4.setText('traffic sign : ')

        self.text_label5 = QLabel(self)
        self.text_label5.setText('motor : ')

        self.text_label6 = QLabel(self)
        self.text_label6.setText('bike= : ')

        self.text_label7 = QLabel(self)
        self.text_label7.setText('truk : ')

        self.text_label8 = QLabel(self)
        self.text_label8.setText('rider : ')

        self.text_label9 = QLabel(self)
        self.text_label9.setText('bus : ')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.text_label1)
        self.vbox_layout.addWidget(self.text_label2)
        self.vbox_layout.addWidget(self.text_label3)
        self.vbox_layout.addWidget(self.text_label4)
        self.vbox_layout.addWidget(self.text_label5)
        self.vbox_layout.addWidget(self.text_label6)
        self.vbox_layout.addWidget(self.text_label7)
        self.vbox_layout.addWidget(self.text_label8)
        self.vbox_layout.addWidget(self.text_label9)



        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.vbox_layout, 4, 4, 4, 4)

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())