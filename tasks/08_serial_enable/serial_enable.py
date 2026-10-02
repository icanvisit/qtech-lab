import serial
from serial.tools import list_ports
import time

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

            port.write(b"enable\r")
            time.sleep(1)
            data = port.read_all()
            enable_response = data.decode(errors="replace")
            print("Ответ устройства")
            print(enable_response)
#Чтоб не гадать хостнейм каждый раз
            prompt = ""
            for line in enable_response.splitlines():
                if line.strip():
                    prompt = line.strip()
#Обязательно нужно разбить на два блока, иначе не успеет перейти в enable
            print("Отправляем show run")
            port.write(b"show run\r")
            time.sleep(2)
            output = ""
#Тут используем цикл While для полного вывода конфига, чтоб не споткнуться об --More--
            while True:
                data = port.read_all()
                chunk = data.decode(errors="replace")
                output += chunk

                if "--More--" in chunk:
                    port.write(b" ")
                    time.sleep(1)
                elif prompt in chunk:
                    break
                else:
                    time.sleep(1)

            print(output)
            port.close()
            print("Порт закрыт")
        except serial.SerialException as error:
            print("Ошибка работы COM порта",error)
if not port_found:
    print("Порт не найден")

