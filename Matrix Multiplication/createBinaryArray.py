import struct
data = struct.pack('9f', 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3)
with open('D.bin', 'wb') as f:
    f.write(data)
