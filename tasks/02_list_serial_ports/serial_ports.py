from serial.tools import list_ports

ports = list_ports.comports()
if not ports:
    print("COM порты не найдены")
else: 
    for port in ports:
        print("Порт:", port.device)
        print("Описание:", port.description)