
import time
import pprint
def main():
    
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
    
    hour,minutes = horaSalida('1815')

    def alertSalida(timeH,timeM):
        timeH = int(timeH)
        timeM = int(timeM)
        horaStrAct = tiempoactual.tm_hour
        minStrAct = tiempoactual.tm_min
        if ((horaStrAct >= timeH) and (minStrAct >= timeM )):
            print('es hora de ir a casa te pasaste de la hora')
        else:
            horas,minutos = restaEntreDosHoras(timeH,timeM,horaStrAct,minStrAct)
            
            print('sigue trabajando falta ', horas,'h:',minutos,'m de trabajo')
    
    def restaEntreDosHoras(horaFinal,minFinal,horaInicial,minInicial):
        horafInt = int(horaFinal)
        minfInt = int(minFinal)
        horaiInt = int(horaInicial)
        miniInt = int(minInicial)

        minRestante = minfInt - miniInt
        if minRestante < 0 :
            minRestante = 60 - miniInt
            horaiInt += 1
        
        horRestante = horafInt - horaiInt

        return horRestante,minRestante
 
    alertSalida(hour,minutes)
if __name__ == '__main__':
    main()
