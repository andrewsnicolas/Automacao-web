from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui
import requests
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
serviço = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service= serviço, options= chrome_options)
#Daqui pra cima tem q copiar a mesma coisa em todos os códigos

navegador.get('https://suap.ifsp.edu.br/accounts/login/?next=/')
#Vai na página inicial do estudante do IF

navegador.find_element(By.ID, 'id_username').send_keys('xxxxxxx') 
#Procura a parte de colocar o aluno e digita o CB

navegador.find_element(By.ID, 'id_password').send_keys('xxxxx') 
#Procura o elemento para colocar a senha do aluno

navegador.find_element(By.XPATH, '//*[@id="login"]/form/div[5]/input').click() 
#Procura o botão "acessar", em seguida clica

navegador.get('https://suap.ifsp.edu.br/edu/emitir_boletim_pdf/1038842/')
#Gera o link do boletim do aluno

#retorno = requests.get('https://suap.ifsp.edu.br/edu/emitir_boletim_pdf/1038842/')
#Com o requests, nós pegamos todo o conteúdo html do nosso site
#with open('meu_boletim.pdf', "wb") as arquivo:
#com o with, transformamos o conteúdo em um arquivo binário para formarmos um pdf
       # arquivo.write(retorno.content) 



#navegador.find_element(By.XPATH, '/html/body/pdf-viewer//viewer-toolbar//div/div[3]/viewer-download-controls//cr-icon-button//div/iron-icon').click()
#Baixa o arquivo
#with open('cleiton.txt')