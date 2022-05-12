import RPi.GPIO as GPIO
from time import sleep
from math import sqrt

# halfstep advance sequence
adv = [ (1,0,0,1), (0,0,0,1), (0,0,1,1), (0,0,1,0),
        (0,1,1,0), (0,1,0,0), (1,1,0,0), (1,0,0,0)]

# halfstep reverse sequence
rev = [ (1,0,0,0), (1,1,0,0), (0,1,0,0), (0,1,1,0),
        (0,0,1,0), (0,0,1,1), (0,0,0,1), (1,0,0,1)]

# enable GPIO
GPIO.setmode(GPIO.BOARD)

# define the pins used for x and y steppers
stepper_x = (13, 11, 7, 5)
stepper_y = (8, 10, 12, 16)

# set the stepper pins to output
GPIO.setup(stepper_x, GPIO.OUT)
GPIO.setup(stepper_y, GPIO.OUT)

# initialize the steppers to 0 voltage
GPIO.output(stepper_x, 0)
GPIO.output(stepper_y, 0)

# set the servo pin to output and 50 Hz PWM frequency
GPIO.setup(19, GPIO.OUT)
servo = GPIO.PWM(19, 50)

# start the servo at rest
servo.start(0)

# function for extending the pen
def extend():
    servo.ChangeDutyCycle(9.5)
    sleep(0.2)
    servo.ChangeDutyCycle(0)

# function for retracting the pen
def retract():
    servo.ChangeDutyCycle(8)
    sleep(0.2)
    servo.ChangeDutyCycle(0)

# move upwards by n steps
def up(cycles):
    for _ in range(cycles):
        for step in range(8):
            GPIO.output(stepper_y, adv[step])
            sleep(0.0008)

# move downwards by n steps
def down(cycles):
    for _ in range(cycles):
        for step in range(8):
            GPIO.output(stepper_y, rev[step])
            sleep(0.0008)

# move left by n steps
def left(cycles):
    for _ in range(cycles):
        for step in range(8):
            GPIO.output(stepper_x, rev[step])
            sleep(0.0008)

# move right by n steps
def right(cycles):
    for _ in range(cycles):
        for step in range(8):
            GPIO.output(stepper_x, adv[step])
            sleep(0.0008)

# slant up and to the right n steps
def up_right(cycles):
    for _ in range(cycles):
        for step in range(16):
            GPIO.output(stepper_y, adv[step%8])
            if ((~step)&1):
                GPIO.output(stepper_x, adv[int(step/2)])
            sleep(0.0008)

# slant down and to the right n steps
def down_right(cycles):
    for _ in range(cycles):
        for step in range(16):
            GPIO.output(stepper_y, rev[step%8])
            if ((~step)&1):
                GPIO.output(stepper_x, adv[int(step/2)])
            sleep(0.0008)

# function for drawing the letter H
def draw_H():
    extend()
    up(320)
    retract()
    down(160)
    extend()
    right(160)
    retract()
    up(160)
    extend()
    down(320)
    retract()

# function for drawing the letter E
def draw_E():
    up(160)
    extend()
    right(160)
    retract()
    up(160)
    extend()
    left(160)
    down(320)
    right(160)
    retract()

# function for drawing the letter L
def draw_L():
    up(320)
    extend()
    down(320)
    right(160)
    retract()

# this is the equation for a quarter circle.
# it returns the difference in y-steps after each single x-step
def transform(val):
    curr = round(sqrt(1638400 - (val - 1280)**2))
    prev = round(sqrt(1638400 - (val - 1281)**2))
    return curr - prev

# map a series of x-steps to the corresponding number of y-steps 
# for a quarter circle
y_steps = [0] + list(map(transform, [i for i in range(1, 1280)]))

# function for drawing the letter O using four quarter circles
def draw_O():
    up(160)
    extend()
    current_y_step = 0
    for i in range(1000):
        GPIO.output(stepper_x, adv[i%8])
        sleep(0.0008)
        for _ in range(y_steps[i]):
            GPIO.output(stepper_y, adv[current_y_step])
            sleep(0.0008)
            current_y_step = (current_y_step + 1) % 8

    current_y_step = 0
    for i in range(1000):
        GPIO.output(stepper_x, adv[i%8])
        sleep(0.0008)
        for _ in range(y_steps[999-i]):
            GPIO.output(stepper_y, rev[current_y_step])
            sleep(0.0008)
            current_y_step = (current_y_step + 1) % 8
    left(40)
    current_y_step = 0
    for i in range(1000):
        GPIO.output(stepper_x, rev[i%8])
        sleep(0.0008)
        for _ in range(y_steps[i]):
            GPIO.output(stepper_y, rev[current_y_step])
            sleep(0.0008)
            current_y_step = (current_y_step + 1) % 8

    current_y_step = 0
    for i in range(1000):
        GPIO.output(stepper_x, rev[i%8])
        sleep(0.0008)
        for _ in range(y_steps[999-i]):
            GPIO.output(stepper_y, adv[current_y_step])
            sleep(0.0008)
            current_y_step = (current_y_step + 1) % 8
    retract()
    right(250)
    down(160)

# function for drawing the letter W
def draw_W():
    extend()
    down_right(160)
    up_right(60)
    down_right(60)
    up_right(140)
    retract()
    down(300)

# function for drawing the letter R
def draw_R():
    extend()
    up(320)
    right(160)
    down(160)
    left(180)
    right(40)
    down_right(80)
    retract()
    right(40)

# function for drawing the letter D
def draw_D():
    extend()
    up(320)
    current_y_step = 0
    for i in range(1280):
        GPIO.output(stepper_x, adv[i%8])
        sleep(0.0008)
        for _ in range(y_steps[1279-i]):
            GPIO.output(stepper_y, rev[current_y_step])
            sleep(0.0008)
            current_y_step = (current_y_step + 1) % 8
    
    current_y_step = 0
    for i in range(1280):
        GPIO.output(stepper_x, rev[i%8])
        sleep(0.0008)
        for _ in range(y_steps[i]):
            GPIO.output(stepper_y, rev[current_y_step])
            sleep(0.0008)
            current_y_step = (current_y_step + 1) % 8
    left(20)
    retract()
    right(160)

# sequence of letters to write "HELLO WORLD!"
draw_H()
right(40)
draw_E()
right(40)
draw_L()
right(40)
draw_L()
draw_O()
left(1000)
down(40)
draw_W()
right(20)
draw_O()
right(40)
draw_R()
right(60)
draw_L()
right(40)
draw_D()
right(40)
extend()
up(40)
retract()
up(40)
extend()
up(240)

servo.stop(0)
GPIO.cleanup()