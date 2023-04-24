import os
import json
import PySimpleGUI as sg

DIR = os.path.dirname(os.path.realpath("."))
PATH_JSON_FILE = f"{DIR}\\UNLPImage\\db\\users.json"
file = open(PATH_JSON_FILE, 'w')

navbar_l = [
    [sg.Text('Nuevo perfil')],
]

navbar_r = [
    [sg.Button('< Volver')],
]

navbar = [
    [sg.Column(navbar_l), 
    sg.Push(), 
    sg.Column(navbar_r)]
]

col1 = [
    [sg.Text('Nick o alias')],
    [sg.Input()],
    [sg.Text('Nombre')],
    [sg.Input()],
    [sg.Text('Edad')],
    [sg.Input()],
    [sg.Text('Genero autopercibido')],
    [sg.InputCombo(values=[
        'Masculino', 
        'Femenino',
        'No binario'
        ],
        default_value='Seleccione una opción')],
    [sg.Checkbox('')],
    [sg.Input()],
]

col2 = [
    [sg.Image(filename='images/new_profile.png', size=(300, 300))],
    [sg.Push(), sg.Button('Seleccionar avatar'), sg.Push()]
]

footer = [
    [sg.Push(),
    sg.Button('Guardar')],
]

layout = [
    [navbar], 
    [sg.Column(col1), sg.Push(), sg.Column(col2), sg.Push()],
    [footer]
]

window = sg.Window(
    'UNLPImage',
    size=(900, 700),
    layout=layout,
)

window.read()
evento, valores = window.read()
print('evento:', evento)

while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    
    if event == "Guardar":
        new_user = {}
        new_user['nick'] = values[0]
        new_user['name'] = values[1]
        new_user['age'] = values[2]
        new_user['gender'] = values[3]
        new_user['other'] = values[5]
        # new_user['avatar'] = values[5]
        user = json.dumps(new_user)
        file.write(user)

        print("Guardado")

file.close()
window.close()
