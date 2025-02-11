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
    

### menu para el trainer : -------------------------------------------------------------------------
    if opcion == "1":
        MenuTrainer()

## menu de opciones para el trainer
        opcTr = int(input("~~~ : "))

        if  opcTr == 1:
            VerNotas()
        elif opcTr == 2:
            EditarNota()
        elif opcTr == 3 :
            VerRutas ()
        elif opcTr == 4 :
            print("")
            
            
        else:
             print("Opcion no valida")
                    




### menu para el camper: ---------------------------------------------------------------------------------------------------------              

    elif opcion == "2":
        MenuCamper()

        ## menu de opciones para el camper
        opcCamper = int(input(" ~~~ :"))


### OPCION SI ESTA INSCRITO ------------------------------
        if opcCamper == 1 :
            iniciarSeccion ()

            opcC = int(input("~~ : "))
            if opcC == 1 :
                VerCursoActual ()
            
#### OPCION SI NO ESTA INSCRITO -----------------------------

        elif opcCamper == 2 :
            CamperInscripcion()
        
#### OPCION 3 -----------------

        elif opcCamper == 3 :
            print("")







## menu para el coordinador: --------------------------------------------------------------------------------------------------------------

    elif opcion == "3":
        MenuCoordinador()
        ## menu de opciones para el trainer
        opc = int(input(" ~~~ :"))

### OPCION 1 --- VER CAMPERS: Y TRAINER ----------------------------------

        if opc == 1 :
            print("1- Ver Campers")
            print("2- Ver Trainer")
            opcV = int(input("~~ :"))
            if opcV == 1 :
                Vercam ()
            elif opcV == 2 :
                VerTrainer ()

### OPCION 2 --- AGREGAR CAMPERS Y CAMPER ----------------------------------

        elif opc == 2 :
            print("1- agregar nuevo Campers")
            print("2- agregar nuevo Trainer")
            opcA = int(input("~~ :"))
            if opcA == 1 :
                IngresarCamper()
            elif opcA == 2 :
                NuevoTrainer ()

### OPCION 3 --- EDITAR CAMPERS: ----------------------------------

        elif opc == 3 :
            print("1- Editar Campers")
            print("2- Editar Trainer")
            opcE = int(input("~~ :"))
            if opcE == 1 :
                EditarCamper ()
            elif opcE == 2 :
                NuevoTrainer ()
        
### OPCION 4 --- ELIMINAR CAMPERS: ----------------------------------

        elif opc == 4 :
            print("1- Eliminar Campers")
            print("2- Eliminar Trainer")
            opcEl = int(input("~~ :"))
            if opcEl == 1 :
                EliminarCamper()
            elif opcEl == 2 :
                EliminarTrainer()
        

### OPCION 5 --- ASIGNAR RUTA A CAMPERS: ----------------------------------

        elif opc == 5 :
            print ("ruta")
        

### OPCION 6 --- AGREGAR CAMPERS A RUTA DISPONIBLE : ----------------------------------

        elif opc == 6 :
            print ("agregar")
        

### OPCION 7 --- AGREGAR NUEVA RUTA  : ----------------------------------

        elif opc == 7 : 
            print("ruta nueva")
        


### OPCION 8 --- SALIR : ----------------------------------

        elif opc == 8 : 
            print("Saliendo del programa ~~~ ")
            r = False
            return r

            





## PARA SALIR DEL MENU PRINCIPAL  ---------------------------------------------------------------------------
    elif opcion == "4":
        print(" Saliendo del sistema ~~~")
        exit ()



# opcion no valida ------------


    else:
        print(" opción no válida, intente de nuevo.")
        
bo=True
while bo==True:
    bo=MenuDelPrincipio()




    

