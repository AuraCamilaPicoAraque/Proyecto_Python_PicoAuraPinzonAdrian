# Python - Proyecto
Se desarrollo el proyecto a partir del 7 de febrero y finalizamos el 12 de este mismo mes , para comprender primero que todo tendremos que saber que nos piden -> [aqui](https://hallowed-slug-719.notion.site/P-P-1-CampusLands-ERP-2e024bf25de9449aba20b1d69c56cfce)  , para mi el proyecto lo dividi en 3 partes el :
* El coordinador = _este tendra el poder de hacer cualquier cosa , seguido del CRUD_
* El Trainer = _este es el profesor que dictara los cursos asignados por el coordinador_
* El camper= _este seremos nosotros los que estamos estudiando en campus , tenemos permisos de ver nuestros cursos y asignaciones previamente .

Y en este proyecto será muy fundamental el tipo de programa de `.json` para nuestra base de datos.
Solamente tendremos que seguir los pasos a seguir para terminar profundamente el proyecto y listo...

## Tabla de contenidos
| Indice | Titulo  |
|--|--|
| 1 |  [Menus](https://github.com/AuraCamilaPicoAraque/Proyecto_Python_PicoAuraPinzonAdrian/tree/master/Menus "Menús")

## Tabla de archivos.

| Indice | Titulo  |
|--|--|
| 1 | [BaseDatosCampus.json](https://github.com/AuraCamilaPicoAraque/Proyecto_Python_PicoAuraPinzonAdrian/blob/master/Menus/BaseDatosCampus.json "BaseDatosCampus.json")
| 2 | [MenuSecundario.py](https://github.com/AuraCamilaPicoAraque/Proyecto_Python_PicoAuraPinzonAdrian/blob/master/Menus/MenuSecundario.py "MenuSecundario.py")
| 3 | [ModuloCamper.py](https://github.com/AuraCamilaPicoAraque/Proyecto_Python_PicoAuraPinzonAdrian/blob/master/Menus/ModuloCamper.py "ModuloCamper.py")
| 4 | [ModuloCoordinador.py](https://github.com/AuraCamilaPicoAraque/Proyecto_Python_PicoAuraPinzonAdrian/blob/master/Menus/ModuloCoordinador.py "ModuloCoordinador.py")
| 5| [ModuloTrainer.py](https://github.com/AuraCamilaPicoAraque/Proyecto_Python_PicoAuraPinzonAdrian/blob/master/Menus/ModuloTrainer.py "ModuloTrainer.py")
| 6| [grupos.json](https://github.com/AuraCamilaPicoAraque/Proyecto_Python_PicoAuraPinzonAdrian/blob/master/Menus/grupos.json "grupos.json")|
| 7| [menuPrincipal.py](https://github.com/AuraCamilaPicoAraque/Proyecto_Python_PicoAuraPinzonAdrian/blob/master/Menus/menuPrincipal.py "menuPrincipal.py")|
| 8| [notas.json](https://github.com/AuraCamilaPicoAraque/Proyecto_Python_PicoAuraPinzonAdrian/blob/master/Menus/notas.json "notas.json")|

### Instalaciones 

Deberás ejecutar este comando para descargar el repositorio:

```bash
git clone <repositorio>

```


## Y para poder ejecutarlo en el visual studio se debe colocar :

```bash
python3 <nombre>.py
```




## Errores

Si da la casualidad de que estas en windows y no te deja ejecutar los archivos .py  puede ser porque no tienes instalado el python.org 




## Descripción de los archivos...

| Índice | Explicación  |
|--|--|
| 1 | Archivo JSON que almacena la base de datos principal del sistema, incluyendo información sobre campers, trainers, coordinadores y otros datos relevantes.  |
| 2 | Script en Python que gestiona un menú secundario dentro del sistema, permitiendo la navegación entre diferentes módulos y funciones.  |
| 3 |  Módulo en Python que maneja la gestión de campers, incluyendo su registro, consulta y actualización de información académica.   |
| 4 | Módulo en Python que gestiona las funciones de los coordinadores, permitiendo la administración de rutas de entrenamiento, asignación de trainers y monitoreo del desempeño de los campers.   |
| 5 | Módulo en Python que maneja las funciones de los trainers, incluyendo la evaluación de campers, asignación de notas y seguimiento del progreso académico.  |
| 6 |Archivo JSON que almacena la información de los grupos dentro del sistema, incluyendo su estructura, asignaciones de campers y trainers.  |
| 7 | Script en Python que gestiona el menú principal del sistema, permitiendo el acceso a las diferentes funciones y módulos de la plataforma. |
| 8 |Archivo JSON que almacena las notas y evaluaciones de los campers, permitiendo un seguimiento de su rendimiento académico. |

## Explicación github.

Para poder subir a la nube este repositorio:

`Terminal :  Ctrl + Alt + T `

* 1-  Debemos iniciar con el  ` git init `  = ¿Porque? __ pues iniciamos un git vaco para que podamos subirlo al local.

* 2- Partiendo de ahí pondremos nuestros datos para subir a la nube   ` git config --global user.email "(gmail)"` para colocar nuestro gmail vinculado al github y seguido también nuestro nombre  ` git config --global user.name "(nombre)"`

* 3- Ingresado nuestro gmail y nombre proseguimos a poner nuestro repositorio que seria de la siguiente manera : ` git remote add origin (link del repositorio)`

* Un ejemplo seria: ` git remote add origin https://github.com/AuraCamilaPicoAraque/Python_S1_PicoAura`
* listo ahora tenemos que confirmar si tenemos nuestros archivos en la carpeta ..   ` git status `
* teniendo esos archivos los agregaremos con  ` git add . `
* Y le ponemos  ` git commit -m "(descripcion que quieras)" `  esto para tener un registro de el proceso que llevamos con los commits
* Ahora si todo va bien tendrías que mandarlo a la nube estando en  local , lo haremos de la siguiente manera :    ` git push origin master `
* Ahora saldrá un menú para que pongas tu usuario de nombre de github ... tendrás que ponerlo 
* Y ahora viene una parte fundamental ... te va a salir otro menú que te dirá que pongas tu contraseña esa sera la que tendrás en github.
* Para sacarla tendrías que meterte  [aqui~](https://github.com/settings/apps) y darle en  ` personal access tokens `  al terminar de darle click le das a `tokens(classic)` 
* Ahora estará vació , aquí le tienes que dar en `generate new token` y le tienes que dar en `Generate new token (classic)`.
* Y listo le pones las opciones que quieres la mas recomendada es `repo`  y ahí te sale un código el cual copias y pegas en lo que te pide en la termina.
* Listo ahora ya estaría subido al repositorio , debes actualizar la pestaña para que te salga

ÉXITOSSSSSSSSSS...


## Repositorio...

Este repositorio fue hecho y desarrollado por [ AuraCamilaPicoAraque ](https://github.com/AuraCamilaPicoAraque)
