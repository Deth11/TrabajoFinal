import PySimpleGUI as sg
from tkinter.font import Font
import tkinter as tk
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


def layoutConfig(colores):
    """Funcion que devuelve una lista la cual es utilizada para crear el layout del menu de configuracion"""
    return [
        [sg.Text('Configuracion del juego', size=(30, 1), justification='center', font=("Helvetica", 25),
                 text_color='Red')],
        [sg.Frame(layout=[
            [sg.T('Seleccione las ayudas que quiere que aparezcan en la sopa')],
            [sg.Checkbox('Definiciones de las palabras'), sg.Checkbox('Mostrar palabras ingresadas')]],
            title='Tipos de Ayuda', title_color='red', tooltip='Elija las ayudas a mostrar')],
        [sg.Frame(layout=[
            [sg.Radio('Horizontal', "RADIO1", default=True), sg.Radio('Vertical', 'RADIO1')]], title='Orientacion',
            title_color='red', tooltip='Elija la orientacion de las palabras')],
        [sg.Frame(layout=[
            [sg.T('Seleccione como desea que sea el estilo de las letras.'
                  '\nPuede previsualizar la tipografia escogiendo una de la lista y clickeando el boton Prev.')],
            [sg.Radio('Mayusculas', "RADIO2", default=True), sg.Radio('Minusculas', 'RADIO2'),
             sg.Listbox(tk.font.families(root=(tk.Tk())), size=(30, 10)), sg.Button('Prev.')]],
            title='Tipografia', title_color='red', tooltip='Seleccione el tipo de letra que quiere usar')],
        [sg.Frame(layout=[
            [sg.T('Seleccione que color quiere que sea el boton de cada tipo de palabra')],
            [sg.Text('Sustantivo'), sg.Spin(values=list(colores.keys()), initial_value='Rojo')],
            [sg.Text('Verbo'), sg.Spin(list(colores.keys()), initial_value='Verde', )],
            [sg.Text('Adjetivo'), sg.Spin(list(colores.keys()), initial_value='Amarillo')]],
            title='Color de botones', title_color='red', tooltip='Elija los colores para cada boton')],
        [sg.Frame(layout=[
            [sg.T('Ingrese el documento donde se encuentran las distintas oficinas y seleccione una de ellas.'
                  '\n(En el caso de no haber, no ingrese nada)')],
            [sg.Text('Archivo de oficinas:'), sg.Input(enable_events=True, key='_DIR_'), sg.FileBrowse()]],
            title='Oficinas', title_color='red',
            tooltip='Elija el archivo de oficinas, en caso de no haber deje el espacio en blanco')],
        [sg.Button('Continuar'), sg.Button('Salir')]
    ]


def layoutIngreso():
    """Funcion que devuelve una lista la cual es utilizada para el ingreso de las palabras"""
    return [[sg.Text('Ingrese las palabras a mostrar en la sopa, deben ser verbos/sustantivos/adjetivos (recuerde '
                     'respetar los acentos)')],
            [sg.T('Una vez escrita la palabra debera clickear el boton "Agregar".\nCuando quiera finalizar la carga haga click en "Listo"')],
            [sg.InputText()],
            [sg.OK(button_text='Agregar'), sg.Button('Listo')]]


def layoutElegir(dicc):
    return[
        [sg.T('Haga click en las flechas para indicar la cantidad de palabras de cada tipo a utilizar')],
        [sg.Text('Verbos'), sg.Spin(list(range(len(dicc['Verbo'])+1), ), auto_size_text=True, initial_value=0)],
        [sg.Text('Adjetivos'), sg.Spin(list(range(len(dicc['Adjetivo'])+1), ), auto_size_text=True, initial_value=0)],
        [sg.Text('Sustantivos'), sg.Spin(list(range(len(dicc['Sustantivo'])+1), ),
        auto_size_text=True, initial_value=0)], [sg.OK(button_text='Listo')]]


def layoutFont(fuente):
    return [[sg.Text('Tipografia: ' + str(fuente), font=fuente)], [sg.OK()]]

def layourElegirColor(colores):
    return [[sg.Text('Sustantivo'), sg.Spin(values=list(colores.keys()), initial_value='Rojo')],
            [sg.Text('Verbo'), sg.Spin(list(colores.keys()), initial_value='Verde', )],
            [sg.Text('Adjetivo'), sg.Spin(list(colores.keys()), initial_value='Amarillo')], [sg.OK()]]


def layoutOficinas(ofi):
    return [[sg.T('Seleccione la oficina correspondiente')], [sg.Spin(ofi, initial_value=ofi[len(ofi) - 1])], [sg.OK()]]
