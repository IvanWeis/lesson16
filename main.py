from flask import Flask, render_template, request
import requests  # чтобы работали запросы
from bs4 import BeautifulSoup  # чтобы работал  суп
               # ЭТО КОНТРОЛЛЕР - здесь происходит вся обработка)
app = Flask(__name__)  # создал приложение

@app.route("/")
def index():   # функция Контроллер Главной страницы
    return render_template('index.html') # рендерит шаблон index.html

@app.route("/contacts/")
def contacts(): # страница с контактами
    developer_name = 'Ivan Weis'
    return render_template('contacts.html', name=developer_name) # рендерит шаблон contacts.html

@app.route("/forma/", methods=['GET'])
def forma_get(): # страница с Формой для отправки  GET-запроса
    return render_template('forma.html')

@app.route("/forma/", methods=['POST'])
def forma_post(): # страница с Формой для отправки POST-запроса
    url = request.form.get('input_text') # получаем URL из элемента input Формы
    response = requests.get(url) # результат запроса в виде текста страницы помещаем в переменную response
    soup = BeautifulSoup(response.text, 'html.parser') # делаем суп, из которого будем вытаскивать новости
    news_a = soup.find_all('div', class_ = 'news-line-item') # в классе находим ВСЕ теги div, содержащие новости
    data1 = [] # создаем переменную, в которой будут храниться найденные новости
    for one_news_a in news_a:  # пробегаем по новостям и складываем в data1
        text = one_news_a.text
        data1.append(text)
#   return render_template('forma.html')
    return render_template('results.html', data=data1) # выводим страницу с помощью темплета results.html
                           # передаем в страницу данные из переменной data1
# @app.route("/results/")
# def results(): # страница с выводом результатов
#     data = ['Анализ а мы у каждого аудиосигнала.', 'Ускоряем работало отменно, но, ']
#     return render_template('results.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)  # запускаем приложение на тестовом сервере debug=True - чтобы показывал ошибки