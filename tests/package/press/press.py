# news[0][0] ~ news[8][2]
# 중앙일보 1번
def Joongang():
    news = [
        ['전체 기사','https://rss.joins.com/joins_news_list.xml'],
        ['주요 기사','https://rss.joins.com/joins_homenews_list.xml'],
        ['인기기사','https://rss.joins.com/sonagi/joins_sonagi_total_list.xml'],
        ['경제','https://rss.joins.com/joins_money_list.xml'],
        ['생활','https://rss.joins.com/joins_life_list.xml'],
        ['정치','https://rss.joins.com/joins_politics_list.xml'],
        ['IT소식','https://rss.joins.com/joins_it_list.xml'],
        ['문화','https://rss.joins.com/joins_culture_list.xml'],
        ['스포츠','https://rss.joins.com/joins_sports_list.xml']
    ]
    return news

# 한겨레 2번
def hankyoreh():
    news = [
        ['전체 기사','https://www.hani.co.kr/rss/'],
        ['주요 기사','https://www.hani.co.kr/rss/lead/'],
        ['인기기사','https://www.hani.co.kr/rss/newsrank/'],
        ['경제','https://www.hani.co.kr/rss/economy/'],
        ['사회','https://www.hani.co.kr/rss/society/'],
        ['정치','https://www.hani.co.kr/rss/politics/'],
        ['과학','https://www.hani.co.kr/rss/science/'],
        ['문화','https://www.hani.co.kr/rss/culture/'],
        ['스포츠','https://www.hani.co.kr/rss/science/']
    ]
    return news

# 조선일보 3번
def chosun():
    news = [
        ['속보','https://fs.jtbc.joins.com/RSS/newsflash.xml'],
        ['정치','https://fs.jtbc.joins.com/RSS/politics.xml'],
        ['경제','https://fs.jtbc.joins.com/RSS/economy.xml'],
        ['사회','https://fs.jtbc.joins.com/RSS/society.xml'],
        ['국제','https://fs.jtbc.joins.com/RSS/international.xml'],
        ['문화','https://fs.jtbc.joins.com/RSS/culture.xml'],
        ['연예','https://fs.jtbc.joins.com/RSS/entertainment.xml'],
        ['스포츠','https://fs.jtbc.joins.com/RSS/sports.xml'],
        ['뉴스랭킹','https://fs.jtbc.joins.com/RSS/newsrank.xml']
    ]
    return news

def press(num):
    if num == 1:
        return Joongang()
    elif num == 2:
        return hankyoreh()
    else:
        return chosun()

def press_num():
    num = int(input("1: 중앙일보\n2: 한겨레\n3: 조선일보\n뉴스를 선택 해주세요\n"))

    while (num > 3) or (num < 1) :
        print('올바른 숫자를 입력해주세요')
        num = int(input(""))
    
    return num