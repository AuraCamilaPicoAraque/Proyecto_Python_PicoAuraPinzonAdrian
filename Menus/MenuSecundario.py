from menuPrincipal import *


def MenuTrainer ():
        print ("#####################################")
        print("##¿Que quieres hacer como Trainer ? ###")
        print ("#####################################")
        print("1- Ver grupo")
        print("2- Asignar notas")
    
def MenuCamper ():
        print ("#####################################")
        print("##¿Que quieres hacer como Camper ? ##")
        print ("#####################################")
        print("1- ver Notas")
        print("2- ver cursos")


def MenuCoordinador ():
        print ("#####################################")
        print("##¿Que quieres hacer como Coordinador ? ##")
        print ("##########################################")
        print("1- Ver grupos")
        print("2- Ingresar nuevo camper")
        print("3- Ingresar nuevo trainer")




opc = input(": ")
if opc == 1 :
                print("a")
elif opc == 2 : 
        
                abrir = abrirCamperJSON()

                nuevaidentificacion = abrir ["campers"][-1] ["identificacion"]+1
                print("Ingrese el nombre del camper")
                nombre = input("~~~: ")

                print("Ingrese el apellido del camper")
                apellido = input("~~~: ")

                print("Ingrese la direccion del camper")
                direccion = input("~~~: ")
                
                print("Ingrese el numero del camper")
                telefonoCamper = input ("~~~: ")

                print("Ingrese el nombre del acudiente del camper")
                nombreAcu = input("~~~: ")

                print("Ingrese el numero del acudiente del camper")
                telefonoAcu = input("~~~: ")
                
                
                
                