import serial

class Communicator:
    def __init__(self):
        self.ser = serial.Serial('COM10', 9600, timeout=1)
        self.ser.flush()

    def turn_on(self):
        self.ser.write(bytes("1", 'utf-8'))

    def turn_off(self):
        self.ser.write(bytes("0", 'utf-8'))
