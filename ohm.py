#Este programa calcula la ley de ohm
print("ley de ohm")
print("selecciona la opcion")
opcion=int(input("1=voltaje, 2=corriente, 3=resistencia: "))
try:
    if opcion==1:
        resistencia=float(input("ingresa la resistencia en (ohm): "))
        corriente=float(input("ingresa la corriente en (amperios): "))
        voltaje=resistencia*corriente
        print("el voltaje es: ",voltaje,"voltios")
    elif opcion==2:
        voltaje=float(input("ingresa el voltaje en voltios: "))
        resistencia=float(input("ingresa la resistencia en ohm: "))
        corriente=voltaje/resistencia
        print("la corriente es: ",corriente,"amperios")
    elif opcion==3:
        voltaje=float(input("ingresa el voltaje en voltios: "))
        corriente=float(input("ingresa la corriente en (amperios): "))
        resistencia=voltaje/corriente
        print("la resistencia es: ",resistencia,"ohm")
    else:
        print("opcion no valida")
except ValueError:
    print("error: entrada no valida, por favor ingresa un numero")