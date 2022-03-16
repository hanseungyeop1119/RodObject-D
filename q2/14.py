from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QFileDialog, QGroupBox, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
import sys
import QZmodel


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('이미지 분류 AI')
        self.model = QZmodel.QZModel()
        self.text_label1 = QLabel(self)

        # self.text_label = QLabel(self)
        # self.text_label.setText1('car                : ', ,'%')
        # self.text_label.setText2('person             :', ,'%')
        # self.text_label.setText3('traffic light      :', ,'%')
        # self.text_label.setText4('traffic sign       :', ,'%')
        # self.text_label.setText7('bike               :', ,'%')
        # self.text_label.setText8('truk               :', ,'%')
        # self.text_label.setText9('rider              :', ,'%')
        # self.text_label.setText10('bus                :', ,'%')

        self.group_box = QGroupBox('메뉴')
        self.group_box2 = QGroupBox('이미지')
        self.group_box3 = QGroupBox('분류 예측')

        self.image_label = QLabel(self)
        pixmap = QPixmap()
        self.image_label.setPixmap(pixmap)

        self.button1 = QPushButton('이미지 불러오기')
        self.button1.clicked.connect(self.button1_click)

        self.button2 = QPushButton('데이터 불러오기')
        self.button2.clicked.connect(self.button2_click)

        self.button3 = QPushButton('모델 저장')
        self.button3.clicked.connect(self.button3_click)

        self.button4 = QPushButton('모델 불러오기')
        self.button4.clicked.connect(self.button4_click)

        self.button5 = QPushButton('이미지 예측')
        self.button5.clicked.connect(self.button5_click)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.image_label)
        self.group_box2.setLayout(self.vbox_layout)

        self.vbox_layout2 = QVBoxLayout()
        self.vbox_layout2.addWidget(self.text_label1)
        self.group_box3.setLayout(self.vbox_layout2)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)
        self.hbox_layout.addWidget(self.button3)
        self.hbox_layout.addWidget(self.button4)
        self.hbox_layout.addWidget(self.button5)
        self.group_box.setLayout(self.hbox_layout)


        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.hbox_layout, 0, 0, 1, 1)
        self.main_layout.addWidget(self.group_box, 0, 0, 1, 3)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 2)
        self.main_layout.addWidget(self.group_box3, 1, 2, 1, 1)
        self.main_layout.addLayout(self.vbox_layout2, 4, 4, 4, 4)


        self.setLayout(self.main_layout)

    def button1_click(self):
        # ''(제목), '.'(경로)
        #self.path, _ = QFileDialog.getOpenFileName(self, '이미지', '../classification_data', '이미지 Files (*jpg *.png)')
        self.path, _ = QFileDialog.getOpenFileName(self, '이미지', 'C:/Ai image', '이미지 Files (*jpg *.png)')
        pixmap = QPixmap(self.path)
        self.image_label.setPixmap(pixmap)

    def button2_click(self):
        self.model.load_data()

    def button3_click(self):
        self.model.save()
        print('모델 저장 완료')

    def button4_click(self):
        #self.model.build()
        #self.model.train()
        self.model.load()
        print()

    def button5_click(self):
        predict = self.model.predict(self.path)

        self.text_label1.setText(predict)
        # self.text_label.setText2(':')
        # self.text_label.setText3(':')
        # self.text_label.setText4(':')
        # self.text_label.setText7(':')
        # self.text_label.setText8(':')
        # self.text_label.setText9(':')
        # self.text_label.setText10(':')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())
