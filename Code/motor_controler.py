import RPi.GPIO as GPIO
import time

class MotorController:
    def __init__(self):
        self.ena = 12
        self.in1 = 17
        self.in2 = 27
        self.enb = 13
        self.in3 = 22
        self.in4 = 23
        
        self.velocity = 10
        
        print(self.ena, self.in1, self.in2, self.enb, self.in3, self.in4)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.enb, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)

        self.pwm_a = GPIO.PWM(self.ena, 1000)
        self.pwm_b = GPIO.PWM(self.enb, 1000)

        self.pwm_a.start(0)
        self.pwm_b.start(0)
        
    def get_velocity(self):
        return self.velocity
    
    def set_velocity(self, vel):
        if self.velocity != 100 and self.velocity != 0:
            self.velocity = vel
            
    def backward(self, motor, speed):
        print("acelerando")
        if motor == 'A' or motor == 'ALL':
            GPIO.output(self.in1, GPIO.HIGH)
            GPIO.output(self.in2, GPIO.LOW)
            GPIO.output(self.ena, GPIO.HIGH)
            self.pwm_a.ChangeDutyCycle(speed)
        if motor == 'B' or motor == 'ALL':
            print("me muevoooo")
            GPIO.output(self.in3, GPIO.HIGH)
            GPIO.output(self.in4, GPIO.LOW)
            GPIO.output(self.enb, GPIO.HIGH)
            self.pwm_b.ChangeDutyCycle(speed)

    def forward(self, motor, speed):
        if motor == 'A' or motor == 'ALL':
            print("palante")
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.HIGH)
            GPIO.output(self.ena, GPIO.HIGH)
            self.pwm_a.ChangeDutyCycle(speed)
            self.set_velocity(speed)
        if motor == 'B' or motor == 'ALL':
            print("palante")
            GPIO.output(self.in3, GPIO.LOW)
            GPIO.output(self.in4, GPIO.HIGH)
            GPIO.output(self.enb, GPIO.HIGH)
            self.pwm_b.ChangeDutyCycle(speed)
            self.set_velocity(speed)

    def stop(self, motor):
        if motor == 'A' or motor == 'ALL':
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.LOW)
            GPIO.output(self.ena, GPIO.LOW)
            self.set_velocity(0)
        if motor == 'B' or motor == 'ALL':
            GPIO.output(self.in3, GPIO.LOW)
            GPIO.output(self.in4, GPIO.LOW)
            GPIO.output(self.enb, GPIO.LOW)
            self.set_velocity(0)

    def turn_left(self, speed=50, duration=1):
        self.forward('A', speed / 4)
        self.forward('B', speed)
        time.sleep(duration)
        self.set_velocity(speed)
        self.forward('ALL', speed)

    def turn_right(self, speed=50, duration=1):
        self.forward('A', speed)
        self.forward('B', speed / 4)
        time.sleep(duration)
        self.set_velocity(speed)
        self.forward('ALL', speed)

    def turn_angle(self, angle, direction='left', speed=50):
        # Definir la relación entre el tiempo de giro y el ángulo (experimental)
        time_per_degree = 1 / 90  # Esto es un ejemplo, debes calibrarlo según tu robot
        time_to_turn = abs(angle) * time_per_degree + 1

        if direction == 'left':
            print("left")
            self.turn_left(speed, time_to_turn)
        elif direction == 'right':
            print("right")
            self.turn_right(speed, time_to_turn)
        else:
            print("Dirección no válida")
            return

    def cleanup(self):
        self.pwm_a.stop()
        self.pwm_b.stop()
        GPIO.cleanup()
