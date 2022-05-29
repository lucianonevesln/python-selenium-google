from selenium import webdriver
import pyautogui
import time

# input que deve ser preenchido pelo usuario no console
busca = input('Buscar no Google: ')
time.sleep(2)

# acionando o driver de conexao
navegador = webdriver.Chrome()
time.sleep(2)

# informando o site que sera utilizado
navegador.get('https://www.google.com.br/')
time.sleep(2)

# informando onde a aplicacao deve interagir com o site
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(f'{busca}')
time.sleep(2)

# informando onde a aplicacao deve interagir com o site atrave de clique para limitar a busca
navegador.find_element_by_xpath('/html/body/div[1]/div[2]/div/img').click()
time.sleep(2)

# clique em botao desejado para finalizar a busca
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
time.sleep(2)

# aumento de tamanho de tela
pyautogui.click(x=979, y=25)