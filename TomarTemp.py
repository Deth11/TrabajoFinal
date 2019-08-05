import os
import json
import time
from Modulos_RaspberryPi.TempPI import Temperatura
import PySimpleGUI as sg

temperatura = Temperatura()


def layoutIngreso():
    return [[sg.Text('Registrar oficina?')], [sg.Radio(text='Si', group_id=00, enable_events=True),
                                              sg.Radio(text='No', group_id=00, enable_events=True)],
            [sg.Text('Indique la oficina: '), sg.InputText()], [sg.Button('Agregar')], [sg.Button('Finalizar')]]


def leer_temp(ofi):
    info_temperatura = temperatura.datos_sensor()
    info_temperatura.update({"nombre": ofi, "fecha": time.asctime(time.localtime(time.time()))})
    return info_temperatura


def guardar_temp(info):
    if os.path.exists(str(os.getcwd()) + "/dato-oficinas.json"):
        print('SI')
        with open("dato-oficinas.json", "r") as log_file:
            lista_de_temperaturas = json.load(log_file)
        lista_de_temperaturas.append(info)

        with open("dato-oficinas.json", "r+") as log_file:
            json.dump(lista_de_temperaturas, log_file, indent=4)
    else:
        print('NO')
        with open("dato-oficinas.json", "w") as log_file:
            json.dump([info], log_file, indent=4)


if __name__ == "__main__":
    while True:
        window = sg.Window('Prueba').Layout(layoutIngreso())
        event, values = window.Read()
        if event == 'Finalizar':
            break
        else:
            if values[1]:
                break
            else:
                if event == 'Agregar':
                    if values[2] is None:
                        window.Close()
                        sg.Popup('Ingrese un nombre de oficina')
                        break
                    else:
                        window.Close()
                        time.sleep(0)
                        temp = leer_temp(values[2])
                        guardar_temp(temp)
