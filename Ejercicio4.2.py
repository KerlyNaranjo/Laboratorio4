#Ingresar una frase y contar el número de palabras

def contar():
	print (len(frase.split(' ')))

def creartxt():
	archivo = open('Frases.txt','w')
	archivo.close()

def grabartxt():
	archivo = open('Frases.txt','w')
	frase = archivo.write(input('Ingrese una frase: '))
	archivo.close()

creartxt()
grabartxt()

def leertxt():
	archivo = open('Frases.txt','r')
	linea = archivo.readline()
	while linea!="":
		print (linea)
		print (len(linea.split(' ')))
		linea=archivo.readline()
	archivo.close()

leertxt()