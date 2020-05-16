# la funcion filter aplica una condicion y aqui en map aplica una funcion

class Empleado:

    def __init__(self, nombre, cargo, salario):

        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):

        return "{} que trabaja como {} y tiene un salario de S/.{}".format(self.nombre, self.cargo, self.salario)

lista_empleados = [

    Empleado("Juan", "Director", 7500),
    Empleado("Ana", "Secretaria", 5000),
    Empleado("Julia", "Admistradora", 2800),
    Empleado("Khaleesi", "Manager", 1500),
    Empleado("Rocky", "Gerente", 4000),
    Empleado("Johanni", "Editora", 1800),
]

def calculo_comision(empleado):
    if empleado.salario <=3000:
        empleado.salario = empleado.salario * 1.03
    return empleado

lista_empleados_comision = map(calculo_comision,lista_empleados)

for Empleado in lista_empleados_comision:

    print(Empleado)