
edad_cliente = 51
nombre_cliente = "Juan"

print ("Buenos días señor {} su edad es {}"
       .format(str(edad_cliente), nombre_cliente))

if edad_cliente >= 18:
    print("Usted es mayor de edad")
    if edad_cliente <= 35:
        print("Por favor pase a la gerencia que tiene aprobado un crédito de apoyo juvenil inmediato")
    elif edad_cliente <= 50:
        print("Por favor pase a la gerencia que tiene aprobado un crédito de apoyo al empresario")   
    else:
        print("Por favor pase a la gerencia que tiene aprobado un crédito de apoyo al adulto mayor")               
else:
    print("Usted es menor de edad")
    
for i in range(1,edad_cliente + 1):
    residuo = i % 2
    if residuo == 0:
        print(i)


respuesta = "si"


while respuesta == "si":  
    print("Quiere seguir")
    respuesta = input()  
    if respuesta == "si":
        print("Seguimos")
    elif respuesta == "no":
        print("Paramos")
    else:
        print("No entiendo por lo tanto paro")





