# 22 - Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
# Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
from cola import Cola

iron={'nombre':'Tony Stark','superheroe':'Iron Man','genero':'M'}
widow={'nombre':'Natasha Romanoff','superheroe':'Black Widow','genero':'F'}
elcapi={'nombre':'Steve Rogers','superheroe':'Capitan America','genero':'M'}
raccoon={'nombre':'Rocket Raccoon','superheroe':'Ranger Rocket','genero':'M'}
lord={'nombre':'Peter Jason Quill','superheroe':'Star-Lord','genero':'M'}
thor={'nombre':'Thor','superheroe':'Thor','genero':'M'}
doctor={'nombre':'Stephen Strange','superheroe':'Dr. Strange','genero':'M'}
capitana={'nombre':'Carol Danvers','superheroe':'Capitana Marvel','genero':'F'}
gamora={'nombre':'Gamora Zen Whoberi Ben Titan','superheroe':'Gamora','genero':'F'}
drax={'nombre':'Arthur Sampson Douglas','superheroe':'Drax','genero':'M'}
ant={'nombre':'Scott Lang','superheroe':'Ant-Man','genero':'M'}

cola1=Cola()

class Datos_personajes():
    nombre,alias,genero=None,None,None

personajes=[iron,widow,elcapi,raccoon,lord,thor,doctor,capitana,gamora,drax,ant]

for i in range(len(personajes)):
    dato=Datos_personajes()
    dato.nombre=personajes[i]['nombre']
    dato.alias=personajes[i]['superheroe']
    dato.genero=personajes[i]['genero']
    cola1.arribo(dato)

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
for i in range(cola1.tamanio()):
    if (cola1.mover_al_final().alias=='Capitana Marvel'):
        dato=cola1.el_final()                              #el_final, funcion nueva para mostrar el final de la cola
        print('Nombre de la capitana marvel:')
        print(dato.nombre)
print()
# b. mostrar los nombre de los superhéroes femeninos;
print('Superheroes femeninas: ')
for i in range(cola1.tamanio()):
    if (cola1.mover_al_final().genero=='F'):
        print(cola1.el_final().nombre)
print()
# c. mostrar los nombres de los personajes masculinos;
print('Superheroes masculinos: ')
for i in range(cola1.tamanio()):
    if (cola1.mover_al_final().genero=='M'):
        print(cola1.el_final().nombre)
print()
# d. determinar el nombre del superhéroe del personaje Scott Lang;
print('Nombre de superheroe de Scott Lang:')
for i in range(cola1.tamanio()):
    if (cola1.mover_al_final().nombre=='Scott Lang'):
        print(cola1.el_final().alias)
print()
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
print('Datos de los personajes cuyo alias o nombre de pila empiezan con la letra S:')
for i in range(cola1.tamanio()):
    if (cola1.mover_al_final().nombre[0]=='S') or (cola1.el_final().alias[0]=='S'):     #mover_al_final no se puede usar dos veces seguidas
        print(cola1.el_final().nombre,', ',cola1.el_final().alias,', ',cola1.el_final().genero)
print()
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
for i in range(cola1.tamanio()):
    if (cola1.mover_al_final().nombre=='Carol Danvers'):
        print('El personaje Carol Danvers se encuentra en la cola')
        print(f'Su nombre de superheroe es {cola1.el_final().alias}')