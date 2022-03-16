from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QFileDialog, QGroupBox, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
import sys
import cv2

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('아아아')

        self.group_box = QGroupBox('그룹1')
        self.group_box2 = QGroupBox('그룹2')

        self.image_label = QLabel(self)
        pixmap = QPixmap()
        self.image_label.setPixmap(pixmap)

        self.button1 = QPushButton('파일 열기')
        self.button1.clicked.connect(self.button1_click)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.image_label)
        self.group_box2.setLayout(self.vbox_layout)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.group_box.setLayout(self.hbox_layout)


        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.hbox_layout, 0, 0, 1, 1)
        self.main_layout.addWidget(self.group_box, 0, 0, 1, 0)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 0)
        self.main_layout.addLayout(self.vbox_layout, 4, 4, 4, 4)

        self.setLayout(self.main_layout)


    def button1_click(self):
        # ''(제목), '.'(경로)
        path, _ = QFileDialog.getOpenFileName(self, '이미지', '../data/images', '이미지 Files (*jpg *.png)')
        pixmap = QPixmap(path)

        self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())