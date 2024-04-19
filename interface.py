import PySimpleGUI as psg
from conversor import solicita_usuario


class Calculator:
    def __init__(self) -> None:
        dic = {'Hex': 16, 'Bin': 2, 'Dec': 10}

        interface = [
            [psg.Input(key='INPUT')],
            [
                psg.Text('Base de entrada: '),
                psg.OptionMenu(['Hex', 'Bin', 'Dex'], default_value='Dec', key='ENTRADA')
            ],
            [
                psg.Text('Base de saida: '),
                psg.OptionMenu(['Hex', 'Bin', 'Dex'], default_value='Dec', key='SAIDA')
            ],
            [psg.Button('Converter')]
        ]

        self.janela = psg.Window(title="Conversor de bases numéricas", layout=interface)

        while True:
            self.event, self.values = self.janela.read()

            if self.event == psg.WIN_CLOSED or self.event == 'Cancel':
                break

            elif self.event == 'Converter':
                print(solicita_usuario(self.values['INPUT'], dic[self.values['ENTRADA']], dic[self.values['SAIDA']]))

        self.janela.close()
