import tkinter as tk

janela = tk.Tk()
janela.title('Calculadora de mudança de base')
janela.geometry('590x420')
janela.resizable(width=False,height=False)
janela.config(bg = '#483D8B')




text = tk.Text(janela,height=5,width=52)

l = tk.Label(janela,text = 'texto teste')
l.config(font = ('courrier',14))
fact = "um texto qualquer para testar"

text.insert(tk.INSERT,fact)

#camponumero = tk.Entry(janela,width=59)
#camponumero.place(x=40,y = 35)

#btc = tk.Button(janela,text='C',width=10,height=3)
#btc.place(x = 50,y = 80)

#btc = tk.Button(janela,text='Apagar',width=24,height=3)
#btc.place(x = 150,y = 80)

#btigual = tk.Button(janela,text='=',width=5,height=18)
#btigual.place(x = 350,y = 80)
'''bta = tk.Button(janela,text='A',width=10,height=3)
bta.place(x = 350,y = 150)

bta = tk.Button(janela,text='B',width=10,height=3)
bta.place(x = 450,y = 150)

bta = tk.Button(janela,text='C',width=10,height=3)
bta.place(x = 350,y = 220)

bta = tk.Button(janela,text='D',width=10,height=3)
bta.place(x = 450,y = 220)

bta = tk.Button(janela,text='E',width=10,height=3)
bta.place(x = 350,y = 290)

bta = tk.Button(janela,text='F',width=10,height=3)
bta.place(x = 450,y = 290)

bt1 = tk.Button(janela,text='1',width=10,height=3)
bt1.place(x = 50,y = 150)

bt2 = tk.Button(janela,text='2',width=10,height=3)
bt2.place(x = 150,y = 150)

bt3 = tk.Button(janela,text='3',width=10,height=3)
bt3.place(x = 250,y = 150)

bt4 = tk.Button(janela,text='4',width=10,height=3)
bt4.place(x = 50,y = 220)

bt5 = tk.Button(janela,text='5',width=10,height=3)
bt5.place(x = 150,y = 220)

bt6 = tk.Button(janela,text='6',width=10,height=3)
bt6.place(x = 250,y = 220)

bt7 = tk.Button(janela,text='7',width=10,height=3)
bt7.place(x = 50,y = 290)

bt8 = tk.Button(janela,text='8',width=10,height=3)
bt8.place(x = 150,y = 290)

bt9 = tk.Button(janela,text='9',width=10,height=3)
bt9.place(x = 250,y = 290)'''




janela.mainloop()