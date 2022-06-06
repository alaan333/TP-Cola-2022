# 18 - Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
# letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
# que resuelva las siguientes situaciones:
# a. cargar 1000 turnos de manera aleatoria a la cola.
# b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
# y F, y la cola_2 con el resto de los turnos (B, D y E).
# c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
# tiene mayor cantidad.
# d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
# mayor que 506.

from cola import Cola
from random import randint
codigo_turno='#@@@'
c1=0
c2=0
c3=0
cola_aux=Cola()
cola1=Cola()
cola2=Cola()
cola3=Cola()
ctrl_colas=False

def letra_aleatoria():
    return chr(randint(65,70)) 

def num_alea():
    return chr(randint(48,57))

# a. cargar 1000 turnos de manera aleatoria a la cola.
for i in range (10):
    codigo_turno=letra_aleatoria()+num_alea()+num_alea()+num_alea()
    cola1.arribo(codigo_turno)
    #print('Este es el codigo',codigo_turno)
print()   

# b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
# y F, y la cola_2 con el resto de los turnos (B, D y E).
while (not cola1.cola_vacia()):
    dato=cola1.atencion()
    if (dato[0]=='A' or dato[0]=='C' or dato[0]=='F'):
        cola2.arribo(dato)
    else:
        cola3.arribo(dato)

# c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
# tiene mayor cantidad.
if (cola2.tamanio()>cola3.tamanio()):    
    while (not cola3.cola_vacia()):              #ciclo para el punto D  
        cola_aux.arribo(cola3.atencion())

    print('La cola A-C-F tiene mas cantidad de turnos')
    while( not cola2.cola_vacia()):
        dato=cola2.atencion()
        if (dato[0]=='A'):
            c1+=1
        elif (dato[0]=='C'):
            c2+=1
        else:
            c3+=1
    if (c1==c2 or c1==c3 or c2==c3):
        print('Dos o tres letras tienen la misma cantidad de turnos')
    else:
        if (c1>c2 and c1>c3):
            print('La letra con mayor cantidad de turnos es la "A"')
        elif (c2>c3):
            print('La letra con mayor cantidad de turnos es la "C"')
        else:
            print('La letra con mayor cantidad de turnos es la "F"')
    print()
elif(cola3.tamanio()>cola2.tamanio()):
    while (not cola2.cola_vacia()):             #ciclo para el punto D  
        cola_aux.arribo(cola2.atencion())                 

    print('La cola B-D-E tiene mas cantidad de turnos')
    while( not cola3.cola_vacia()):
        dato=cola3.atencion()
        if (dato[0]=='B'):
            c1+=1
        elif (dato[0]=='D'):
            c2+=1
        else:
            c3+=1
    if (c1==c2 or c1==c3 or c2==c3):
        print('Dos o tres letras tienen la misma cantidad de turnos')
    else:
        if (c1>c2 and c1>c3):
            print('La letra con mayor cantidad de turnos es la "B"')
        elif (c2>c3):
            print('La letra con mayor cantidad de turnos es la "D"')
        else:
            print('La letra con mayor cantidad de turnos es la "E"')
    print()
else:
    print('Ambas colas tienen la misma cantidad de turnos')
    ctrl_colas=True                #para el punto D
    print()

# d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
# mayor que 506.
if (not ctrl_colas):     #para que no entre en el caso de que sean iguales
    ctrl=False
    print('Turnos de la cola con menor cantidad de turnos, mayores a 506:')
    while(not cola_aux.cola_vacia()):
        dato=cola_aux.atencion()
        if (dato[1]>='5') and (dato[3]>='6'):
            print(dato)
            ctrl=True
    if (not ctrl):
        print('No hay turnos mayores a 506')