#Diccionario no se escribe en pluarl
estudiante = {
	'nombre': 'Leidy',
	'edad': 30,
	'esVoleibolista': True
}
#imprimir/ accedder a todas las llaves 
#atributos de mi diccionario

print(estudiante)
#necesito acceder a un ATRIBUTO O LLAVE DEL DICCIONARIO
print(estudiante['nombre'])
print(estudiante.get('edad'))

#recorrer un diccionario
#y obetner sus valores
for valor in estudiante.values():
	print(valor)

