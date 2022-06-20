import requests
import bs4


base_url = 'https://habr.com'
url = base_url + '/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {'Accept-Language': 'ru-RU,ru;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Cache-Control': 'max-age=0',
    'Cookie': '_ym_d=1628840683; _ym_uid=1628840683355101683; _ga=GA1.2.137596937.1628841988; fl=ru; hl=ru; feature_streaming_comments=true; _gid=GA1.2.1021543475.1641571984; habr_web_home=ARTICLES_LIST_ALL; _ym_isad=1; visited_articles=599735:203282; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1',
    'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36'}


response = requests.get(base_url, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    title = article.h2.a.text
    post = article.div.div.text
    href_l = article.find(class_="tm-article-snippet__title-link").attrs['href']
    date = article.find('time').text

    for key_w in KEYWORDS:
        if key_w in title or (key_w in post):
            print(f'{date} - {title} - {base_url}{href_l}')




