import Funciones as p
import PySimpleGUI as sg
import Matriz as M
import Cross as g
# Inicio programa principal
sg.ChangeLookAndFeel('TanBlue')
# Creacion menu de configuracion
window = sg.Window('Sopa de Letras', p.layoutConfig(), default_element_size=(40, 1), grab_anywhere=False)
# Variables del menu de configuracion
while True:
    button, values = window.Read()
    if button is None or button == 'Salir':
        break
    colores = {'Rojo': 'red', 'Azul': 'blue', 'Amarillo': 'yellow', 'Violeta': 'purple',
           'Naranja': 'orange', 'Negro': 'black', 'Verde': 'green'}
    definiciones = values[0]
    cantPalIngresadas = values[1]
    orientacion = values[2]
    caps = values[4]
    ColSus = colores[values[7]]
    ColVer = colores[values[8]]
    print(values)
    ColAdj = colores[values[9]]
    oficina = values[10]
    fuente = values[6]
    if button == 'Prev.':
        wndw = sg.Window('Muestra Tipografia', disable_close=True).Layout(p.layoutFont(fuente))
        wndw.Read()
        wndw.Close()
    if not fuente:
        fuente = ['Helvetica']
    if oficina:
        sg.ChangeLookAndFeel('SandyBeach')  # Cambia la estetica de la matriz a una mas veraniega
    else:
        sg.ChangeLookAndFeel('BluePurple')  # Cambia la estetica de la matriz a una mas invernal
    if button == 'Jugar':
        window.Close()
        break
# Ingresa las palabras
if button != 'Salir' and button is not None:
    window.Close()
    window = sg.Window('Sopa de Letras', p.layoutIngreso(), grab_anywhere=False, disable_close=True)
    button, values = window.Read()
    dicc = {'Sustantivo': [], 'Adjetivo': [], 'Verbo': []}
    while button != 'Listo':
        if button is None:
            window.Close()
            break
        elif button == 'Agregar':
            p.ingresoPalabra(dicc, caps, values[0])
            window.Close()
            window = sg.Window('Sopa de Letras', p.layoutIngreso(), grab_anywhere=False)
            button, values = window.Read()
# Creacion de la matriz horizontal/vertical
if button == 'Listo' or button == 'Jugar':
    window.Close()
    window = sg.Window('Sopa de Letras').Layout(p.layoutElegir(dicc))
    event, values = window.Read()
    window.Close()
    cantV = int(values[0])
    cantS = int(values[2])
    cantA = int(values[1])
    if cantV > len(dicc['Verbo']):
        cantV = len(dicc['Verbo'])
    if cantA > len(dicc['Adjetivo']):
        cantA = len(dicc['Adjetivo'])
    if cantS > len(dicc['Sustantivo']):
        cantS = len(dicc['Sustantivo'])
    matr = []
    mx = M.matriz(dicc, matr, caps, int(values[2]), int(values[0]), int(values[1]))
    try:
        if orientacion:
            g.hacer_grafico_horizontal(matr, mx, caps, dicc, cantS, cantV, cantA,
                                       ColSus, ColVer, ColAdj, definiciones, cantPalIngresadas, fuente)
        else:
            g.hacer_grafico_vertical(matr, mx, caps, dicc, int(values[2]), int(values[0]), int(values[1]), ColSus, ColVer, ColAdj)
    except ValueError:
        sg.Popup('No se ingreso ninguna palabra')
else:
    window.Close()