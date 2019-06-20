import Funciones as p
import PySimpleGUI as sg
import Matriz as M
import Grafico as g
# Inicio programa principal
sg.ChangeLookAndFeel('TanBlue')
# Creacion menu de configuracion
window = sg.Window('Sopa de Letras', p.layoutConfig(), default_element_size=(40, 1), grab_anywhere=False)
button, values = window.Read()
# Variables del menu de configuracion

definiciones = values[0]
cantTipoPal = values[1]
cantPalIngresadas = values[2]
orientacion = values[3]
caps = values[5]
oficina = values[8]
fuente = values[7]
if not fuente:
    fuente = ['Helvetica']  # No logramos aplicar la fuente en las palabras
if oficina:
    sg.ChangeLookAndFeel('SandyBeach')  # Cambia la estetica de la matriz a una mas veraniega
else:
    sg.ChangeLookAndFeel('BluePurple')  # Cambia la estetica de la matriz a una mas invernal
if button is None or button == 'Salir':
    window.Close()
# Ingresa las palabras
else:
    window = sg.Window('Sopa de Letras', p.layoutIngreso(), grab_anywhere=False)
    button, values = window.Read()
    dicc = {'Sustantivo': [], 'Adjetivo': [], 'Verbo': []}
    while button != 'Listo':
        if button is None:
            window.Close()
            break
        elif button == 'Agregar':
            p.ingresoPalabra(dicc, fuente, caps, values[0])
            window.Close()
            window = sg.Window('Sopa de Letras', p.layoutIngreso(), grab_anywhere=False)
            button, values = window.Read()
    # Creacion de la matriz horizontal/vertical
    if button == 'Listo':
        window.Close()
        window = sg.Window('Sopa de Letras').Layout(p.layoutElegir(dicc))
        event, values = window.Read()
        window.Close()
        print(dicc['Verbo'])
        print(dicc['Sustantivo'])
        print(dicc['Adjetivo'])
        matr = []
        if orientacion:
            M.matriz_horizontal(dicc, matr, caps)
        else:
            M.matriz_vertical(dicc, matr)
        # Matriz graficada
        g.hacer_grafico(matr, dicc, definiciones, cantPalIngresadas, cantTipoPal)
