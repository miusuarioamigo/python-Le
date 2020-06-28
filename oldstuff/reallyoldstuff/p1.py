print "Hola, mi nombre es P1"
nombre = raw_input ("Cual es tu nombre:")
print "Un placer conocerte" + nombre
Ayuda = raw_input ("Dime en que puedo ayudarte"+ nombre)
print "Puedo ayudarte a buscar la tabla de multiplicar de varios numeros"
numero = int(raw_input("Dame el numero de la tabla de multiplicar: ")) 
for x in range(1,10): 
	print (str(x)+ " * "+str(numero)+" = "+str((numero*x)))
AyudaB = raw_input ("Puedo ayudarte en algo mas"+ nombre)
print "si, si puedo hacer eso"

print "..."

N1 = raw_input("Dame el valor uno")
N2 = raw_input("Dame el valor dos")

if N1 > N2:
	print str(N1)+ " es mayor que "+ str(N2)
else:
    print str(N2)+ " es mayor que "+ str(N1)

print "P1, NO HA SIDO TERMINADO CORRECTAMENTE"    	