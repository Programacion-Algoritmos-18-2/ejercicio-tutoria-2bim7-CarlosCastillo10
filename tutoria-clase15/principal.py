
"""
	Importamos las clases que necesitamos de los modulos.
"""
from paquete_modelo.mimodelo import Persona
from paquete_archivos.miarchivo import MiArchivo
from paquete_ordenamiento.miordenacion import *


m = MiArchivo() # objeto para leer el archivo

lista = m.obtener_informacion() # Guardamos lo que retorna el metodo
lista = [l.split(";") for l in lista] # Separamos por ';' el txt

listado_edades = [] # Lista que va a guardar las edades

for x in lista:
	p = Persona(x[0],x[1],x[2]) # Creamos el objeto de tipo Persona y le enviamos los parametros
	listado_edades.append(p.obtener_edad()) # Agregamos en la lista las edades

merge_sort_result = merge_sort(listado_edades)  # Guardamos en 'merge_sort_result' lo que retorna el metodo 'merge_sort' y le enviamos la lista de edades

print(merge_sort_result) # Presentamos en pantalla

m.cerrar_archivo() # Cerramos el archivos





