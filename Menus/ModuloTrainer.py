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


######################################################################################################################################
####
### OPCION DE INICIO DE SESION SIENDO TRAINER ---------------------------------------------------------------------------------------------


def iniciarSeccionTrainer ():
    abrir = abrirCamperJSON ()

    numIdenT = int(input("Ingrese su número de identificación para iniciar sesión: "))
    for i in range (len(abrir["trainers"])):
            if numIdenT==(abrir["trainers"][i]["ID"]):
                print(f"\nBienvenido, {abrir['trainers'][i]['nombres']} : Jornada del trainer {abrir['trainers'][i]['Jornada del trainer']} ~~~")
                
                guardarCamperJSON(abrir)





####################################################################################################################################
#### MENU DE TRAINER -----------------------------------------------------------------------------

######## OPCION 1 - VER NOTAS DE LOS CURSOS ---------------------------------------------------------------------------------------------------

def VerNotas():
    nota=abrirnotasJSON ()
    print("¿A que Camper quiere ver las notas? ")
    for i in range (len(nota["NotasCamper"])):
     print("Campers # ", i + 1, nota["NotasCamper"][i]["Nombre"])
    num=int(input(": "))
    print(nota ["NotasCamper"][num-1]["Notas"] )



################################################################################################################################

### OPCION 2 NOTAS ASIGNACION :  ---------------------------------------------------------------------------------------------

def NotasPromedio(pro , fil , otro) :
    notaF = (pro*0.6) + (fil*0.3) + (otro*0.1)
    return notaF

def NotasAsig () :
    abrir2 = abrirCamperJSON ()
    abrir = abrirnotasJSON ()
    nombre=input("ingresa el nombre del camper: ")

    for i in range (len(abrir["NotasCamper"])):
        if nombre == (abrir["NotasCamper"][i]["Nombre"]):
            print(f"Notas de: {abrir["NotasCamper"][i]["Nombre"]}")

            proyecto = int(input("Ingrese la nota del proyecto: ~ "))
            abrir ["NotasCamper"][i]["Notas"]["proyecto"] = proyecto

            filtro = int(input("Ingrese la nota del filtro: ~ "))
            abrir ["NotasCamper"][i]["Notas"]["filtro"] = filtro

            otros = int(input("Ingrese la nota de otros: ~ "))
            abrir ["NotasCamper"][i]["Notas"]["otros"] = otros

            notaFinal = NotasPromedio(proyecto, filtro, otros)
            abrir ["NotasCamper"][i]["Notas"]["Nota Final"] = notaFinal

            if notaFinal >= 60 :
                abrir2["campers"][i]["estado del estudiante"]["estado"] = "Aprobado"
                abrir ["NotasCamper"][i]["Notas"]["Riesgo"] = "Bajo"
                if notaFinal == 60 :
                    abrir2["campers"][i]["estado del estudiante"]["estado"] = "cursando"
                    abrir ["NotasCamper"][i]["Notas"]["Riesgo"] = "Medio"
            else:
                abrir2["campers"][i]["estado del estudiante"]["estado"] = "Reprobado"
                abrir ["NotasCamper"][i]["Notas"]["Riesgo"] = "Alto"
                print("Ten cuidado camper estas en rendimiento muy alto estudia o recupera las notas :(")
            guardarnotasJSON (abrir)
            guardarCamperJSON(abrir2)

#### El :. 2f Redondea el número a dos decimales y lo muestra en formato de punto flotante (float).

            print(f"Nota Final del Camper es de {notaFinal:.2f}~~~")
            print(f"La nota de {abrir["NotasCamper"][i]["Nombre"]} ha sido asignada correctamente ~~~")


######## OPCION 3 - ASIGNAR NOTA A CAMPERS -------------------------------------------------------------------------------------------

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



#####################################################################################################################################
######## OPCION 4 - VER RUTAS ASIGNADAS Y SUS CAMPERS ------------------------------------------------------------------------------
    
def VerRutas():
     rutas=abrirCamperJSON()
     for i in rutas["Rutas"]:
           print(i, ":\n\n", "\n".join(rutas["Rutas"][i]))
           print()





    