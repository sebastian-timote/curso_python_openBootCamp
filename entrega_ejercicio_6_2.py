class Alumno:
    nombre = ''
    nota = 0.0

    def setNombreAlumno(self, nombre):
        self.nombre = nombre
    def setNotaFinalAlumno(self, nota):
        self.nota = nota
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
    
n = Alumno()
n.setNombreAlumno('sebas')
n.setNotaFinalAlumno(5.0)
n.isAprovado()