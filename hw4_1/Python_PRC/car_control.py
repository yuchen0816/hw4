import time
import serial
import sys,tty,termios

s = serial.Serial(sys.argv[1])

position = input("poisition:")
d1 = int(input("d1:"))
d2 = int(input("d2:"))

print(position)
print(d1)
print(d2)
a = d2/8
b = (d1 + 15)/8

if position == 'west':
    s.write("/goStraight/run -50 \n".encode())
    time.sleep(a)
    s.write("/stop/run \n".encode())
    s.write("/turn/run -50 -0.1 \n".encode())
    time.sleep(2.15)
    s.write("/stop/run \n".encode())
    s.write("/goStraight/run -50 \n".encode())
    time.sleep(b)
    s.write("/stop/run \n".encode())

elif position == 'east':
    s.write("/goStraight/run -50 \n".encode())
    time.sleep(a)
    s.write("/stop/run \n".encode())
    s.write("/turn/run -50 0.1 \n".encode())
    time.sleep(2.35)
    s.write("/stop/run \n".encode())
    s.write("/goStraight/run -50 \n".encode())
    time.sleep(b)
    s.write("/stop/run \n".encode())

elif position == 'south':
    s.write("/goStraight/run -50 \n".encode())
    time.sleep(b)
    s.write("/stop/run \n".encode())

