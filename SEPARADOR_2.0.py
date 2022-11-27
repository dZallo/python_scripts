"""

PNM 08/08/2022
Este script tiene el cometido de copiar un directorio, que puede tener varios niveles de subdirectorios, hacer una copia
con la misma jerarquía, pero sólo manteniendo los archivos de la extensión que le hayamos indicado

"""

import os
import shutil

#--------------------------------------------------------------------------------------------------------------------------
def list_paths(route):              #lista las rutas de todos los archivos de un directorio en str

    list_archivos_r = []
    list_archivos = os.listdir(route)

    for dir in list_archivos:
        list_archivos_r.append(os.path.join(route, dir))  #lista de las rutas de todos los archivos de la subcarpeta
    return list_archivos_r, list_archivos
#--------------------------------------------------------------------------------------------------------------------------
def subdir_eval(list_archivos_r,extensiones):   #devuelve listas de las rutas de los subdirectorios y los archivos a copiar para cada directorio

    dir_list = []
    copy_list = []

    if list_archivos_r == []:
        pass
    else:
        for route in list_archivos_r:
            if os.path.isdir(route) == True:
                dir_list.append(route)  # Se gaurdan las rutas de los subdirectorios de nivel
            else:
                for end in extensiones:
                    if route.endswith(end) == True:
                        copy_list.append(route)   #Se guardan las rutas de los archivos que no se ignoran

    return (dir_list,copy_list)
#--------------------------------------------------------------------------------------------------------------------------


src = input('Introduce la ruta de la carpeta que quieres copiar:')
dest = input('Introduce la ruta del destido de la carpeta copiada:')
dir_name = input('Introduce el nombre que quieres poner a la carpeta: ')

dest= [os.path.join(dest,dir_name)]             #transformo dest en una lista porque luego se va a usar para contener las rutas de destino de cada archivo

os.mkdir(dest[0])

n = int(input('¿Cuántos TIPOS de archivos quieres separar (.pdf,.txt...)? Introduce el NÚMERO:'))

extensiones = []       #se inicializa la lista de los tipos de archivos que van a ser copiados

for i in range(n):
    file_extension = input('Extensión de los archivos a copiar:')
    extensiones.append(file_extension)      #Se crea una lista con las extensiones de los archivos que se quieren separar

list_archivos_r,list_archivos = list_paths(src)
dir_list,copy_list = subdir_eval(list_archivos_r,extensiones)
dest = dest*len(list_archivos)


dir_exists = True
list_subdir = []

while dir_exists == True :

    destaux = []

    for i, file in enumerate(list_archivos_r):

        if os.path.isdir(file) == True:
            os.mkdir(os.path.join(dest[i], list_archivos[i]))      # Se copia el subnivel de subdirectorios
            list_subdir.append(list_archivos_r[i])
            destaux.append(os.path.join(dest[i],list_archivos[i]))   #variable auxiliar que lista las rutas de destino para el próximo ciclo
        elif file in copy_list:
            shutil.copy2(file,dest[i])


    list_archivos_r = []
    list_archivos = []
    copy_list = []           # una vez copiado el nivel anterior se reinician las listas para pasar al siguiente nivel
    dest =[]


    for i,ruta in enumerate(list_subdir):
        list_archivos_raux,list_archivosaux = list_paths(ruta)
        subdir_listaux, copy_listaux = subdir_eval(list_archivos_raux, extensiones)
        list_archivos_r = list_archivos_r + list_archivos_raux
        list_archivos = list_archivos + list_archivosaux
        copy_list = copy_list + copy_listaux
        dest = dest + [destaux[i]]*len(list_archivosaux)     # se generan las rutas de destino que corresponderán con los archivos


    if list_archivos == [] :
        dir_exists = False                                   # el programa se cierra en caso de no haber más archivos en el siguiente nivel

    list_subdir = []
