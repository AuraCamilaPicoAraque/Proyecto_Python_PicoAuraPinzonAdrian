import json

##  Abrir
def abrirCamperJSON():
    Abrir = {}
    with open("./BaseDatosCampus.json" , "r") as openFile :
        Abrir = json.load (openFile)
    return Abrir


def abrirnotasJSON():
    Abrir = {}
    with open("./notas.json" , "r") as openFile :
        Abrir = json.load (openFile)
    return Abrir

def abrirgruposJSON():
    Abrir = {}
    with open("./grupos.json" , "r") as openFile :
        Abrir = json.load (openFile)
    return Abrir


## Guardar

def guardarCamperJSON(lool):
    with open ("./BaseDatosCampus.json" , "w") as outFile :
        json.dump (lool , outFile, indent=4 , ensure_ascii=False)

def guardarnotasJSON(lool):
    with open ("./notas.json" , "w") as outFile :
        json.dump (lool , outFile, indent=4 , ensure_ascii=False)

def guardargruposJSON(lool):
    with open ("./grupos.json" , "w") as outFile :
        json.dump (lool , outFile, indent=4 , ensure_ascii=False)









#### MENU DE TRAINER -----------------------------------------------------------------------------

def VerCursoActual(identificacion):
      abrir = abrirCamperJSON ()
      for camper in abrir ["campers"]:
            if camper ["identificacion"] == identificacion :
                        print(f"curso actual: {camper['ruta_asignada']}")
                        
## [F]  hace más sencillo introducir variables y expresiones en las cadenas


#### TRAINERS 

######## OPCION 1 - MENUTRAINER

def VerNotas():
    nota=abrirnotasJSON ()
    print("¿A que Camper quiere ver las notas? ")
    for i in range (len(nota["NotasCamper"])):
     print("Campers # ", i + 1, nota["NotasCamper"][i]["Nombre"])
    num=int(input(": "))
    print(nota ["NotasCamper"][num-1]["Notas"] )




######## OPCION 2 - MENUTRAINER -------------------------------------------------------------------------------------------

def EditarNota():
    nota=abrirnotasJSON ()
    print("A Que Camper Le Quiere Editar La Nota?")

    for i in range (len(nota["NotasCamper"])):
        print(f"Campers # {i + 1}: {nota['NotasCamper'][i]['Nombre']} - Nota: {nota['NotasCamper'][i]['Notas']}")


    Opcion= int(input("Ingresa el numero del Camper Que quiere modificar la nota: "))
    
    if 0 < Opcion and Opcion < len(nota["NotasCamper"]): #Explicacion del metodo: Basicamente dice que si la opcion de la lista de estudiante es menos 0 y lee todos los estudiantes 
                nuevaNotaProyecto = int(input("Ingresa una nueva nota del proyecto: "))
                nota["NotasCamper"][Opcion-1]["Notas"]["proyecto"] = nuevaNotaProyecto
                nuevaNotaFiltro = int(input("Ingresa una nueva nota del Filtro: "))
                nota["NotasCamper"][Opcion-1]["Notas"]["filtro"] = nuevaNotaFiltro
                otros = int(input("Ingresa otra nota: "))
                nota["NotasCamper"][Opcion-1]["Notas"]["otros"] = otros
                print(f"La nota de {nota['NotasCamper'][Opcion-1]['Nombre']}Ha sido actualizada correctamente~~")
                guardarnotasJSON(nota)
    else:
                print("La opcion es invalida ~~")




######## OPCION 3 - MENUTRAINER
    
def VerRutas():
     rutas=abrirCamperJSON()
     for i in rutas["Rutas"]:
           print(i, ":\n\n", "\n".join(rutas["Rutas"][i]))
           print()



###############################################################################################




## Para que ingrese un nuevo camper siendo coordinador

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

##########################################################################################################

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
                                                "estado" : "en proceso de Incripcion",
                                               "riesgo" : "Bajo"
                                               }
                                               })
                
                guardarCamperJSON(abrir)

############################################################################################################################

## EDITAR CAMPERS -------------------------------------------------------------------------------



def EditarCamper (): 
    abrir = abrirCamperJSON()
    Vercam ()
    print("¿ Que estudiante desear editar ?")

    elije = int(input(" ~~~ : "))

    print(" ~~~ Que opcion deseas editar? ~~~")

    print("1- Nombres.. ~~ ")
    print("2- Apellidos.. ~~ ")
    print("3- Direccion.. ~~ ")
    print("4- Telefono.. ~~ ")
    print("5- Acudiente.. ~~ ")

    editar = int(input("~~~ : "))

    if editar == 1 :
        print("Cual sera los nuevos nombres ~~")
        nom = input ("~~: ")
        abrir["campers"][elije-1]["nombres"] = nom


    elif editar == 2 :
        print("Cual sera los nuevos apellidos ~~")
        ape = input ("~~: ")
        abrir["campers"][elije-1]["apellidos"] = ape
           

    elif editar == 3 :
        print("Cual sera la nueva dirección ~~")
        dire = input ("~~: ")
        abrir["campers"][elije-1]["direccion"] = dire


    elif editar == 4 :
        print("Cual sera el nuevo telefono ~~")
        tel = int(input ("~~: "))
        abrir["campers"][elije-1]["telefonos"] = tel


    elif editar == 5 :
        print("Cual sera el nuevo acudiente ~~")
        acu = input ("~~: ")
        abrir["campers"][elije-1]["acudiente"] = acu   
        
    guardarCamperJSON(abrir)
    

    
### EDITAR TRAINERS --------------------------------------------------------------------------------------------------



def EditarTrainer ():
    abrir = abrirCamperJSON()
    VerTrainer()
    print ("¿A que trainer desea editar ? ")

    elijeTr = int(input("~~~ : "))
    print(" ~~~ Que opcion deseas editar? ~~~")

    print("1- Nombres.. ~~ ")   
    print("2- Jornada del trainer ")   

    opc = int(input("~~~~ :"))

    if opc == 1 :
        print (" Cual sera el nuevo nombre del trainer?")
        nomtrai = input("~~~ :")
        abrir["trainers"][elijeTr - 1]["nombres"] = nomtrai

    elif opc == 2 :
        print("Cual jornada de trabajo le quieres cambiar ")
        print ("""Mañana : 1
Tarde: 2
Jornada Completa: 3 """)
        jorTra = int(input("~~~~ : "))
        abrir["trainers"][elijeTr - 1]["Jornada del trainer"] = jorTra
    
    guardarCamperJSON
         

         

## coordinador opcion 7


 #def agregarRut():
   # abrir= abrirgruposJSON()
  #  for i in range (len(abrir["P1","P"])):
        

















####################################################################################################

## OPCION 2 [COORDINADOR] AGREGAR NUEVO TRAINER 


def NuevoTrainer () :
      
        abrir = abrirCamperJSON()
        nuevaidentrai = abrir ["trainers"][-1] ["ID"]+1
        NuevoTra = abrir ["trainers"]
        print("Ingrese el nombre del trainer ")
        nt = input("~~~: ")
        print("Ingrese la jornada del nuevo trainer")
        print ("""Mañana : 1
Tarde: 2
Jornada Completa: 3 """)
        opc = input ("~~~ : ")
        abrir["trainers"].append ({  "ID" : nuevaidentrai ,
                                     "nombres" : nt ,
                                     "Ruta" : "",
                                     "Jornada del trainer" : opc
                                     })
        guardarCamperJSON(abrir)
        



              
              
##################################################################################################

### OPCION 1 [COORDINADOR]  VER TRAINER

def VerTrainer():
      abrir = abrirCamperJSON ()
      for i in range(len(abrir["trainers"])):
            print("Trainer   ~~ ", " Id: ", abrir["trainers"][i]["ID"])
            print("Nombres   ~~ " , abrir[ "trainers"][i]["nombres"])
            print("Ruta ~~ " , abrir["trainers"][i]["Ruta"])
            print("Jornada del trainer ~~ " , abrir["trainers"][i]["Jornada del trainer"])
            print()
            print()





##   OPCION 1 [COORDINADOR]  VER CAMPERS  
abrir={}
def Vercam ():
    abrir = abrirCamperJSON ()
    for i in range(len(abrir["campers"])):
        print("camper    ~~ ", "Id: ", abrir["campers"][i]["identificacion"])
        print("Nombres   ~~ " , abrir [ "campers"][i]["nombres"])
        print("Apeliidos ~~ " , abrir [ "campers"][i]["apellidos"])
        print("dirección ~~ " , abrir [ "campers"][i]["direccion"])
        print("telefonos ~~ " , abrir [ "campers"][i]["telefonos"])
        print("acudiente ~~ " , abrir [ "campers"][i]["acudiente"])
        print("Estado :  ~~ " , abrir [ "campers"][i]["estado del estudiante"]["estado"])
        print("riesgo:   ~~ " , abrir [ "campers"][i]["estado del estudiante"]["riesgo"])
        print()
        print()

    guardarCamperJSON(abrir)






##################################################################################

### OPCION DE INICIO DE SESION SIENDO CAMPER --


def iniciarSeccion ():
    abrir = abrirCamperJSON ()

    numIdent = input("Ingrese su número de identificación para iniciar sesión: ")
    for i in range (len(abrir["campers"])):
            if numIdent==(abrir["campers"][i]["identificacion"]):
                print(f"\nBienvenido, {abrir['campers'][i]['nombres']} {abrir['campers'][i]['apellidos']} ~~~~")
                
                guardarCamperJSON(abrir)





### OPCION DE INICIO DE SESION SIENDO TRAINER --


def iniciarSeccionTrainer ():
    abrir = abrirCamperJSON ()

    numIdenT = input("Ingrese su número de identificación para iniciar sesión: ")
    for i in range (len(abrir["trainers"])):
            if numIdenT==(abrir["trainers"][i]["ID"]):
                print(f"\nBienvenido, {abrir['trainers'][i]['nombres']} {abrir['trainers'][i]['Jornada del trainer']} ~~~")
                
                guardarCamperJSON(abrir)





#### ELIMINAR CAMPER Y TRAINERS --------------------------------------------------------------------------------


#### OPCION 4 [COORDINADOR]  ELIMINAR CAMPER ---



def EliminarCamper():
    abrir=abrirCamperJSON()
    for i in range (len(abrir["Campers"])):
        print("Campers # ", i + 1, abrir["NotasCamper"][i]["Nombre"])
    eliminarCamper= int(input("¿Que Camper Quieres eliminar?: " ))
    for i in range (len(abrir["campers"])):
        if abrir["campers"][i]["identificacion"]==eliminarCamper:
            del(abrir["campers"][i])
            guardarCamperJSON(abrir)




#### OPCION 4 [COORDINADOR]  ELIMINAR TRAINER ---


def EliminarTrainer():
    abrir=abrirCamperJSON ()
    for i in range (len(abrir["trainers"])):
          print("Trainers #", i+1, abrir["trainers"][i]["nombres"])
    eliminarTrainer= int(input("Que trainer quieres elminar"))
    for i in range (len(abrir["trainers"])):
        if abrir["trainers"][i]["ID"]==eliminarTrainer:
            del(abrir["trainers"][i])
    guardarCamperJSON(abrir)


                    