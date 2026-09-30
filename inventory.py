devices = [
    {
        "hostname": "R1",
        "com_port": "COM3",
        "model": "QSR-1000",
        "role": "router",
        "management_ip": "192.168.0.1"
    },
    {
        "hostname": "SW1",
        "com_port": "COM4", 
        "model": "QSW-4530",
        "role": "switch",
        "management_ip": "192.168.0.2"
    },
    {
        "hostname": "SW2", 
        "com_port": "COM5", 
        "model": "QSW-4530", 
        "role": "switch",
        "management_ip": "192.168.0.3"
    },
    {
        "hostname": "SW3", 
        "com_port": "COM6", 
        "model": "QSW-4530", 
        "role": "switch",
        "management_ip": "192.168.0.4"
    },
]
def count_devices_by_role(devices,role):
    count = 0

    for device in devices:
        if device['role'] == role:
            count += 1

    return count

switches = count_devices_by_role(devices,'switch')
routers = count_devices_by_role(devices,'router')

print('Коммутаторов', switches)
print('Маршрутизаторов', routers)
try:
    with open('.\\qtech-lab\\inventory.txt', 'r', encoding='utf-8') as file:
        saved_inventory = file.read()

    print('Содержание файла')
    print(saved_inventory)

except FileNotFoundError:
    print('Файл не найден')
    

