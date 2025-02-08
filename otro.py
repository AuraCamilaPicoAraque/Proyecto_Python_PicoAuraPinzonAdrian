        opc = int(input(": "))

        if opc == 1 :
            print("")

        elif opc == 2 :
            print("")


def abrirCoordinadorJSON ():
    Abrir = {}
    with open("../bbdd/Coordinador.json" , "r") as openFile :
        Abrir = json.load (openFile)
    return Abrir

def abrirTrainerJSON ():
    Abrir = {}
    with open("../bbdd/trainer.json" , "r") as openFile :
        Abrir = json.load (openFile)
    return Abrir

def abrirNuevoJSON ():
    Abrirlol = {}
    with open("../bbdd/Coordinador.json" , "r") as openFile :
        Abrirlol = json.load (openFile)
    return Abrirlol



def guardarCoordinadorJSON (lool):
    with open ("../bbdd/Coordinador.json" , "w") as outFile :
        json.dump (lool , outFile)

def guardarNuevoJSON (lool):
    with open ("../bbdd/Coordinador.json" , "w") as outFile :
        json.dump (lool , outFile)

def guardarTrainerJSON (lool):
    with open ("../bbdd/Coordinador.json" , "w") as outFile :
        json.dump (lool , outFile)
