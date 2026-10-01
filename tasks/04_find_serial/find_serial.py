from serial.tools import list_ports
import serial

ports = list_ports.comports()
if not ports:
    print("COM порты не найдены")
else:
    for port in ports:
     print('Порт', port.device)

selected_port = input("Введите порт:")
port_found = False

for port in ports:
    if selected_port == port.device:
        port_found = True

if port_found:
    print("Порт найден", selected_port)
else:
    print("Порт не найден", selected_port)