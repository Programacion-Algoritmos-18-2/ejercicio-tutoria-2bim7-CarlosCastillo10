
import codecs
import sys

# Clase que permite leer el archivo
class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/data_combinacion.txt", "r") # Abrimos el archivo

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()



