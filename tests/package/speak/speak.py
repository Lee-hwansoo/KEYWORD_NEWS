from gtts import gTTS, lang
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import os

def formclass1read(self):
    tts = gTTS("키워드 뉴스입니다. 선택 가능한 뉴스는 1번 중앙일보, 2번 한겨례, 3번 조선일보 입니다. 프로그램 종료는 0번을 누르세요.", lang='ko')
    if os.path.isfile('ui_1.mp3') == True:
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_1.mp3")))
        self.player.play()
    else:
        tts.save("ui_1.mp3")
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_1.mp3")))
        self.player.play()

def formclass2toformclass1(self):
    tts = gTTS("선택 가능한 뉴스는 1번 중앙일보, 2번 한겨례, 3번 조선일보 입니다. 프로그램 종료는 0번을 누르세요.", lang='ko')
    if os.path.isfile('ui_2_backform1.mp3') == True:
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_2_backform1.mp3")))
        self.player.play()
    else:
        tts.save("ui_2_backform1.mp3")
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_2_backform1.mp3")))
        self.player.play()

def formclass2read_num1(self,feed):
    tts = gTTS("분류를 고르세요. 다시듣기는 0번, 이전 화면은 백스페이스입니다." + ", 1번" + str(feed[0][0]) + ", 2번"+ str(feed[1][0]) + ", 3번 " + str(feed[2][0]) + ", 4번 " + str(feed[3][0]) + ", 5번 " + str(feed[4][0]) + ", 6번 " + str(feed[5][0]) + ", 7번 " + str(feed[6][0]) + ", 8번 " + str(feed[7][0]) + ", 9번 " + str(feed[8][0]), lang='ko')
    if os.path.isfile('ui_2_1.mp3') == True:
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_2_1.mp3")))
        self.player.play()
    else:
        tts.save("ui_2_1.mp3")
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_2_1.mp3")))
        self.player.play()

def formclass2read_num2(self,feed):
    tts = gTTS("분류를 고르세요. 다시듣기는 0번, 이전 화면은 백스페이스입니다." + ", 1번" + str(feed[0][0]) + ", 2번"+ str(feed[1][0]) + ", 3번 " + str(feed[2][0]) + ", 4번 " + str(feed[3][0]) + ", 5번 " + str(feed[4][0]) + ", 6번 " + str(feed[5][0]) + ", 7번 " + str(feed[6][0]) + ", 8번 " + str(feed[7][0]) + ", 9번 " + str(feed[8][0]), lang='ko')
    if os.path.isfile('ui_2_2.mp3') == True:
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_2_2.mp3")))
        self.player.play()
    else:
        tts.save("ui_2_2.mp3")
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_2_2.mp3")))
        self.player.play()

def formclass2read_num3(self,feed):
    tts = gTTS("분류를 고르세요. 다시듣기는 0번, 이전 화면은 백스페이스입니다." + ", 1번" + str(feed[0][0]) + ", 2번"+ str(feed[1][0]) + ", 3번 " + str(feed[2][0]) + ", 4번 " + str(feed[3][0]) + ", 5번 " + str(feed[4][0]) + ", 6번 " + str(feed[5][0]) + ", 7번 " + str(feed[6][0]) + ", 8번 " + str(feed[7][0]) + ", 9번 " + str(feed[8][0]), lang='ko')
    if os.path.isfile('ui_2_3.mp3') == True:
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_2_3.mp3")))
        self.player.play()
    else:
        tts.save("ui_2_3.mp3")
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_2_3.mp3")))
        self.player.play()

def formclass3read(self,title,keyword):
    tts = gTTS("제목은 " + str(title) + " 입니다." + "키워드는 " + str(keyword[0][0]) + " " + str(keyword[1][0]) + " " +  str(keyword[2][0]) + " " +  str(keyword[3][0]) + " " +  str(keyword[4][0]) + " 입니다.", lang='ko')
    if os.path.isfile('ui_3.mp3') == True:
        os.remove('ui_3.mp3')
    tts.save("ui_3.mp3")
    self.player = QMediaPlayer()
    self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_3.mp3")))
    self.player.play()

def formclass3readagain(self):
    self.player = QMediaPlayer()
    self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_3.mp3")))
    self.player.play()

def formclass3nexterror(self):
    tts = gTTS("마지막 기사입니다. 엔터를 눌러주세요", lang='ko')
    if os.path.isfile('ui_3_nexterror.mp3') == True:
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_3_nexterror.mp3")))
        self.player.play()
    else:
        tts.save("ui_3_nexterror.mp3")
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_3_nexterror.mp3")))
        self.player.play()

def formclass3preverror(self):
    tts = gTTS("이전 기사가 없습니다. 엔터를 눌러주세요", lang='ko')
    if os.path.isfile('ui_3_preverror.mp3') == True:
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_3_preverror.mp3")))
        self.player.play()
    else:
        tts.save("ui_3_preverror.mp3")
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_3_preverror.mp3")))
        self.player.play()

def formclass4read(self,text):
    tts = gTTS("선택하신 기사의 원문입니다. " + str(text) + "   기사가 끝났습니다. 다시 듣기는 0번입니다.", lang='ko')
    if os.path.isfile('ui_4.mp3') == True:
        os.remove('ui_4.mp3')
    tts.save("ui_4.mp3")
    self.player = QMediaPlayer()
    self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_4.mp3")))
    self.player.play()

def formclass4readagain(self):
    self.player = QMediaPlayer()
    self.player.setMedia(QMediaContent(QUrl.fromLocalFile("ui_4.mp3")))
    self.player.play()

def speakcancel(self):
    self.player = QMediaPlayer()
    self.player.stop()

