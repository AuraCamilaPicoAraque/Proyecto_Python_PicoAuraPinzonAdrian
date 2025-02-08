import json

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


def MenuTrainer():
        print ("#####################################")
        print("##¿Que quieres hacer como Trainer ? ###")
        print ("#####################################")
        print("1- Ver grupo")
        print("2- Asignar notas")
    
def MenuCamper():
        print ("#####################################")
        print("##¿Que quieres hacer como Camper ? ##")
        print ("#####################################")
        print("1- ver Notas")
        print("2- ver cursos")

def MenuCoordinador():
        print ("#####################################")
        print("##¿Que quieres hacer como Coordinador ? ##")
        print ("##########################################")
        print("1- Ver grupos")
        print("2- Ingresar nuevo camper")
        print("3- Ingresar nuevo trainer")
        opc = int(input(": "))
        if opc == 2 :
                IngresarCamper()





def IngresarCamper(): 
        
                abrir = abrirCamperJSON()

                nuevaidentificacion = abrir ["campers"][-1] ["identificacion"]+1
                print("Ingrese el nombre del camper")
                nombre = input("~~~: ")

                print("Ingrese el apellido del camper")
                apellido = input("~~~: ")

                print("Ingrese la direccion del camper")
                direccion = input("~~~: ")
                
                print("Ingrese el numero del camper")
                telefonoCamper = int(input ("~~~: "))

                print("Ingrese el nombre del acudiente del camper")
                nombreAcu = input("~~~: ")

                abrir["campers"].append ({     "identificacion" : nuevaidentificacion ,
                                               "nombres": nombre ,
                                               "apellidos": apellido ,
                                               "direccion": direccion ,
                                               "telefonos": telefonoCamper ,
                                               "acudiente": nombreAcu ,
                                             "estado del estudiante": 
                                             {
                                                "estado" : "Inscrito",
                                               "riesgo" : "Bajo"
                                               }
                                               })
                
                guardarCamperJSON(abrir)
                                               
                
                
                
                