import RPi.GPIO as GPIO     #importa a biblioteca GPIO
import time

GPIO.setmode(GPIO.BCM)      #GPIO - utilizando a numercao BCM(GPIO)

time_high = 0.05
time_low = 0
led = [2,3,4,17,27,22]
rev = [27,17,4,3]

for i in led:
    print(i)
    GPIO.setup(i, GPIO.OUT)
    
while(1):
    for i in led:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(time_high)
        GPIO.output(i, GPIO.LOW)
        time.sleep(time_low)
    for i in rev:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(time_high)
        GPIO.output(i, GPIO.LOW)
        time.sleep(time_low)
    
