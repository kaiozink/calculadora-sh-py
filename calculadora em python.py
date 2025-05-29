#importando tkinder
from tkinter import* 
from tkinter import ttk
#cria interfaces de GUI (biblioteca padrão do python)

#cores

cor1="#6e716f"
cor2="#cbd1ce"
cor3="#34334f"
cor4="#dcff18"


janela=Tk()#cria a janela
janela.title ("Calculadora")#nomeia a janela 
janela.geometry("235x235")#altera a largura e comprimento da janela

janela.config(background=cor2)#altera as cores da janela

#criando telas
visor = Frame(janela,width=235 ,height=40,background=cor3)#cria uma coluna para mostrar o resultado
visor.grid(row=0,column=0,)

#string
valor_texto = StringVar()
valor_texto.set("")

#adionando valor

def adicionar_valor(valor):
    valor_atual =valor_texto.get()
    valor_texto.set(valor_atual+str(valor))
    

#limpar visor 
def limpar():
    valor_texto.set("")

#calcular
def calcular():
    try:
        expressao = valor_texto.get()           # Corrigido: uso de get()
        resultado = eval(expressao)             # Usa eval para calcular a expressão
        valor_texto.set(str(resultado))         # Mostra o resultado no visor
    except:
        valor_texto.set("ERROR")                # Em caso de erro, mostra "ERROR"

    




#visor
app_label=Label(visor,textvariable=valor_texto,width=25,height=3,padx=5,relief=FLAT,bg=cor3,foreground=cor2,anchor='e',justify=RIGHT)
app_label.place(x=0,y=0)





#corpo botoes

Frame_corpo = Frame(janela,width=235 ,height=295,)#cria uma coluna para mostrar o resultado
Frame_corpo.grid(row=1,column=0,)

#botões
b_apagar= Button (Frame_corpo, text="C",width=15,height=2,bg=cor1,relief=RAISED ,overrelief=RIDGE,
                  command=limpar) 
b_apagar.place(x=0,y=0)

b_multiplicar= Button (Frame_corpo, text="*",width=7,height=2,bg=cor1,relief=RAISED ,overrelief=RIDGE,
             command=lambda:adicionar_valor("*")) 
b_multiplicar.place(x=118,y=0)

b_divisao = Button (Frame_corpo, text="/",width=6,height=2,background=cor4,foreground=cor1,
                    command=lambda:adicionar_valor("/")) 
b_divisao.place(x=177,y=0)

b_adição= Button (Frame_corpo, text="+",width=6,height=2,background=cor4,foreground=cor1,
                  command=lambda:adicionar_valor("+") ) 
b_adição.place(x=177,y=45)

b_subtra= Button (Frame_corpo, text="-",width=6,height=2,background=cor4,foreground=cor1,
                  command=lambda:adicionar_valor("-") ) 
b_subtra.place(x=177,y=90)

b_igual= Button (Frame_corpo, text="=",width=6,height=2,background=cor4,foreground=cor1,
                 command=calcular) 
b_igual.place(x=177,y=135)


#numeraçoes

b_1= Button (Frame_corpo, text="1",width=6,height=2,background=cor4,foreground=cor1,
             command=lambda:adicionar_valor(1) ) 
b_1.place(x=10,y=135)


b_2= Button (Frame_corpo, text="2",width=6,height=2,background=cor4,foreground=cor1,
              command=lambda:adicionar_valor(2)) 
b_2.place(x=65,y=135)

b_3= Button (Frame_corpo, text="3",width=6,height=2,background=cor4,foreground=cor1,
              command=lambda:adicionar_valor(3)) 
b_3.place(x=120,y=135)

b_4= Button (Frame_corpo, text="4",width=6,height=2,background=cor4,foreground=cor1,
              command=lambda:adicionar_valor(4)) 
b_4.place(x=10,y=90)

b_5= Button (Frame_corpo, text="5",width=6,height=2,background=cor4,foreground=cor1,
              command=lambda:adicionar_valor(5)) 
b_5.place(x=65,y=90)

b_6= Button (Frame_corpo, text="6",width=6,height=2,background=cor4,foreground=cor1,
              command=lambda:adicionar_valor(6)) 
b_6.place(x=120,y=90)

b_7= Button (Frame_corpo, text="7",width=6,height=2,background=cor4,foreground=cor1,
              command=lambda:adicionar_valor(7)) 
b_7.place(x=120,y=45)

b_8= Button (Frame_corpo, text="8",width=6,height=2,background=cor4,foreground=cor1,
              command=lambda:adicionar_valor(8)) 
b_8.place(x=65,y=45)

b_9= Button (Frame_corpo, text="9",width=6,height=2,background=cor4,foreground=cor1,
              command=lambda:adicionar_valor(9)) 
b_9.place(x=10,y=45)










janela.mainloop()#mantem um loop na janela 

