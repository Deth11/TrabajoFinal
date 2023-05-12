import PySimpleGUI as sg
from Modulos_Sopa import cross as g, funciones as p, matriz as M
import json


"""Este modulo tiene el programa principal en el cual 
   se van a invocar todas la funciones e importar modulos

    El programa principal esta dividio en partes : 

    Inicio programa principal
    Variables del menu de configuracion
    Ingresa las palabras
    Creacion de la matriz horizontal/vertical


"""
# Inicio programa principal
sg.ChangeLookAndFeel('TanBlue')
# Creacion menu de configuracion
colores = {'Rojo': 'red', 
           'Azul': 'blue', 
           'Amarillo': 'yellow', 
           'Violeta': 'purple',
           'Naranja': 'orange', 
           'Verde': 'green'}
window = sg.Window('Sopa de Letras', 
                   default_element_size=(40, 1), 
                   grab_anywhere=False).Layout(p.layout_config(colores))
# Variables del menu de configuracion
while True:
    button, values = window.Read()
    if button is None or button == 'Salir':
        break
    colores = {'Rojo': 'red', 
               'Azul': 'blue', 
               'Amarillo': 'yellow', 
               'Violeta': 'purple',
               'Naranja': 'orange', 
               'Verde': 'green'}
    definiciones = values[0]
    cantPalIngresadas = values[1]
    orientacion = values[2]
    caps = values[4]
    ColSus = colores[values[7]]
    ColVer = colores[values[8]]
    ColAdj = colores[values[9]]
    oficina = values['_DIR_']
    fuente = values[6]
    if button == 'Prev.':
        wndw = sg.Window('Muestra Tipografia', 
                         disable_close=True).Layout(p.layout_font(fuente))
        wndw.Read()
        wndw.Close()
    if not fuente:
        fuente = ['Helvetica']
    if oficina != '':
        e = window.FindElement('_DIR_')
        with open(oficina, "r") as log_file:
            lista_de_temperaturas = json.load(log_file)
            aux = []
            for x in lista_de_temperaturas:
                aux.append(x['nombre'])
        w = sg.Window('Oficinas').Layout(p.layout_oficinas(aux))
        event, values = w.Read()
        for x in lista_de_temperaturas:
            if values[0] == x['nombre']:
                w.Close()
                break
        """if int(x['temperatura']) >= 20:
           sg.ChangeLookAndFeel('Reds')  
           # Cambia la estetica de la matriz a una mas veraniega
        else:
            sg.ChangeLookAndFeel('BluePurple')  
            # Cambia la estetica de la matriz a una mas invernal"""
        
        (sg.ChangeLookAndFeel('Reds')
        ) if int(x['temperatura']) >= 20 else (
                            sg.ChangeLookAndFeel('BluePurple')) 
        # Cambia la estetica de la matriz a una 
        # mas veraniega o invernal segun la condicion
        
        e.Update('')
    if button == 'Continuar':
        window.Close()
        break
# Ingresa las palabras
if button != 'Salir' and button is not None:
    window.Close()
    ok = True
    while ok:
        if ColVer == ColSus or ColVer not in colores.values():
            if ColVer == ColSus:
                sg.Popup('Se eligieron 2 colores iguales, elije de nuevo', 
                         title='')
            wn = sg.Window('Eegir colores').Layout(
                    p.layout_elegir_color(colores)
                    )
            event, values = wn.Read()
            ColAdj = colores[values[2]]
            ColSus = colores[values[0]]
            ColVer = colores[values[1]]
            wn.Close()
        elif ColVer == ColAdj or ColAdj not in colores.values():
            if ColVer == ColAdj:
                sg.Popup('Se eligieron 2 colores iguales, elije de nuevo', 
                         title='')
            wn = sg.Window('Eegir colores').Layout(
                    p.layout_elegir_color(colores)
                    )
            event, values = wn.Read()
            ColAdj = colores[values[2]]
            ColSus = colores[values[0]]
            ColVer = colores[values[1]]
            wn.Close()
        elif ColSus == ColAdj or ColSus not in colores.values():
            if ColSus == ColAdj:
                sg.Popup('Se eligieron 2 colores iguales, elije de nuevo', 
                         title='')
            wn = sg.Window('Elegir colores').Layout(
                p.layout_elegir_color(colores)
                )
            event, values = wn.Read()
            ColAdj = colores[values[2]]
            ColSus = colores[values[0]]
            ColVer = colores[values[1]]
            wn.Close()
        else:
            ok = False
    window = sg.Window('Sopa de Letras', 
                       p.layout_ingreso(), 
                       grab_anywhere=False, 
                       disable_close=True)
    button, values = window.Read()
    dicc = {'Sustantivo': [], 'Adjetivo': [], 'Verbo': []}
    while button != 'Listo':
        if button is None:
            window.Close()
            break
        elif button == 'Agregar':
            p.ingreso_palabra(dicc, caps, values[0])
            window.Close()
            window = sg.Window('Sopa de Letras', 
                               p.layout_ingreso(), 
                               grab_anywhere=False)
            button, values = window.Read()
# Creacion de la matriz horizontal/vertical
if button == 'Listo' or button == 'Jugar':
    window.Close()
    ok = True
    while ok:
        window = sg.Window('Sopa de Letras').Layout(
            p.layout_elegir(dicc)
            )
        event, values = window.Read()
        if int(values[0]) > 0 or int(values[1]) > 0 or int(values[2]) > 0:
            ok = False
        else:
            sg.Popup('Aumente al menos un tipo de palabra', 
                     title='Incorrecto')
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
    mx = M.matriz(dicc, matr, caps, cantS, cantV, cantA)
    try:
        try:
            g.hacer_grafico_horizontal
            ( matr, 
              mx, 
              caps, 
              dicc, 
              cantS, 
              cantV, 
              cantA,
              ColSus, 
              ColVer, 
              ColAdj, 
              definiciones, 
              cantPalIngresadas, 
              fuente) if orientacion else g.hacer_grafico_vertical(
                                                        matr,
                                                        mx, 
                                                        caps, 
                                                        dicc, 
                                                        cantS, 
                                                        cantV, 
                                                        cantA,
                                                        ColSus, 
                                                        ColVer, 
                                                        ColAdj, 
                                                        definiciones, 
                                                        cantPalIngresadas, 
                                                        fuente )
        except ValueError:
            sg.Popup('No se ingreso ninguna palabra')
        except tk._tkinter.TclError:
            pass
    except NameError:
        pass
else:
    window.Close()
