import pyautogui
import time
# Passo a passo do projeto
# Passo 1 : Entrar no sistema da Empresa

    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.5

# abrir o chrome :
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(5)

# Passo 2 : Fazer Login
#Login:
pyautogui.click(x=930, y=365)
pyautogui.write("felipeluizcunha2003@gmail.com")

#Senha:
pyautogui.press("tab")
pyautogui.write("s04b30100")

#Confirmar login e entrar:
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3 : Importar a base de dados de produtos
# pip install pandas numpy openpyx1
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria  = tabela.loc[linha, "categoria"]
    preco_unitario  = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]


    # Passo 4 : Cadastrar 1 produto
    pyautogui.click(x=775, y=247)


    # Preencher os campos
    pyautogui.write(str (codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # Com tudo preenchido só enviar :

    pyautogui.press("tab")
    pyautogui.press("enter")


    pyautogui.scroll(1000)

# Passo 5 : Repetir o cadastro para todos os produtos

