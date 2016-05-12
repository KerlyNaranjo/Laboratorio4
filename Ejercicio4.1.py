#Ingresar una frase y contar el número de palabras

#frase = str(input('Ingrese una frase: '))

def contar():
	return len(frase.split(' '))

def creartxt():
	archivo = open('Frases.txt','w')
	archivo.close()

def escribirtxt():
	archivo = open('Frases.txt','w')
	#frase = archivo.write((input('Ingrese las frases que desee: '))
	frase = archivo.write(str(input('Ingrese una frase: ')))
	#archivo.write(len(frase.split(' ')))
	archivo.close()
	print (len(frase.split(' ')))

creartxt()
escribirtxt()