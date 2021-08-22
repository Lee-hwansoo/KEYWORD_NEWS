# python == 3.7.9
# java version "16.0.2" 2021-07-20
# Java(TM) SE Runtime Environment (build 16.0.2+7-67)
# Java HotSpot(TM) 64-Bit Server VM (build 16.0.2+7-67, mixed mode, sharing)
# win10 64bit
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from package.press import press
from package.crawling import crawling
from package.word import word
from package.cloud import cloud
from package.speak import speak

form_class_1 = uic.loadUiType("./tests/1.ui")[0]
form_class_2 = uic.loadUiType("./tests/2.ui")[0]
form_class_3 = uic.loadUiType("./tests/3.ui")[0]
form_class_4 = uic.loadUiType("./tests/4.ui")[0]

class Main(QMainWindow, form_class_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_1.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_1.clicked.connect(lambda :self.Qpress_num(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_2.clicked.connect(lambda :self.Qpress_num(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_3.clicked.connect(lambda :self.Qpress_num(self.pushButton_3))
        self.pushButton_prev.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_prev.clicked.connect(lambda :self.close())
        speak.formclass1read(self)

    def Qpress_num(self,button):
        num = int(button.text())
        feed = press.press(num)
        self.dialog = Index(self,feed,num)
        self.dialog.show()
        

class Index(QMainWindow, form_class_2):
    def __init__(self,parent=None,feed=None,num=None):
        super(Index,self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal) # qtcore로 window 모달
        self.label_1.setText(str(feed[0][0]))
        self.label_2.setText(str(feed[1][0]))
        self.label_3.setText(str(feed[2][0]))
        self.label_4.setText(str(feed[3][0]))
        self.label_5.setText(str(feed[4][0]))
        self.label_6.setText(str(feed[5][0]))
        self.label_7.setText(str(feed[6][0]))
        self.label_8.setText(str(feed[7][0]))
        self.label_9.setText(str(feed[8][0]))
        self.pushButton_0.clicked.connect(lambda :self.onemore(num,feed))
        self.pushButton_1.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_1.clicked.connect(lambda :self.Qcrawling(feed,self.pushButton_1,num))
        self.pushButton_2.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_2.clicked.connect(lambda :self.Qcrawling(feed,self.pushButton_2,num))
        self.pushButton_3.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_3.clicked.connect(lambda :self.Qcrawling(feed,self.pushButton_3,num))
        self.pushButton_4.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_4.clicked.connect(lambda :self.Qcrawling(feed,self.pushButton_4,num))
        self.pushButton_5.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_5.clicked.connect(lambda :self.Qcrawling(feed,self.pushButton_5,num))
        self.pushButton_6.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_6.clicked.connect(lambda :self.Qcrawling(feed,self.pushButton_6,num))
        self.pushButton_7.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_7.clicked.connect(lambda :self.Qcrawling(feed,self.pushButton_7,num))
        self.pushButton_8.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_8.clicked.connect(lambda :self.Qcrawling(feed,self.pushButton_8,num))
        self.pushButton_9.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_9.clicked.connect(lambda :self.Qcrawling(feed,self.pushButton_9,num))
        self.pushButton_prev.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_prev.clicked.connect(lambda :self.close())
        self.pushButton_prev.clicked.connect(lambda :speak.formclass2toformclass1(parent))
        if num == 1:
            speak.formclass2read_num1(self,feed)
        elif num == 2:
            speak.formclass2read_num2(self,feed)
        else:
            speak.formclass2read_num3(self,feed)

    def Qcrawling(self,feed,button,num):
        select = int(button.text()) - 1
        title = feed[select][0]
        url = crawling.feed_link(feed,select)
        self.dialog = Keywords(self,title,url,num,feed)
        self.dialog.show()

    def onemore(self,num,feed):
        speak.speakcancel(self)
        if num == 1:
            speak.formclass2read_num1(self,feed)
        elif num == 2:
            speak.formclass2read_num2(self,feed)
        else:
            speak.formclass2read_num3(self,feed)        

class Keywords(QMainWindow, form_class_3):
    
    def __init__(self,parent=None,title=None,url=None,num=None,feed=None):
        super(Keywords,self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.label_index.setText(title)
        self.news_num = 0
        self.aritcle = crawling.get_news(url,self.news_num)
        self.titleBrowser.setText(self.aritcle.title)
        self.nouns_most = word.importance(self.aritcle)
        self.pushButton_0.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_0.clicked.connect(lambda :self.onemore())
        self.pushButton_4.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_4.clicked.connect(lambda :self.prev(url))
        self.pushButton_5.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_5.clicked.connect(lambda :self.now(title))
        self.pushButton_6.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_6.clicked.connect(lambda :self.next(url))
        self.pushButton_prev.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_prev.clicked.connect(lambda :self.close())
        if num == 1:
            self.pushButton_prev.clicked.connect(lambda :speak.formclass2read_num1(parent,feed))
        elif num == 2:
            self.pushButton_prev.clicked.connect(lambda :speak.formclass2read_num2(parent,feed))
        else:
            self.pushButton_prev.clicked.connect(lambda :speak.formclass2read_num3(parent,feed))
        cloud.keywordcloud(self.nouns_most)
        cloud.showcloud(self)
        speak.formclass3read(self,self.aritcle.title,self.nouns_most)

    # 마지막 end of list 에러 처리
    def next(self,url):
        try:
            self.news_num+=1
            self.aritcle = crawling.get_news(url,self.news_num)
            self.titleBrowser.setText(self.aritcle.title)
            self.nouns_most = word.importance(self.aritcle)
            cloud.keywordcloud(self.nouns_most)
            cloud.showcloud(self)
            speak.formclass3read(self,self.aritcle.title,self.nouns_most)
        except IndexError:
            speak.formclass3nexterror(self)
            msgBox = QMessageBox()
            msgBox.setWindowTitle("KEYWORDNEWS")
            #msgBox.setWindowIcon(QtGui.QPixmap("info.png")) # 메세지창의 상단 icon 설정
            #msgBox.setWindowIcon(QtGui.QIcon('PathToIcon/icon.png')) # 위에거나 아래거
            #self.label.setFont(QFont("Sanserif", 14)) # 라벨설정 # from PyQt5.QtGui import QIcon, QFont
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("경고")
            msgBox.setInformativeText("마지막 기사입니다.\n엔터를 눌러주세요.")
            msgBox.setStandardButtons(QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Cancel)
            msgBox.exec_()

    # list의 최소범위 에러 처리
    def prev(self,url):
        if self.news_num != 0:
            self.news_num-=1
            self.aritcle = crawling.get_news(url,self.news_num)
            self.titleBrowser.setText(self.aritcle.title)
            self.nouns_most = word.importance(self.aritcle)
            cloud.keywordcloud(self.nouns_most)
            cloud.showcloud(self)
            speak.formclass3read(self,self.aritcle.title,self.nouns_most)
        else:
            speak.formclass3preverror(self)
            msgBox = QMessageBox()
            msgBox.setWindowTitle("KEYWORDNEWS")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("경고")
            msgBox.setInformativeText("이전 기사가 없습니다.\n엔터를 눌러주세요.") 
            msgBox.setStandardButtons(QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Cancel)
            msgBox.exec_()

    def now(self,title):
        self.dialog = Newspaper(self,title,self.aritcle)
        self.dialog.show()

    def onemore(self):
        speak.formclass3readagain(self)

class Newspaper(QMainWindow, form_class_4):
    
    def __init__(self,parent=None,title=None,article=None):
        super(Newspaper,self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.label_index.setText(title)
        self.titleBrowser.setText(article.title)
        self.textBrowser.setText(article.text)
        self.pushButton_0.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_0.clicked.connect(lambda :self.onemore())
        self.pushButton_prev.clicked.connect(lambda :speak.speakcancel(self))
        self.pushButton_prev.clicked.connect(lambda :self.close())
        speak.formclass4read(self,article.text)

    def onemore(self):
        speak.formclass4readagain(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    KEYWORDNEWS = Main()
    KEYWORDNEWS.show()
    app.exec_()