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
    


#################################################################################################################################################

##########################################################################################################


### OPCION DE INICIO DE SESION SIENDO CAMPER --------------------------------------------------------------------------------------------------


def iniciarSeccion ():
    abrir = abrirCamperJSON ()

    numIdent = input("Ingrese su número de identificación para iniciar sesión: ")
    for i in range (len(abrir["campers"])):
            if numIdent==(abrir["campers"][i]["identificacion"]):
                print(f"\nBienvenido, {abrir['campers'][i]['nombres']} {abrir['campers'][i]['apellidos']} ~~~~")
                guardarCamperJSON(abrir)
                return numIdent
            

####################################################################################################################################
## MENU DE CAMPER -----------------------------------------------------------------------------------------------------------------
### OPCION DE INICIO DE SESION SIENDO CAMPER ----------------------------------------------------------------------------------------------


def iniciarSeccion ():
    abrir = abrirCamperJSON ()

    numIdent = input("Ingrese su número de identificación para iniciar sesión: ")
    for i in range (len(abrir["campers"])):
            if numIdent==(abrir["campers"][i]["identificacion"]):
                print(f"\nBienvenido, {abrir['campers'][i]['nombres']} {abrir['campers'][i]['apellidos']} ~~~~")
                guardarCamperJSON(abrir)
                return numIdent


####################################################################################################################################
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

                print("Ingrese la ruta de estudio   |  Manana = 1   |   Tarde = 2   | ")
                Ruta = int(input("~~~: "))

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
                                               },
                                               "jornada" : Ruta ,
                                               "Ruta" : ""
                                               })
                
                guardarCamperJSON(abrir)


#########################################################################################################################################
##### OPCIONES -----------------------------------------------------------------------------------------------------------------------------------
##### OPCION 1 - VER INFORMACION DEL CURSO EN EL QUE ESTOY ----------------------------------------------------------------------------------------

def VerInfoCurso (identificacion) :
    abrir = abrirCamperJSON ()
    for Ruta in abrir ["Rutas"]:
        for camper in abrir ["campers"]:
            for i in camper["Rutas"]:
                print(i, ":\n\n", "\n".join(camper["Rutas"][i]))
                if camper ["identificacion"] == identificacion and Ruta == camper["Ruta"]:
                    print(f"Rutas del camper :{abrir['Rutas'][Ruta]}")



##### OPCION 2 - VER RUTA ASIGNADA ------------------------------------------------------------------------------------------------------------------

def VerCursoActual(identificacion):
      abrir = abrirCamperJSON ()
      for camper in abrir ["campers"]:
            if camper ["identificacion"] == identificacion :
                        print(f"curso actual: {camper['Ruta']}")



##### OPCION 3 - VER NOTAS ------------------------------------------------------------------------------------------------------------------



def VerNotas(identificacion):
    campers = abrirCamperJSON()
    abrir = abrirnotasJSON()
    
    for camper in campers["campers"]:
        if camper["identificacion"] == identificacion:
            nombre = camper["nombres"]
            for nota in abrir["NotasCamper"]:
                if nota["Nombre"] == nombre:
                    print(f"Tus notas {nombre} son las siguientes :\n {nota["Notas"]}")
                    return
    
    print("No se encontraron notas para esta identificación.")


