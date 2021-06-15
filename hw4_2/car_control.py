enable_lens_corr = False
import pyb, sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

uart = pyb.UART(3,9600,timeout_char=1000)
uart.init(9600,bits=8,parity = None, stop=1, timeout_char=1000)

min_degree = 0
max_degree = 179

'''while(True):
    uart.write("/stop/run \n".encode())  
    time.sleep(1)
    uart.write("/goStraight/run -50 \n".encode())
    time.sleep(1)'''
while(True):
    clock.tick()
    img = sensor.snapshot()
    if enable_lens_corr: img.lens_corr(1.8) # for 2.8mm lens...
    for l in img.find_lines(threshold = 1000, theta_margin = 25, rho_margin = 25):
        if (min_degree <= l.theta()) and (l.theta() <= max_degree):
            img.draw_line(l.line(), color = (255, 0, 0))
            print(l.theta())
            if(l.theta()>90): ##turn left
                turn_degree = l.theta() -90
                print(turn_degree)
                turn_time = (turn_degree/90) * 3 
                uart.write("/turn/run -50 -0.1 \n".encode())
                time.sleep(turn_time)
                uart.write("/goStraight/run -50 \n".encode())
                time.sleep(3)
                uart.write("/stop/run \n".encode())
                break
            elif(l.theta()<90): ##turn right
                turn_degree = 90 - l.theta()
                print(turn_degree)
                turn_time = (turn_degree/90) * 3.8
                uart.write("/turn/run -50 0.1 \n".encode())
                time.sleep(turn_time)
                uart.write("/goStraight/run -50 \n".encode())
                time.sleep(3)
                uart.write("/stop/run \n".encode())
                break
    print("FPS %f" % clock.fps())