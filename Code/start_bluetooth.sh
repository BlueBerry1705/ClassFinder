#!/bin/bash

# Iniciar el servicio rfcomm para escuchar conexiones Bluetooth
sudo rfcomm release /dev/rfcomm0
sleep 1
sudo rfcomm watch hci0 &

sleep 3

# Ejecutar código para leer mensajes a través del puerto serial Bluetooth
python3 /home/pi/Documents/Robotito/main.py

