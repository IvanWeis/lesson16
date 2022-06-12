import pprint
                # ЗДЕСЬ ДЛЯ СПРАВКИ КОД ИЗ ПРОГРАММЫ parser HTML
import requests
from bs4 import BeautifulSoup

domain = 'https://pythondigest.ru'
url = f'{domain}/feed/'
# print(url)
response = requests.get(url) # результат запроса в виде текста страницы помещаем в переменную response
soup = BeautifulSoup(response.text, 'html.parser') # делаем суп, из которого будем вытаскивать новости
#print(soup)  # для проверки
news_a = soup.find_all('div', class_ = 'news-line-item') # в классе находим ВСЕ теги div, содержащие новости
#pprint.pprint(news_a)  # для проверки
file_news = [] # создаем переменную, в которой будут храниться найденные
# новости в формате, удобном для записи в файл
for one_news_a in news_a:
    text = one_news_a.text
    file_news.append(text)
    #print(text)
    #print(type(text))

print(file_news) # для проверки