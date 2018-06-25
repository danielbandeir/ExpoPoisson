# -*- coding: utf-8 -*-

import statistics
from expovariate import *
from tkinter import *
from tkinter import messagebox
from poisson import *


def deleteText(text, text2):
    entryLambda.delete(0, END)
    entrySampleSpace.delete(0, END)

def insertTextLambdaFirst(text):
    entryMeanFirst.delete(0, END)
    entryMeanFirst.insert(0, text)

def insertTextLambdaSecond(text):
    entryMeanSecond.delete(0, END)
    entryMeanSecond.insert(0, text)

def insertTextVarianceFirst(text):
    entryVarianceFirst.delete(0, END)
    entryVarianceFirst.insert(0, text)

def insertTextVarianceSecond(text):
    entryVarianceSecond.delete(0, END)
    entryVarianceSecond.insert(0, text)

def bt_onClick():
    if (str(entrySampleSpace.get()).isnumeric()) and (str(entryLambda.get()).isnumeric()):
        num1 = float(entryLambda.get())
        num2 = int(entrySampleSpace.get())

        calFirst = exp.calcExpovariate(num1,num2)
        calSecond = exp.calcExpovariateSimulation(num1, num2)

        entryMeanFirst["text"] = insertTextLambdaFirst(statistics.mean(calFirst))
        entryMeanSecond["text"] = insertTextLambdaSecond(statistics.mean(calSecond))
        entryVarianceFirst["text"] = insertTextVarianceFirst(statistics.variance(calFirst))
        entryVarianceSecond["text"] = insertTextVarianceSecond(statistics.variance(calSecond))

        exp.plotHist()
    else:
        messagebox.showerror("Erro", "Valores inválidos ou Campo em Branco. Digite novamente")
        deleteText(entrySampleSpace, entryLambda)

def bt_ladder():
        test = entryArchivePoisson.get()
        pos.importPoisson(test)
        pos.plotGraphic()


GUI = Tk()
pos = poisson()
exp = expovariate()

labelLambda = Label(GUI, text="Digite o valor de Lambda")
labelLambda.place(x=50, y=20)

entryLambda = Entry(GUI)
entryLambda.place(x=60, y=50)


labelSampleSpace = Label(GUI, text="Digite o tamanho amostral")
labelSampleSpace.place(x=50, y = 80)

entrySampleSpace = Entry(GUI)
entrySampleSpace.place(x=60, y=120)

buttonCalc = Button(GUI, width = "25", command=bt_onClick, text="Calcular").place(x=30, y=155)


labelTest = Label(GUI, text="Média gerada pelo Python")
labelTest.place(x=50, y = 200)
entryMeanFirst = Entry(GUI, text="")
entryMeanFirst.place(x=60, y=220)

labelTest = Label(GUI, text="Média gerada pelo MTI")
labelTest.place(x=50, y = 240)
entryMeanSecond = Entry(GUI, text="")
entryMeanSecond.place(x=60, y=260)

labelTest = Label(GUI, text="Variancia gerada pelo Python")
labelTest.place(x=50, y = 290)
entryVarianceFirst = Entry(GUI, text="")
entryVarianceFirst.place(x=60, y=310)

labelTest = Label(GUI, text="Vaciancia gerada pelo MTI")
labelTest.place(x=50, y = 330)
entryVarianceSecond = Entry(GUI, text="")
entryVarianceSecond.place(x=60, y=350)

labelTest = Label(GUI, text="Feito por: Daniel Bandeira").place(x = 315, y = 150)
labelTest = Label(GUI, text="Versão 2.0").place(x=350, y = 170)

labelLambda = Label(GUI, text="Função escada em poisson")
labelLambda.place(x=300, y=20)

entryArchivePoisson = Entry(GUI)
entryArchivePoisson.place(x=310, y=50)

buttonArchivePoisson = Button(GUI, text = "Calcular e demonstrar função escada", command=bt_ladder)
buttonArchivePoisson.place(x=275, y=80)

"Largura, Altura, Esquerda, topo"
GUI.geometry("500x400+280+200")

GUI.title("Simulation Project with Exponencial")
GUI.mainloop()
