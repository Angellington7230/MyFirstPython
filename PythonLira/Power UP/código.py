# PASSO 1: Entrar no sistema da empresa
# PASSO 2: Fazer o Login
# PASSO 3: Importar a base de dados
# PASSO 4: Cadastrar o produto
# PASSO 5: Repetir até acabar

from operator import index
import pyautogui

import time

import pandas

pyautogui.PAUSE = 0.5

link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/tabela")

# Abre o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

time.sleep(0.5)

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(1)

#Fazer o Login
#pyautogui.click(x=195, y=415)
#time.sleep(1)
#pyautogui.write("anjodeneve@gmail.com")
#time.sleep(1)
#pyautogui.press("tab")
#pyautogui.write("123456")
#pyautogui.click(x=334, y=567)

time.sleep(2)

#Importar Dados

tabela = pandas.read_csv("produtos.csv")


# # Para cada linha da minha tabela

for linha in tabela.index:
    #Cadastrar 1 produto
    pyautogui.click(x=343, y=387)

    #codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    #marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    
    #tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    
    #categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    #preço unitario do produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    #custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    #Obs
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    pyautogui.press("enter")

