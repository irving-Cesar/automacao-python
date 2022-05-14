# !pip install pyautogui
# !pip install pyperclip

# RESOLUÇÃO DA TELA USADA: 1366 x 768

import pandas as pd # leitor para a tabela
import pyautogui # automação do teclado/mouse
import pyperclip # ajudar com a leitura de caracteres especiais
import time

# pause para fazer os processos. 1 seg
pyautogui.PAUSE = 1

# acessar o site da "empresa"
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=391, y=268, clicks = 2) # clicar na aba "exportar"

time.sleep(2) # tempo para carregar a aba

pyautogui.click(x=391, y=268, button='right') # clicar com o btn direito no arquivo
pyautogui.click(x=497, y=645) # fazer download do arquivo

time.sleep(15) # tempo estimado para a finalização do download do arquivo

tabela = pd.read_excel(r'C:\Users\userTest\Downloads\Vendas - Dez.xlsx') # receber valores do arquivo (.xlsx)

# somandos valores
faturamento = tabela['Valor Final'].sum()
quantidade_produtos = tabela['Quantidade'].sum()

display(tabela) # mostrar tabela
# print('Valor final {:.2f}, quantidade {} '.format(faturamento, quantidade_produtos))

# acessar e-mail
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox') # É preciso estar logado
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x=119, y=174) # clicar em "escrever" novo e-mail
time.sleep(4)

pyautogui.write('pythonAutoEmailTeste@gmail.com')
pyautogui.press('tab') # selecionar email
pyautogui.press('tab') # pular para assunto
time.sleep(1)
pyperclip.copy('Relatório de vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

text = """Prezados, boa tarde!

O Faturamento de ontem foi de R$ {:,.2f}
E a Quantidade de produtos vendidos foi de {:,}

Atenciosamente,
pythonTeste.
""".format(faturamento, quantidade_produtos)

pyautogui.write(text)

time.sleep(3)
pyautogui.click(x=855, y=693) # clicar em "Enviar" e-mail
