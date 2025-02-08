import json
from MenuSecundario import *

##  Abrir
def abrirCamperJSON():
    Abrir = {}
    with open("./BaseDatosCampus.json" , "r") as openFile :
        Abrir = json.load (openFile)
    return Abrir
    
## Guardar

def guardarCamperJSON(lool):
    with open ("./BaseDatosCampus.json" , "w") as outFile :
       json.dump (lool , outFile, indent=4 , ensure_ascii=False)

def MenuDelPrincipio():
    print ("##########################################")
    print("\n ----- Bienvenidos al CampusLand --------")
    print ("##########################################")
    print("¿Quien eres?")
    print("1- Trainer")
    print("2- Campers")
    print("3- Coordinador ")

    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        MenuTrainer()
    elif opcion == "2":
        MenuCamper()
    elif opcion == "3":
        MenuCoordinador()
    elif opcion == "4":
        print(" Saliendo del sistema ~~~")
        bo=False
    else:
        print(" opción no válida, intente de nuevo.")

abrir = {}

bo=True
while bo==True:
    MenuDelPrincipio()


    

