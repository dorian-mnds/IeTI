from serial import Serial
import serial.tools.list_ports
if __name__ == "__main__":
    serial_port = serial.tools.list_ports.comports()
    # To obtain the list of the communication ports
    for port in serial_port:
        print(f"{port.name} // {port.device} // D={port.description}")
    # To select the port to use
    selectPort = input("Select a COM port : ")
    print(f"Port Selected : COM{selectPort}")
    # To open the serial communication at a specific baudrate
    # serNuc = Serial('COM'+str(selectPort), 115200)  # Under Windows only
    serNuc = Serial(str(selectPort), 115200)  # Under Mac only
    appOk = 1
    while appOk:
        data_to_send = input("Char to send : ")
        if data_to_send == 'q' or data_to_send == 'Q':
            appOk = 0
        else:
            serNuc.write(bytes(data_to_send, 'ascii'))
            while serNuc.inWaiting() == 0:
                pass
            data_rec = serNuc.read(1)  # bytes
            print(str(data_rec))

    serNuc.close()
