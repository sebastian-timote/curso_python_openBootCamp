class Alumno:
    nombre = ''
    nota = 0.0
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def imprimirDataAlumno(self):
        print('nombre:',self.nombre)
        print('nota:',self.nota)

    def isAprovado(self):
        if (self.nota and self.nombre):
            if (self.nota >= 3.0 and self.nota <= 5.0):
                print('el sr.', self.nombre,' con una nota de ', self.nota,' ha aprovado el curso FELICITACIONES!!')
            else:
                if self.nota > 5.0:
                    return print('dato erroneo el rango de la nota debe ser de 1.0 a 5.0')
                print('el sr.', self.nombre,' con una nota de ', self.nota,' ha Perdido el curso a ESTUDIAR SE DIJO!!')

        else:
            print('no se ha actualizado la nota o el nombre del alumno')
    
n = Alumno('',2)
n.imprimirDataAlumno()
n.isAprovado()