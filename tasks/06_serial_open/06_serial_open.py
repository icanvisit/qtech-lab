import serial
from serial.tools import list_ports

ports = list_ports.comports()
if not ports:
    print("COM порты не найдены")
else:
    for port in ports:
        print("Порт", port.device)

selected_port = input("Введите порт:")
port_found = False

for port in ports:
    if selected_port == port.device:
        port_found = True
        try:
            port = serial.Serial(
                port = selected_port,
                baudrate=9600,
                timeout=1
            )
            print("Порт открыт")

            port.write(b"\r")
            print("Enter отправлен")

            port.close()
            print("Порт закрыт")
        except serial.SerialException as error:
            print("Ошибка работы COM порта",error)
if not port_found:
    print("Порт не найден")

