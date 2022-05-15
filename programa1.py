#programa 1
import time
import threading
from random import randint

def MedeSensor(thread_name):
    while 1:
        time.sleep(randint(1,5) + thread_name)
        sensor = randint(1,10)
        print("Valor medido do sendor: ", sensor, "Thread executada: ", thread_name)


#programa principal
ValorSensor1 = threading.Thread(target = MedeSensor, args=(1,))
ValorSensor1.start()
ValorSensor2 = threading.Thread(target = MedeSensor, args=(2,))
ValorSensor2.start()

while 1:
    print("Executando programa principal")
    time.sleep(1)

