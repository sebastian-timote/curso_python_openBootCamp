
#realizar un script que nos diga la hora de ir a casa usando modulo time
# usamos la fecha del sistema y poder comprobar la hora
# en caso de que sean mas de las 1900h, se mortrara un mensaje y en caso contrario
# hareis una operacion para calcular el tiempo que queda de trabajo

import time
import pprint
def main():
    #tomo el tiempo actual
    tiempoactual = time.localtime()
    def horaSalida(hora):
        #separamos horas de minutos y los ponemos en variables diferentes
        #y las retornamos
        horas = ''
        min = ''
        ciclos = 0
        for i in hora:
            ciclos+=1
            if ciclos <= 2:
                horas += i
                continue
            min+=i
        return horas,min
    
    hour,minutes = horaSalida('1900')

    def alertSalida(timeH,timeM):
        #nosmuestra mensaje de si es hora de ir a casa
        #convertimos a entero ya que es string
        timeH = int(timeH)
        timeM = int(timeM)
        #tomamos de la tupla el campo de la hora 
        horaStrAct = tiempoactual.tm_hour
        # tomamos de la tupla el campo de los minutos
        minStrAct = tiempoactual.tm_min
        if ((horaStrAct >= timeH) and (minStrAct >= timeM )):
            print('es hora de ir a casa te pasaste de la hora')
        else:
            horas,minutos = restaEntreDosHoras(timeH,timeM,horaStrAct,minStrAct)
            
            print('sigue trabajando falta ', horas,'h:',minutos,'m de trabajo')
    
    def restaEntreDosHoras(horaFinal,minFinal,horaInicial,minInicial):
        # resta de horas y min muestra las horas y los minutos de diferencia entre dos horas

        horafInt = int(horaFinal)
        minfInt = int(minFinal)
        horaiInt = int(horaInicial)
        miniInt = int(minInicial)

        minRestante = minfInt - miniInt
        #comprueba si la operacion da negativo
        if minRestante < 0 :
            minRestante = 60 - miniInt
            horaiInt += 1
        
        horRestante = horafInt - horaiInt

        return horRestante,minRestante
 
    alertSalida(hour,minutes)
if __name__ == '__main__':
    main()
