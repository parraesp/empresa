__author__ = 'Alberto L'

class Departamento:
    def __init__(self, nombre_depto, id_depto):
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.lista_empleados = []

    def aniadir_empleado(self, empleado):
        self.lista_empleados.append(empleado)

    def get_salario_total(self):
        suma  = 0
        for i in self.lista_empleados:
            suma += i.get_salario()
        return suma