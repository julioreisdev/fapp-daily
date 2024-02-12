import PySimpleGUI as sg
from datetime import datetime, timedelta
import os

now = (datetime.now() - timedelta(days=0)).strftime('%d-%m-%Y')

form = [ 
    [sg.Text('Como está se sentindo?', font=('Helvetica', 18))], 
    [sg.Multiline(default_text='', size=(80, 10), font=('Helvetica', 14), key='-INPUT-')], 
    [sg.Button('Registrar', size=(10, 2), font=('Helvetica', 14))]
]

window = sg.Window('FAPP DAILY', form, size=(600, 300), element_justification='c', finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Registrar':
        input_text = values['-INPUT-'].strip()
        if input_text:
            path = f'./diaries/{now}.txt'
            if not os.path.exists(path):
                with open(path, 'w') as file:
                    file.write(f'{input_text}')
            else:
                with open(path, 'r+') as file:
                    file_lines = file.readlines()
                    if len(file_lines) != 0:
                        file.write(f'\n{input_text}')
                    else:
                        file.write(f'{input_text}')
            sg.popup('Registro efetuado com sucesso!', title='Sucesso')
            window.close()
        else:
            sg.popup('Por favor, preencha o campo de entrada!', title='Erro')

window.close()
