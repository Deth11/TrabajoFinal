import Adafruit_DHT


class Temperatura:

    def __init__(self, pin=17, sensor=Adafruit_DHT.DHT11):
        self._sensor = sensor
        self._data_pin = pin

    def datos_sensor(self):
        """ Devuelve un diccionario con la temperatura y humedad """
        humedad, temperatura = Adafruit_DHT.read_retry(self._sensor, self._data_pin)
        return {'temperatura': temperatura, 'humedad': humedad}


if __name__ == "__main__":
    import time

    temp = Temperatura()
    while True:
        datos = temp.datos_sensor()
        # Imprime en la consola las variables temperatura y humedad con un decimal
        print('Temperatura = {0:0.1f}°C  Humedad = {1:0.1f}%'.format(datos['temperatura'], datos['humedad']))
        time.sleep(0.5)