#uma calculadora muito simples, só faz as quatro operações basicas e só é capaz de fazer uma conta por vez
#vou tentar atualizar ela com frequencia, mas por enquanto é isso mesmo

#isso é um projeto simples pra treinar minhas habilidades em python

#aprecie com moderação


#importando recursos essenciais pra calcs 
# -*- coding: UTF-8 -*-
import tkinter.font as font
from tkinter import *
from tkinter import ttk



#declarando três variaveis globais: o valor da tela, o valor da equação e uma "chave" para a equaçaõ
valortelinha = ""
valordaequs = ""
equa = ""


def c():
    #aqui a gente puxa o valor da telinha e esvazia ele, fazemos o mesmo com a propriedade de texto da label 
    # (que seria a telinha)
    global valortelinha 
    valortelinha = ""
    lbl.config(text ="")

def igual():
    #aqui é mais complexo, vamos fazer com que o botão "=" realize a operação
    #a logica é simples: a gente pega o valor string da telinha e o valor que foi salvo clicando no botão
    #da operação correspondente e jogamos ele pra uma variavel (equaf) e depois usamos a função eval() para
    #que ele leia a equação que foi gerada e a trate como uma equação própria.
    #após isso o valor total vai ser impresso no label da tela e o valor da variavel telinha é apagado
    global valordaequs
    global valortelinha
    global equa
    match(valordaequs):
        case 1:
             equaf = equa+valortelinha
             total = str(eval(equaf))
             lbl.config(text = total)
             valortelinha = ""
        case 2:
             equaf = equa+valortelinha
             total = str(eval(equaf))
             lbl.config(text = total)
             valortelinha = ""
        case 3:
             equaf = equa+valortelinha
             total = str(eval(equaf))
             lbl.config(text = total)
             valortelinha = ""

        case 4:
             equaf = equa+valortelinha
             total = str(eval(equaf))
             lbl.config(text = total)
             valortelinha = ""



#as funções das operações são relativamente simples tambem, vamos lá
#primeiro eu defini uma "chave" pra cada operação, que vai ser chamada quando o botão "=" é clicado
#e joga esse valor dentro do case correspondente.

#depois disso a gente faz o seguinte: dentro da função equa a gente junta a string que tá na tela com a string
#que corresponde ao sinal da operação (é bem bobo mas é o que eu sei fazer) e depois disso apagamos a tela e o valor
#da variavel telinha para que o proximo input seja recebido
def mais():
    global valortelinha
    global valordaequs
    global equa
    valordaequs = 1
    equa = valortelinha+"+"
    lbl.config(text = "")
    valortelinha = ""
    
def menos():
    print("-")
    global valortelinha
    global valordaequs
    global equa
    valordaequs = 2
    equa = valortelinha+"-"
    lbl.config(text = "")
    valortelinha = ""
    
def dividir():
    global valortelinha
    global valordaequs
    global equa
    valordaequs = 3
    equa = valortelinha+"/"
    lbl.config(text = "")
    valortelinha = ""

def multiplicar():
    global valortelinha
    global valordaequs
    global equa
    valordaequs = 4
    equa = valortelinha+"*"
    lbl.config(text = "")
    valortelinha = ""


#função bem simples que pega o valor atribuido a cada botão quando ele é clicado 
#e adiciona esse valor na string da tela
def numero(num): 
    global valortelinha
    valortelinha = valortelinha+str(num)
    lbl.config(text = valortelinha)


#algumas definições pro tkinter, cor do botão, alturas e colunas (nomes bobos desculpa)
#e as definições da janela
corbtn = '#fcfcfc'
alts = [140,195,250,305,360]
cols = [5,82,160,240]
window = Tk()
window.title("Caculadora")
window.geometry('320x415')
window.configure(background = "#2a3942")



        


#definindo os botões na tela do app >///<
btn2 = Button(window ,text="C",command=c,bg=corbtn,relief= FLAT,bd = 5).place(x = cols[0], y =alts[0],width=230,height=50)
btn4 = Button(window ,text="/",command=dividir,bg=corbtn,relief= FLAT,bd = 5).place(x = cols[3], y =alts[0],width=75,height=50)

btn5 = Button(window ,text="7",command=lambda:numero(7),bg=corbtn,relief= FLAT,bd = 5).place(x = cols[0], y =alts[1],width=75,height=50)
btn6 = Button(window ,text="8",command=lambda:numero(8),bg=corbtn,relief= FLAT,bd = 5).place(x = cols[1], y =alts[1],width=75,height=50)
btn7 = Button(window ,text="9",command=lambda:numero(9),bg=corbtn,relief= FLAT,bd = 5).place(x = cols[2], y =alts[1],width=75,height=50)
btn8 = Button(window ,text="X",command=multiplicar,bg=corbtn,relief= FLAT,bd = 5).place(x = cols[3], y =alts[1],width=75,height=50)

btn9 = Button(window ,text="4",command=lambda:numero(4),bg=corbtn,relief= FLAT,bd = 5).place(x = cols[0], y =alts[2],width=75,height=50)
btn11 = Button(window ,text="6",command=lambda:numero(6),bg=corbtn,relief= FLAT,bd = 5).place(x = cols[2], y =alts[2],width=75,height=50)
btn10 = Button(window ,text="5",command=lambda:numero(5),bg=corbtn,relief= FLAT,bd = 5).place(x = cols[1], y =alts[2],width=75,height=50)
btn12 = Button(window ,text="-",command=menos,bg=corbtn,relief= FLAT,bd = 5).place(x = cols[3], y =alts[2],width=75,height=50)

btn13 = Button(window ,text="1",command=lambda:numero(1),bg=corbtn,relief= FLAT,bd = 5).place(x = cols[0], y =alts[3],width=75,height=50)
btn14 = Button(window ,text="2",command=lambda:numero(2),bg=corbtn,relief= FLAT,bd = 5).place(x = cols[1], y =alts[3],width=75,height=50)
btn15 = Button(window ,text="3",command=lambda:numero(3),bg=corbtn,relief= FLAT,bd = 5).place(x = cols[2], y =alts[3],width=75,height=50)
btn16 = Button(window ,text="+",command=mais,bg=corbtn,relief= FLAT,bd = 5).place(x = cols[3], y =alts[3],width=75,height=50)

btn14 = Button(window ,text="0",command=lambda:numero(0),bg=corbtn,relief= FLAT,bd = 5).place(x = cols[0], y =alts[4],width=75,height=50)
btn15 = Button(window ,text="=",command=igual,bg="#196aa7",fg="#FFFFFF",relief= FLAT,bd = 5).place(x = cols[1], y =alts[4],width=233,height=50)

#e por ultimo a definição da label que servira de telinha da calculadora
lbl = Label(window,text=valortelinha, bg = "#425a68", font=("Roboto", 25),anchor='e')
lbl.place(x = 0, y = 5,width=320,height=120)
 
















    
window.mainloop()
