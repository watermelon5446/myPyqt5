import sys 
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') #창의 제목
        self.move(300, 300)
        self.resize(400, 200) # (너비,높이)
        self.show() # 위젯을 스크린에 보여줌


if __name__ == '__main__': #직접 실행하는지 모듈로 하는지 확인
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())