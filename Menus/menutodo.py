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


##Ver campers en la seccion de coordinador , 

def Vercam ():
      abrir = abrirCamperJSON ()
      for i in range(len(abrir["campers"])):
            print("camper ~~ ", i+1 , "Id: ", abrir["campers"]["identificacion"])
            print("Nombres ~ " , abrir [ "campers"]["nombres"])
            print("Apeliidos ~ " , abrir [ "campers"]["apellidos"])
            print("dirección ~ " , abrir [ "campers"]["direccion"])
            print("telefonos ~ " , abrir [ "campers"]["telefonos"])
            print("acudiente ~ " , abrir [ "campers"]["acudiente"])
            print("Estado : ~ " , abrir [ "campers"]["estado"])
            print("riesgo: ~ " , abrir [ "campers"]["riesgo"])



## Para que ingrese u nuevo camper siendo coordinador

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



## Para cuando desee el camper ingresarse en caso de que no este registrado

def CamperInscripcion(): 
        
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



## editar 

def EditarOpcion (): 
    abrir = abrirCamperJSON()
    Vercam ()
    print("¿ Que estudiante desear editar ?")

    elije = int(input(" ~~~ : "))

    print(" ~~~ Que opcion deseas editar? ~~~")
    print(" 1- Identidad.. ~~ ")
    print("2- Nombres.. ~~ ")
    print("3- Apellidos.. ~~ ")
    print("4- Direccion.. ~~ ")
    print("5- Telefono.. ~~ ")
    print("6- Acudiente.. ~~ ")

    editar = int(input("~~~ : "))

    if editar == 1 :
        print("Cual sera los nuevos nombres ~~")
        nom = input ("~~: ")
        abrir["campers"][editar-1]["nombres"] = nom


    elif editar == 2 :
        print("Cual sera los nuevos apellidos ~~")
        ape = input ("~~: ")
        abrir["campers"][editar-1]["apellidos"] = ape
           

    elif editar == 3 :
        print("Cual sera la nueva dirección ~~")
        dire = input ("~~: ")
        abrir["campers"][editar-1]["direccion"] = dire


    elif editar == 4 :
        print("Cual sera el nuevo telefono ~~")
        tel = input ("~~: ")
        abrir["campers"][editar-1]["telefonos"] = tel


    elif editar == 4 :
        print("Cual sera el nuevo acudiente ~~")
        tel = input ("~~: ")
        abrir["campers"][editar-1]["acudiente"] = tel   

