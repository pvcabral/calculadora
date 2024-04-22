from tkinter import Tk, Label, Button, OptionMenu, StringVar
from conversor import solicita_usuario


WIDTH = 325
HEIGHT = 260
X = [0, 65, 130, 195, 260, 160]
Y0 = 55
Y = [Y0, Y0 + 40, Y0 + 80, Y0 + 120, Y0 + 160]
DIC = {'Bin': 2, 'Dec': 10, 'Hex': 16}
BUTTONS = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def insert(text):
    input.config(text=input.cget('text') + text)


def apagar(index):
    input.config(text=input.cget('text')[index:-1])
    btn_apagar.config(
        text='<=',
        command=lambda: apagar(0)
    )


def converter():
    resultado = solicita_usuario(input.cget('text'), DIC[base_entrada.cget('text')], DIC[base_saida.cget('text')])
    input.config(text=resultado)
    btn_apagar.config(
        text='c',
        command=lambda: apagar(-1)
    )


janela = Tk()
janela.title('Calculadora de mudança de base')
janela.config(
    width=WIDTH,
    height=HEIGHT
)
janela.resizable(
    width=False,
    height=False
)
janela.config(
    bg='#6eabe4'
)

input = Label(
    janela,
    anchor='e',
    bg='#ffffff',
    text='',
    font=('Arial', 15),
    width=29,
    height=2
)
input.place(x=0, y=0)

base_entrada = OptionMenu(
    janela,
    StringVar(value='Base de entrada'),
    *['Bin', 'Dec', 'Hex'],
)
base_entrada.config(
    width=20
)
base_entrada.place(x=X[0], y=Y[4])

base_saida = OptionMenu(
    janela,
    StringVar(value='Base de saida'),
    *['Bin', 'Dec', 'Hex'],
)
base_saida.config(
    width=20
)
base_saida.place(x=X[5], y=Y[4])

btn1 = Button(
    janela,
    text=BUTTONS[1],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[1])
)
btn1.place(x=X[0], y=Y[0])

btn2 = Button(
    janela,
    text=BUTTONS[2],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[2])
)
btn2.place(x=X[1], y=Y[0])

btn3 = Button(
    janela,
    text=BUTTONS[3],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[3])
)
btn3.place(x=X[2], y=Y[0])

btn4 = Button(
    janela,
    text=BUTTONS[4],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[4])
)
btn4.place(x=X[0], y=Y[1])

btn5 = Button(
    janela,
    text=BUTTONS[5],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[5])
)
btn5.place(x=X[1], y=Y[1])

btn6 = Button(
    janela,
    text=BUTTONS[6],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[6])
)
btn6.place(x=X[2], y=Y[1])

btn7 = Button(
    janela,
    text=BUTTONS[7],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[7])
)
btn7.place(x=X[0], y=Y[2])

btn8 = Button(
    janela,
    text=BUTTONS[8],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[8])
)
btn8.place(x=X[1], y=Y[2])

btn9 = Button(
    janela,
    text=BUTTONS[9],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[9])
)
btn9.place(x=X[2], y=Y[2])

btn10 = Button(
    janela,
    text=BUTTONS[10],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[10])
)

btn10.place(x=X[3], y=Y[0])

btn11 = Button(
    janela,
    text=BUTTONS[11],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[11])
)
btn11.place(x=X[4], y=Y[0])

btn12 = Button(
    janela,
    text=BUTTONS[12],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[12])
)
btn12.place(x=X[3], y=Y[1])

btn13 = Button(
    janela,
    text=BUTTONS[13],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[13])
)
btn13.place(x=X[4], y=Y[1])

btn14 = Button(
    janela,
    text=BUTTONS[14],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[14])
)
btn14.place(x=X[3], y=Y[2])

btn15 = Button(
    janela,
    text=BUTTONS[15],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[15])
)
btn15.place(x=X[4], y=Y[2])

btn_apagar = Button(
    janela,
    text='<=',
    font=('Arial', 15),
    width=5,
    command=lambda: apagar(0)
)
btn_apagar.place(x=X[0], y=Y[3])

btn0 = Button(
    janela,
    text=BUTTONS[0],
    font=('Arial', 15),
    width=5,
    command=lambda: insert(BUTTONS[0])
)
btn0.place(x=X[1], y=Y[3])

btn_convert = Button(
    janela,
    text='Converter',
    font=('Arial', 15),
    width=19,
    command=converter
)
btn_convert.place(x=X[2], y=Y[3])

janela.mainloop()
