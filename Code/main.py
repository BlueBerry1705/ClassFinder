import serial
from motor_controler import MotorController
import time

def BluetoothCommand(message, motor):
    def forward(motor):
        print("forward")
        motor.forward('ALL', 40)
    
    def backward(motor):
        print("backward")
        motor.backward('ALL', 10)
    
    def stop(motor):
        print("stop")
        motor.stop('ALL')
    
    def turn(motor):
        print("turn")
        motor.turn_left()

    def incVelocity(motor):
        print("IncVelocity")
        motor.set_velocity(motor.get_velocity() + 10)  
        motor.forward('ALL', motor.get_velocity())
    
    def decVelocity(motor):
        print("DecVelocity")
        motor.set_velocity(motor.get_velocity() - 10)
        motor.forward('ALL', motor.get_velocity())
        
    def clase1(motor):
        motor.forward('ALL', 50)
        time.sleep(5)
        motor.stop('ALL')
      
    def spin(motor):
        motor.stop('A')
        motor.forward('B', 20)
    
    switch = {
        "f": forward,
        "b": backward,
        "s": stop,
        "t": turn,
        "+": incVelocity,
        "-": decVelocity,
        "q": stop,
        "x": spin
    }
    
    switch.get(message, stop)(motor)

def FindClass(message, motor):
    clase = message[-2:]
    try:
        numero = int(clase)
        
        
        
        if numero == 3:
            motor.forward('ALL',50)
            time.sleep(12)
            return True
        
        if numero > 3 and (numero % 2) != 0:
            motor.forward('ALL',50)
            resultado = ((numero - 3) // 2) + 1
            time.sleep(22 * resultado + 12)
            return True
        else:
            print("No mapeado")
         
    except ValueError:
        print("Los dos últimos carácteres no son un número")
    
    return False


def get_sensors(motor, distances, giro):
    if distances[0] <= 40:
        motor.turn_angle(45, 'right', 30)
        giro += 1
    
    elif distances[1] <= 40:
        motor.turn_angle(90, 'right', 30)
        giro += 1
    
    elif distances[2] <= 40:
        motor.turn_angle(45, 'left', 30)
        giro += 1


if __name__ == '__main__':

    motor = MotorController()
    serBt = serial.Serial('/dev/rfcomm0', 9600)
    
    init = False
    
    giro = 0
    
    

    try:
        while True:
            if init:
                data = serSensor.readline().decode().rstrip()
                if data:
                    # Separar los datos en una lista
                    distances = data.split(' ')
                    # Convertir los datos a números enteros
                    distances = [int(distance) for distance in distances]
                    # Imprimir las distancias medidas
                    print("Distancias medidas:", distances)
                    get_sensors(motor, distances, giro)
                
            
            if serBt.in_waiting > 0:
                message = serBt.readline().decode('utf-8').rstrip()
                print("Mensaje recibido: ", message)
                if message == "k":
                    break
                
                if message == "q":
                    init = True
                    serSensor = serial.Serial('/dev/ttyUSB0', 9600)  # Ajusta el nombre del puerto serie según corresponda
                    serSensor.flushInput()
                else:
                    BluetoothCommand(message, motor)
                    if FindClass(message, motor):
                        time.sleep(giro)
                        motor.stop('ALL')
                        
                        

    except KeyboardInterrupt:
        print("Programa finalizado")

