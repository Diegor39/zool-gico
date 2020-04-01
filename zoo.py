
animales = list()
class Zoo:

 def __init__(self, nombre, tipo, clasificacion):
 	self.nombre = nombre
 	self.tipo = tipo
 	self.clasificacion = clasificacion

 def setNombre(self, nombre):
 	self.nombre = nombre
 def getNombre(self):
 	print("El nombre es: ", self.nombre)

 def setTipo(self, tipo):
 	self.tipo = tipo
 def getTipo(self):
 	print("El tipo es: ", self.tipo)

 def setClasificacion(self, clasificacion):
 	self.clasificacion = clasificacion
 def GetClasificacion(self):
 	print("La clasificacion es: ", self.clasificacion)

 crea=int (input("¿Cuantos animales desas crear?"))
 ban = 0;

 while ban < crea:
 	ban=ban+1;
 	noma = input("Dame el nombre del animal %d: " %ban)
 	tipa = input("Dame el tipo del animal %d: " %ban)
 	claa = input("Dame la clasificacion del animal %d: " %ban)

 	ani = animal(noma, tipa,claa)
 	animales.append(ani)

 print("Los animales creados fueron: ")
 for y in animales:
 	y.getNombre()
 	y.getTipo()
 	y.GetClasificacion()

 ID_ani = int(input("Dame un ID para cambiar"))
 print("El animal seleccionado es: ", animales[ID_ani].nombre)
 ntipo = input ("Dame un nuevo tipo: ")
 animales[ID_ani].setTipo(ntipo)
 print ("El nuevo tipo", animales[ID_ani].nombre, "es", animales[ID_ani].tipo)


