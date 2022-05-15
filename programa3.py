#programa que exemplifica o uso de um recurso por duas threads. 

#programa 1
import time
import threading
from random import randint

lock = threading.Lock()

def MedeSensor(thread_name):
    while 1:
        if(thread_name == 1):
            ValorBase = 10
        if(thread_name == 2):
            ValorBase = 51
            
        tempo = randint(1,5)
        tempo1 = tempo * thread_name
        time.sleep(tempo1)
        #bloqueia o recurso para que nenhuma thread execute a porcao do codigo 
        
        lock.acquire() 
        
        tempoProcessamento = 10
        while(tempoProcessamento > 0):
            time.sleep(1)
            sensor = randint(1,5) + ValorBase
            print "Valor calculado do processo ", thread_name, "igual a: ", sensor
            tempoProcessamento = tempoProcessamento - 1
            #print(tempoProcessamento)
        
        
        lock.release() #desbloqueia o recurso 
        
        

#programa principal
ValorSensor1 = threading.Thread(target = MedeSensor, args=(1,))
ValorSensor1.start()
ValorSensor2 = threading.Thread(target = MedeSensor, args=(2,))
ValorSensor2.start()

while 1:
    print("Executando programa principal")
    time.sleep(1)



