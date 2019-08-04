import os
import json
import time
from TempPI import Temperatura
import PySimpleGUI as sg

temperatura = Temperatura()


def layoutIngreso():
    return [[sg.Text('Registrar oficina?')], [sg.Radio(text='Si', group_id=00), sg.Radio(text='No', group_id=00)],
            [sg.Text('Indique la oficina: '), sg.InputText()], [sg.Button('Agregar')], [sg.Button('Finalizar')]]


def leer_temp():
    info_temperatura = temperatura.datos_sensor()
    info_temperatura.update({"fecha": time.asctime(time.localtime(time.time()))})
    return info_temperatura


def guardar_temp(info):
    with open(os.path.join("archivos_texto", "dato-oficinas.json"), "r") as log_file:
        try:
            lista_de_temperaturas = json.load(log_file)
        except Exception:
            # En caso de que el json no sea una lista
            lista_de_temperaturas = []
    lista_de_temperaturas.append(info)
    with open(os.path.join("archivos_texto", "dato-oficinas.json"), "w") as log_file:
        json.dump(lista_de_temperaturas, log_file, indent=4)


if __name__ == "__main__":
    while True:
        window = sg.Window('Prueba').Layout(layoutIngreso())
        event, values = window.Read()
        if event == 'Finalizar':
            break
        else:
            if values[0]:
                if event == 'Agregar':
                    if values[2] is None:
                        window.Close()
                        sg.Popup('Ingrese un nombre de oficina')
                        break
                    else:
                        window.Close()
                        time.sleep(100)
                        temp = leer_temp()
                        guardar_temp(temp)
            else:
                break
