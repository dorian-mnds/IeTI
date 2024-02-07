import serial
import serial.tools.list_ports

serial_port = serial.tools.list_ports.comports()

# Affiche les ports série conenctés à l'ordi
for port in serial_port:
    print(f"{port.name} // {port.device} // D={port.description}")

# Premier argument: nom du device de l'affichage préccédent correspondant à la nucléo
ser = serial.Serial("/dev/cu.usbmodem11303", baudrate=115200)

# Sending a char to Nucleo Board
ser.write(b'a')
# Waiting for data sending by Nucleo board
while(ser.in_waiting == 0):
    print("Wait !")
rec_data_nucleo = ser.readline(2)
print(f'Rec = {rec_data_nucleo}')
ser.close()
