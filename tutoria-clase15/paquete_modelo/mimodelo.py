
class Persona(object):

	# Constructor
	def __init__(self,n,a,ed):

		self.agregar_nombre(n)
		self.agregar_apellido(a)
		self.agregar_edad(ed)
		
	# Metodos de agregar
	def agregar_nombre(self, n):
		self.nombre = n

	def agregar_apellido(self, a):
		self.apellido = a

	def agregar_edad(self, ed):
		self.edad = int(ed) # Convertimos a entero lo que recibe el metodo

	# Metodos de obtener
	def obtener_nombre(self):
		return self.nombre

	def obtener_apellido(self):
		return self.apellido

	def obtener_edad(self):
		return self.edad

	def __str__(self):

		return "\nNombre: %s\nApellido: %s\nEdad: %d\n"%(self.obtener_nombre(),self.obtener_apellido(),self.obtener_edad())

	def __repr__(self):

		return "\nNombre: %s\nApellido: %s\nEdad: %d\n"%(self.obtener_nombre(),self.obtener_apellido(),self.obtener_edad())



	