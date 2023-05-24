import pywhatkit
import pandas as pd
import pyautogui
import sys
df=pd.read_excel("contatos.xlsx")
lista=list(df["numeros"])
txt=open("mensagem.txt")
mensagem=txt.read()
f = open("PyWhatKit_DB.txt","w")
f.close()

for i in lista:
    i=str(str("+")+str(i))
    pywhatkit.sendwhatmsg_instantly(i,mensagem,5, tab_close=True)
    x, y = pyautogui.position()
    if (x == 0 and y == 0):
        sys.exit()




