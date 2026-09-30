import serial

try:
    port = serial.Serial (
        port="COM99",
        baudrate=9600,
        timeout=1
    )
    
    
    print("Порт открыт")
    port.close()

except serial.SerialException:
    print("Порт COM99 недоступен")