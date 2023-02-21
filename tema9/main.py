# BIBLIOTECA STANDARD DE PYTHON Y FUNCIONES BUILT IN
# TODO programacion multihilos
# hay que darle tiempo para que se ejecuten los hilos
# por que si el programa principal se ejecuta muy rapido no se alcanzan a ejecutar los hilos
# se ejcuta el primer hilo y sigue con el segundo sin esperar a terminar el primer hilo
import _thread
import time

def horaActual(nombreThread,tiempoEspera):
    count = 0
    while count < 5:
        time.sleep(tiempoEspera)
        count += 1
        print(f'hilo: {nombreThread} - {time.ctime(time.time())}')

_thread.start_new_thread(horaActual, ('thread_uno',1))
_thread.start_new_thread(horaActual, ('thread_dos',2))
print('he disparado ya los hilos')
while True:
    pass

