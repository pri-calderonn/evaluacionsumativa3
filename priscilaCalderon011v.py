import os
import time
import random
print("Bienvenido a CatPremium")
cantidad=[]
cantidad=()

nombre=input("Ingrese su nombre y apellido")
direccion=input("ingrese su direccion")
comuna=int(input("Ingrese su comuna 1. San bernardo 2. Calera de tango 3. Buin"))
try:
    if  comuna==1:
        print()
    elif  comuna==2:
        print()
    elif  comuna==3:
        print()
except ValueError:
    print("Ingrese una opcion valida")
print("De cuantos kg va a querer el/los sacos  ,escoja una opcion")
saco=int(input("1.Saco de 5kg   2. Saco de 10 kg    3. Saco de 20kg")) 
try:
    if saco ==1:
        cantidad=int(input("Cuantos sacos va a llevar: "))
        cantidad=+1
    
    elif saco ==2:
        cantidad=int(input("Cuantos sacos va a llevar: "))
        cantidad=+1
    elif saco ==3:
        cantidad=int(input("Cuantos sacos va a llevar: "))
        cantidad=+1
except ValueError:
    print("Ingrese una opcion valida")
    
print (f"nombre: {nombre}")
print (f"direccion: {direccion}")
print (f"comuna: {comuna}")
print (f"saco de 5kg: {cantidad}")
print (f"saco de 10kg: {cantidad}")
print (f"saco de 20kg: {cantidad}")

def registrar_pedidos(pedidos):
    nombre=input("Ingrese su nombre y apellido: ")
    direccion=(input("Ingrese su direccion"))
    sector=input("Ingrese comuna :  (san bernardo,calera de tango , buin)")
    kilos=int(input("saco de cuantos kg : 5kg , 10 kg, 20"))
    if kilos =='5kg':
        cantidad=int(input("cuantos sacos quiere?"))
        cantidad=+1
    elif kilos=='10kg':
        cantidad=int(input("cuantos sacos quiere?"))
        cantidad=+1
    elif kilos =='20kg':
        cantidad=int(input("cuantos sacos quiere?"))
        cantidad=+1
        
    pedidos.append ({'nombre y apellido' : nombre , 'direccion' : direccion , 'sector' : sector , 'kilos' : kilos}  )
    
def listar_pedidos(pedidos):
    print ("lista de pedidos")
    for pedido in pedidos:
        print(pedidos)
    

def hoja_rutas (pedidos):
    comuna=input("Ingrese el sector para imprimir la hoja de rutas ")
def salir (pedidos):
    salir    

while True:
        
        print("1. Registrar pedido")
        print("2. Lista de los pedidos")
        print("3.Imprimir hoja de ruta")
        print("4. Salir del programa")
        pedido=int(input("Elija una opcion"))
        try:
    
            if pedido==1:
                print(f"Registrar pedidos {registrar_pedidos}")
            elif pedido == 2:
                print(f"La lista de pedidos es: {listar_pedidos}")
            elif pedido == 3 :
                print(f"Hoja de rutas {hoja_rutas}")
            elif pedido ==4:
                print("Hasta luego,gracias por venir")
                
        except ValueError:
            print ("Debe ingresar una opcion valida")