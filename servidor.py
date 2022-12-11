from flask import Flask, request, render_template
from selenium import webdriver
import time


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def buscador():
    time.sleep(2)
    busca = request.form.get['id_palavra']
    time.sleep(2)
    navegador = webdriver.Chrome()
    #time.sleep(2)
    #navegador.get('https://www.gov.br/receitafederal/pt-br')
    #time.sleep(2)
    #navegador.find_element_by_xpath('//*[@id="searchtext-input"]').send_keys(f'{busca}')
    #time.sleep(2)
    #navegador.find_element_by_xpath('//*[@id="searchtext-label"]/button').click()


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, debug = True)