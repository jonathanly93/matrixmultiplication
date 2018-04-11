import binascii
import struct

n = 9
filePath = 'C:\Users\Jayly\Desktop\Mars\D.bin'
file = open(filePath, "rb")
with file:
    print(struct.unpack('f'*n, file.read(4*n)))
