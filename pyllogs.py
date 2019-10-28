import sys, logging, RegexGroup
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyllogs.ui")[0]


# TODO : 정규식 입력 예시 추가 ? 버튼

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_btn.clicked.connect(self.open_file)
        self.submit_btn.clicked.connect(self.submit_file)
        self.input_src = ""


    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "",
                                            "All Files(*);; Log Files(*.txt, *.log)", '/Documents')
        if fname[0]:
            self.input_src = fname[0]  # 파일 full path 저장
            self.label_file_name.setText(fname[0])


    def submit_file(self):
        logging.info("group1  " + self.group1_input.toPlainText())
        logging.info("group2  " + self.group2_input.toPlainText())
        logging.info("group3  " + self.group3_input.toPlainText())
        logging.info("group4  " + self.group4_input.toPlainText())
        logging.info("group5  " + self.group5_input.toPlainText())

        if self.input_src == "":
            QMessageBox.about(self, "Warning", "파일을 선택하지 않았습니다.")
        elif not self.check_valid_regnum():
            QMessageBox.about(self, "Warning", "정규식 그룹은 최소 3개 이상 입력해주세요.")
        elif not self.check_valid_opt():
            QMessageBox.about(self, "Warning", "level과 time을 다르게 체크해주세요.")
        else:
            parse_src(self)

    # 정규식 최소 input 갯수 validation
    def check_valid_regnum(self):
        count = 0
        input_list = [self.group1_input, self.group2_input, self.group3_input, self.group4_input, self.group5_input]

        for n_input in input_list:
            if n_input.toPlainText() != "":
                count += 1

        if count < 3:
            return False

        return True

    # 옵션 check validation
    def check_valid_opt(self):
        time_list = [self.time_group1, self.time_group2, self.time_group3, self.time_group4, self.time_group5]
        level_list = [self.level_group1, self.level_group2, self.level_group3, self.level_group4, self.level_group5]

        for (time, level) in zip(time_list, level_list):
            if time.isChecked() is True and level.isChecked() is True:
                return False

        return True


def parse_src(self):
    logging.debug("pyllogs.parse_src START")
    # time, level, content1, content2, content3 순으로
    # TODO : timestamp,level 체크





if __name__ == "__main__":
    app = QApplication(sys.argv)
    mWindow = MainWindow()
    mWindow.show()
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
    logging.debug('Start of program')
    app.exec_()
