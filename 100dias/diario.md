###  Perfil de Tryhackme 
*__https://tryhackme.com/p/Tanotash__*

#  Dia 0 viernes 26 de marzo 

##  Progreso del dia.
realice el room de THM Lian Yu https://tryhackme.com/room/lianyu, es un room para nivel iniciante, sobre el arrowverse, donde se busca sacar informacion de una pagina que se desplego, hice uso de logeo en ftp y escalamiento de privilegios para obtener las respectivas flags adjunto el archivo aa.jpg como evidnecia que incluida dentro otro archivo comprimido 

#  Dia 1 sabado 27 de marzo

##  Progreso del dia.
Realice el room Break out the cage https://tryhackme.com/room/breakoutthecage1 donde tuve que hace enumeracion para saber sus vulneravilidades y saber donde ubicarme 
adjunto prueba de enumeracion en el archivo cage.png donde utilice gobuster para enumerar los directorios por fuerza bruta 

#  Dia 3 domingo 28 de marzo 

## Progreso del dia 

siguiendo con la dinamica de acabar el roadmap de THM trate de realizar la room Buffer Overflow Prep https://tryhackme.com/room/bufferoverflowprep pero por falta de conocimiento y porque se me juntaron mas proyectos decidi dejarla en reposo por un tiempo espero retomarla en un tiempo, es un problema que me pasa con las maquina remotas de windows, no gozo de muchos recursos en mi laptop y me cuesta mucho trabajo organizarme con tantos programas abiertos 

# Dia 4 Lunes 29 de marzo 

## progreso del dia

este dia estuve haciendo algunas nstalaciones para poder realizar el room https://tryhackme.com/room/attacktivedirectory puesto que anteriormente ya habia utilizado bloodhount pero en la maquina virtual de THM asi que decidi instalarlo en en mi pc, ademas de algunas otras instalaciones para poder realizar este room, estoy pensando seriamente en pasarme a kali puesto que lo tiene ya preinstalado 

# Dia 5 martes 30 de marzo

## progreso del dia 

aunque este repositorio es para la realizacion de los rooms de THM, cumpliendo con el reto de 100 de codigo en ciberseguridad, hize la instalacion de la maquina virtual de badstore para su posterior analisis y enumeracion de vulneravilidades que hice el dia siguiente usando el programa de virtualbox para correrla configurando como sistema linux y cambiando la opcion de red a solo anfitrion 

# dia 6 miercoles 31 de marzo 

## Progreso del dia 

se busco vulneravilidades en la maquina instalada previamente en el dia 5 que en su mayoria era sqlinjection que use sqlmap para poder ver la base datos de items aunque no me daba como tal toda la base de datos solo la de los usuarios admin y uno con permisos custumer, viendo igual que la contraseña por defecto al crear un usuario era welcome que se almacenaba en formato MD5 

# Dia 7 jueves 31 de marzo

## progreso del dia

Se continuo con el room dejado en el dia 4, acabando de instalar bloodhount, utilice la maquina virtual de THM para usar enum4linux para enumerar la ip que me dio la maquina a desplegar para posteriormente resolver las dudas, despues de esto procedi a instalar kerbrute para el siguiente modulo 

# Dia 8 viernes 1 de abril 

## progreso del dia 

desifrando con kerberus se optubo un hash para decodificar, intente con hashcat pero e tenido problemas para usarlo, e encontrado diferentes manuales pero aveces no se cual es de cual, entrando ala wiki de hashes el que me da es un 18200 pero en mi hashcat me da un 7500 una vez viendo esto intente pero tampoco me dejo asi que decidi correrlo con john y asi obtube la contraseña que estaba en hash Kerberos 5 AS-REQ Pre-Auth etype 23, despues de esto entre smbclient y asi encontrar un archivo que contenia un archivo en base64 que tenia en su interior "backup@spookysec.local:backup2517860"
