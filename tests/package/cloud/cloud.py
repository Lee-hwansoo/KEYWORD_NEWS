from wordcloud import WordCloud
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure

wc = WordCloud(font_path="c:\\windows\\fonts\\malgun.ttf",background_color="white",width=740, height=300, max_font_size=60)

def keywordcloud(nouns):
    cloud = wc.generate_from_frequencies(dict(nouns))
    cloud.to_file('keywordcloud.jpg')

    # self.fig = plt.Figure(figsize=[7.4, 3])
    # self.ax = self.fig.add_subplot(111)

    # self.ax.clear()
    # self.canvas = FigureCanvas(self.fig)
    # self.cloudview.addWidget(self.canvas)


    # self.canvas.draw()
    # self.canvas.show()

    
    # 기본 wordcloud
    # plt.figure(figsize=(7.4, 3))
    # plt.axis('off')
    # plt.imshow(cloud)
    # plt.show()

def showcloud(self):
    self.cloud = QPixmap('keywordcloud.jpg')
    self.cloudview.setPixmap(self.cloud)
