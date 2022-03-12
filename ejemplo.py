numeros=[]

for i in range(0,5,1):
	numero = int (input("Ingrese un numero: "))
	numeros.append(numero)
	
print(numeros)

for k in numeros:
	numeroingresado = int(input("ingrese un numero: "))
	if(numero == numeroingresado):
		print("Numero encontrado")
	else:
		print("Numero no esta")
