#creando tuplas en python
estudiantes = ('Leidy','Natalia')
print(estudiantes)

#estudiantes.append('marta') Error no se puede

#print(estudiantes)

#recorrer una tupla es lo mismo que una lista
for estudiante in estudiantes:
	print(estudiante)

#convertir una tupla en lista
listaEstudiantes = list(estudiantes)
print(listaEstudiantes)
listaEstudiantes.append("nuevo")
newTupla = tuple(listaEstudiantes)
print(newTupla)