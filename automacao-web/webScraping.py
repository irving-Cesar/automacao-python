# !pip install selenium

# instalação do chrome webdriver necessária. Versão usada: 101.0.4951.54 (Versão oficial) 32 bits
# Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing

from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador_chrome = wb.Chrome()

# handles = navegador_chrome.window_handles 
  
# for h in handles: 
#     navegador_chrome.switch_to.window(h) 

#     if navegador_chrome.title == 'Configurações':
#         navegador_chrome.close()
        

arr_cotacoes = ['dolar', 'euro', 'ouro']

xPath_google = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
for ac in arr_cotacoes:
    navegador_chrome.get('https://www.google.com.br/')
    busca = navegador_chrome.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    busca.send_keys('Cotação {}'.format(ac))
    busca.send_keys(Keys.ENTER)
    if ac == 'dolar':
        dolar_cotacao = navegador_chrome.find_element(By.XPATH, xPath_google).get_attribute('data-value')
    elif ac == 'euro':
        euro_cotacao = navegador_chrome.find_element(By.XPATH, xPath_google).get_attribute('data-value')
    elif ac == 'ouro':
        navegador_chrome.get('https://www.melhorcambio.com/ouro-hoje#:~:text=O%20valor%20do%20grama%20do,em%20R%24%20299%2C71.')
        ouro_cotacao = navegador_chrome.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
        ouro_cotacao = ouro_cotacao.replace(',', '.')

print(dolar_cotacao)
print(euro_cotacao)
print(ouro_cotacao)

dolar_cotacao = float(dolar_cotacao)
euro_cotacao = float(euro_cotacao)
ouro_cotacao = float(ouro_cotacao)

navegador_chrome.quit()

tabela = pd.read_excel('Produtos.xlsx')

# atualizando valores: Moeda
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(dolar_cotacao)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(euro_cotacao)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(ouro_cotacao)

# atualizando valores: preço Compras
tabela['Preço de Compra'] = (tabela['Preço Original'] * tabela['Cotação'])

# atualizando valores: preço Venda
tabela['Preço de Venda'] = (tabela['Preço de Compra'] * tabela['Margem']).map('{:.2f}'.format)

display(tabela)

tabela.to_excel('Produtos Novos.xlsx', index=False)


print('TABELA ATUALIZADA:')

tabela_nova = pd.read_excel('Produtos Novos.xlsx')

display(tabela_nova)
