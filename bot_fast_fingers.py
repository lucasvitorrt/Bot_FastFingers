import PySimpleGUI as sg
import functions as f

layout = [
    [sg.T('Quantidade de PPM (Média):'), sg.InputText(size=(4, 1), key='Entrada')],
    [sg.T('Tempo entre Palavras:'), sg.T(' ' * 6), sg.InputText(size=(4, 1), key='Tempo')],
    [sg.Button('Iniciar'), sg.T(' ' * 23), sg.Button('Parar')]
]

window = sg.Window('FastFingers', layout, size=(241, 92), keep_on_top=True)


def begin(window):
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Iniciar':
            ppm = values['Entrada']
            tempo = values['Tempo']
            f.digita(ppm, tempo)
        if event == 'Parar':
            f.close()
            break
    window.close()


begin(window)

