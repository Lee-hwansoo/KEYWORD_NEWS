# NLP  (Natural Language Processing, 자연어처리)
# KoNLPy (Korean natural language processing) 패키지 중 okt 라이브러리 사용 (java)
# konlpy : PySocks, oauthlib, requests-oauthlib, tweepy, numpy, JPype1, beautifulsoup4, konlpy 설치됨
# mecab 설치
# https://hong-yp-ml-records.tistory.com/91
from konlpy.tag import Mecab
from collections import Counter

mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")

def importance(article):
    nouns = mecab.nouns(article.text)
    nouns = [n for n in nouns if len(n) > 1]
    count = Counter(nouns)
    nouns_most = count.most_common(20)
    return nouns_most