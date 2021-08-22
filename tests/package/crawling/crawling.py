# feed 분석기와 newspaper article
import feedparser
from newspaper import Article

# num <= 9 장르 선택
def feed_link(rss,num):
    feeds = feedparser.parse(rss[num][1])
    links = [entry['link'] for entry in feeds['entries']]
    return links

def get_news(url,num):
    article = Article(url[num], language='ko')
    article.download()
    article.parse()
    return article