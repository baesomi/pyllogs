import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyllogs.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_btn.clicked.connect(self.open_file)
        self.submit_btn.clicked.connect(self.submit_file)
        self.input_src = ""

    def open_file(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label_file_name.setText(fname[0])

    def submit_file(self):
        # TODO : 입력 값 저장 및 파일 저장
        # TODO : 정규식 validation check
        # TODO : 로그 처리 로직
        self.label_file_name.setText()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mWindow = MainWindow()
    mWindow.show()

    app.exec_()
