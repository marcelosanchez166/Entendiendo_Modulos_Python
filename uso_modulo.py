import modulos #ayuda para importar y optimizar el uso de reserva de memoria dado que no estoy importando todo lo del archivo modulo

#por ejemplo si solo importo modulos debo instanciar cada funcion y es lo que hace optimizar el uso de memoria
modulos.sumar(7,3)
modulos.restar(8,3)


"""###############################################"""

from modulos import * #Al importar todo lo del archivo con el asterisco reservo un gran tamaño de memoria, pero es mas facil usar 
#todas las funciones del archivo
"""El nombre del archivo debe ser diferente a la carpeta donde se encuentre para que no de problemas cuando manda a llamar las funciones"""

#Eje:
sumar(9,5)
restar(9,4)




