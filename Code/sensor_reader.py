import serial
import time

class SensorReader:
    def __init__(self):
        self.serial_port = '/dev/ttyUSB0'  # Puerto serie predeterminado
        self.baud_rate = 9600  # Velocidad de transmisión predeterminada
        self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)

    def read_sensor_data(self):
        try:
            self.ser.write(b'r')  # Envía un carácter 'r' al Arduino para solicitar la lectura del sensor
            time.sleep(0.1)  # Espera un breve momento para que el Arduino responda
            distance_str = self.ser.readline().decode().rstrip()  # Lee la respuesta del Arduino y elimina caracteres no deseados
            distance = int(distance_str)
            return distance
        except Exception as e:
            print("Error al leer datos del sensor:", e)
            return None
