# 16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.

from heap import HeapMax

cola_prioridad=HeapMax()

# a. cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).
cola_prioridad.agregar('Empleado Jose',1)
cola_prioridad.agregar('Empleado Carlos',1)
cola_prioridad.agregar('Empleado Manuel',1)

# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print(cola_prioridad.vector[0][0])
print()

# c. cargue dos documentos del staff de TI.
cola_prioridad.agregar('Proyecto Juan TI',2)
cola_prioridad.agregar('Proyecto Tomas TI',2)

# d. cargue un documento del gerente.
cola_prioridad.agregar('Gerente-Doc-1',3)

# e. imprima los dos primeros documentos de la cola.
print(cola_prioridad.vector[0][0],' ',cola_prioridad.vector[1][0])
print()

# f. cargue dos documentos de empleados y uno de gerente.
cola_prioridad.agregar('Empleado Lucas',1)
cola_prioridad.agregar('Empleado Antonio',1)
cola_prioridad.agregar('Gerente-Doc-2',3)

# g. imprima todos los documentos de la cola de impresión.
print('Cola final: ')
for i in range(len(cola_prioridad.vector)):
    print(cola_prioridad.vector[i][0])

