#Implementacao de um codigo para controle de um led

import RPi.GPIO as GPIO
import time

#Configura o modo de pinagem do raspberry
GPIO.setmode(GPIO.BOARD) #pinout como o da placa

#Configurar uma porta GPIO como nivel baixo pull down
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Configura uma porta como saida
GPIO.setup(38, GPIO.OUT)

led_aceso = 0
led_contador = 0

#Funcao 
def controla_led(channel):
    #como as variaveis sao globais deve-se declaralas
    global led_aceso
    global led_contador
    print("Botao foi presionado")
    if led_aceso == 0:
        GPIO.output(38, GPIO.HIGH)
        led_aceso = 1
        
    elif led_aceso == 1:
        GPIO.output(38, GPIO.LOW)
        led_aceso = 0
        
    led_contador = led_contador + 1 
    #time.sleep(1)
    


#Funcao de callback de interrupcao
#cria o tratamento do evento de deteccao de uma board de subida
#no pino 36 do GPIO. debounce de 200ms. 
GPIO.add_event_detect(36, GPIO.RISING, callback=controla_led,
                      bouncetime=200)

#Programa principal
try:
    while True:
         
        print("Programa principal")
        if led_aceso == 0:
            print("O led esta apagado")
        else:
            print("O led esta aceso")
        print("O botao foi pressionado ", + led_contador, "vezes")    
        time.sleep(1)

#ocorre quando o control + c e pressinado
except KeyboardInterrupt:
    GPIO.output(38, GPIO.LOW)
    print("Programa sendo finalizado")
    exit()

