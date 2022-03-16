from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLabel
import sys


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.text_label = QLabel(self)
        self.text_label.setText('텍스트')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.text_label)

        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.vbox_layout, 4, 4, 4, 4)

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())