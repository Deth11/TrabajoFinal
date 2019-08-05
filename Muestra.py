import time
from Modulos_RaspberryPi.MatrizPI import Matriz
from Modulos_RaspberryPi.SonidoPI import Sonido
from Modulos_RaspberryPi.TempPI import Temperatura
import PySimpleGUI as sg

matriz = Matriz(numero_matrices=2, ancho=16)
sonido = Sonido()
temperatura = Temperatura()


def layout_muestra():
    return [[sg.Button('Mostrar'), sg.Button('Salir')]]


def acciones():
    print("Sonido Detectado!")
    temp_data = temperatura.datos_sensor()
    temp_formateada = 'Temperatura = {0:0.1f}°C  Humedad = {1:0.1f}%'.format(temp_data['temperatura'],
                                                                             temp_data['humedad'])
    matriz.mostrar_mensaje(temp_formateada, delay=0.08, font=2)


if __name__ == "__main__":
    while True:
        window = sg.Window('Prueba').Layout(layout_muestra())
        event, values = window.Read()
        if event == 'Mostrar':
            time.sleep(0.1)
            sonido.evento_detectado(acciones)
        else:
            break
