
"""
	Importamos las clases que necesitamos de los modulos.
"""
from paquete_modelo.mimodelo import Persona
from paquete_archivos.miarchivo import MiArchivo
from paquete_ordenamiento.miordenacion import *


m = MiArchivo() # objeto para leer el archivo

lista = m.obtener_informacion() # Guardamos lo que retorna el metodo
lista = [l.split(";") for l in lista] # Separamos por ';' el txt

listado_edades = []

for x in lista:
	p = Persona(x[0],x[1],x[2])
	listado_edades.append(p.obtener_edad())

merge_sort_result = merge_sort(listado_edades)  

print(merge_sort_result)

m.cerrar_archivo()





