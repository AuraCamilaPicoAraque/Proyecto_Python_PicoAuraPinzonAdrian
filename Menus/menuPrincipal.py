import json
from MenuSecundario import *
from menutodo import *

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
    print("\n ----- Bienvenidos al CampusLand -------- \n")
    print ("##########################################")
    print("¿Quien eres?")
    print("1- Trainer")
    print("2- Campers")
    print("3- Coordinador ")
    print("4- Salir del sistema")

    opcion = input("Seleccione una opción: ")
    

### menu para el trainer
    if opcion == "1":
        MenuTrainer()

        opcTr = int(input("~~~ : "))

        if  opcTr == 1:
            VerNotas()
        elif opcTr == 2:
            EditarNota()
        elif opcTr == 3 :
            Vercam ()
        elif opcTr == 4 :
            print("")
            
            
        else:
             print("Opcion no valida")
                    




### menu para el camper
    elif opcion == "2":
        MenuCamper()

        opcCamper = int(input(" ~~~ :"))

        if opcCamper == 1 :
            print("a")
            
        elif opcCamper == 2 :
            CamperInscripcion()




## menu para el coordinador

    elif opcion == "3":
        MenuCoordinador()
        opc = int(input(" ~~~ :"))

        if opc == 1 :
            Vercam ()
        elif opc == 2 :
            IngresarCamper()
        elif opc == 3 :
            NuevoTrainer ()





    elif opcion == "4":
        print(" Saliendo del sistema ~~~")
        exit ()
    else:
        print(" opción no válida, intente de nuevo.")
        
bo=True
while bo==True:
    MenuDelPrincipio()




    

