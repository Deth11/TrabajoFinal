import PySimpleGUI as sg
import tkinter as tk
from tkinter.font import Font
from pattern.web import Wiktionary


def ingresoPalabra(dicc, caps, pal):
    """Ingresa una palabra y la asigna a un diccionario dependiendo el tipo de palabra.
    Ademas de agregar la palabra agrega su definicion.
    El tipo de palabra lo busca en Wiktionary al igual que su definicion.
    En caso de que la palabra no se encuentre sera agregado al archivo 'errores'."""
    try:
        article = Wiktionary(language='es').search(pal.lower())
        listaTipo = []
        titulos = ['Adjetivo', 'Forma adjetiva', 'Verbo', 'Verbo transitivo', 'Forma verbal', 'Sustantivo femenino',
                   'Sustantivo masculino']
        indiceFull = False
        for i in range(len(article.sections)):
            listaTipo.append(article.sections[i].title)
            if article.sections[i].title in titulos and indiceFull == False:
                indice = i
                indiceFull = True
        titleText = article.sections[indice].content.find('1')
        line = article.sections[indice].content[titleText + 1:]
        indexTo = line.partition('\n')[0].find('[')
        definition = line[:indexTo]
        if caps:
            pal.upper()
        if 'Adjetivo' in listaTipo or 'Forma adjetiva' in listaTipo:
            dicc['Adjetivo'].append((pal, definition))
        elif 'Verbo transitivo' in listaTipo or 'Forma verbal' in listaTipo or 'Verbo' in listaTipo:
            dicc['Verbo'].append((pal, definition))
        elif 'Sustantivo masculino' in listaTipo or 'Sustantivo femenino' in listaTipo:
            dicc['Sustantivo'].append((pal, definition))
    except AttributeError or TypeError:
        sg.Popup('La palabra no se encuentra en Wiktionary, sera informado al desarollador.',
                 title='Palabra no encotrada')
        errores = open('Errores.txt', 'a+')
        errores.write(pal + '\n')
        errores.close()
    except:
        sg.Popup('Lamentamos informar que el error es desconocido.', title='Error desconocido')


def layoutConfig():
    """Funcion que devuelve una lista la cual es utilizada para crear el layout del menu de configuracion"""
    colores = ['Rojo', 'Azul', 'Violeta', 'Negro', 'Verde', 'Amarillo']
    return [
        [sg.Text('Configuracion del juego', size=(30, 1), justification='center', font=("Helvetica", 25),
                 text_color='Red')],
        [sg.Frame(layout=[
            [sg.Checkbox('Definiciones'), sg.Checkbox('Cantidad de palabras ingresadas')]],
            title='Tipos de Ayuda', title_color='red')],
        [sg.Frame(layout=[
            [sg.Radio('Horizontal', "RADIO1", default=True), sg.Radio('Vertical', 'RADIO1')]], title='Orientacion',
            title_color='red', )],
        [sg.Frame(layout=[
            [sg.Radio('Mayusculas', "RADIO2", default=True), sg.Radio('Minusculas', 'RADIO2'),
             sg.Listbox(list(tk.font.families(root=tk.Tk())), size=(30, 10)), sg.Button('Prev.')]], title='Tipografia', title_color='red')],
        [sg.Frame(layout=[
           [sg.Text('Sustantivo'), sg.Spin(values=colores, initial_value='Rojo', disabled=True, )],
            [sg.Text('Verbo'), sg.Spin(colores, initial_value='Verde', )],
            [sg.Text('Adjetivo'), sg.Spin(colores, initial_value='Amarillo', disabled=True)]], title='Color de botones', title_color='red')],
        [sg.Frame(layout=[
            [sg.Radio('Oficina verano', "RADIO3", default=True), sg.Radio('Oficina invierno', 'RADIO3')]],
            title='Oficinas',
            title_color='red')],
        [sg.Button('Jugar'), sg.Button('Salir')]
    ]


def layoutIngreso():
    """Funcion que devuelve una lista la cual es utilizada para el ingreso de las palabras"""
    return [[sg.Text('Primero ingrese las palabras a buscar, deben ser verbos/sustantivos/adjetivos (recuerde '
                     'respetar los acentos)')], [sg.InputText()],
            [sg.OK(button_text='Agregar'), sg.Button('Listo')]]


def layoutElegir(dicc):
    return[[sg.Text('Verbos'), sg.Spin(list(range(len(dicc['Verbo'])+1), ), auto_size_text=True, initial_value=0)],
           [sg.Text('Adjetivos'), sg.Spin(list(range(len(dicc['Adjetivo'])+1), ), auto_size_text=True, initial_value=0)],
           [sg.Text('Sustantivos'), sg.Spin(list(range(len(dicc['Sustantivo'])+1), ),
            auto_size_text=True, initial_value=0)], [sg.OK(button_text='Listo')]]


def layoutFont(fuente):
    return [[sg.Text('Tipografia: ' + str(fuente), font=fuente)], [sg.OK()]]
