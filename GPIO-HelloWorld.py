import RPi.GPIO as GPIO     #importa a bibliote GPIO
import time                 #importa a biblioteca de temporização

GPIO.setmode(GPIO.BOARD)    #GPIO - utilizando a pinagem fisica da placa
GPIO.setwarnings(False)     #desabilitar mensagens de warning

GPIO.setup(7, GPIO.OUT)     #define o pino 7 como saída

while(1):
    print('LED (7) ON')
    GPIO.output(7, GPIO.HIGH)   #ligando o LED

    time.sleep(2)

    print('LED (7) OFF')
    GPIO.output(7, GPIO.LOW)    #desligando o LED

    time.sleep(2)
    
