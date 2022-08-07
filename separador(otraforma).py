"""
Este script tiene el cometido de tomar un directorio, que puede tener varios niveles de subdirectorios, hacer una copia
con la misma jerarquía, pero sólo manteniendo los archivos de la extensión que le hayamos indicado

"""

import os


#--------------------------------------------------------------------------------------------------------------------------
def listar_rutas(route):              #lista las rutas de todos los archivos de un directorio en str

    lista_archivos_r = []
    lista_archivos = os.listdit(route)

    for dir in lista_archivos:
        lista_archivos_r.append(os.path.join(route, dir))  #lista de las rutas de todos los archivos de la subcarpeta
    return lista_archivos_r
#--------------------------------------------------------------------------------------------------------------------------
def subandingore(lista_archivos_r,extensiones):    #devuelve listas de las rutas de los subdirectorios y los archivos a ignorar en un directorio

    dir_list = []
    ignore_list = []
    not_ignore_list = []

    for route in lista_archivos_r:
        if os.path.isdir(route) == True:
            dir_list.append(route)  # Se gaurdan las rutas de los subdirectorios de nivel 1
        else:
            for end in extensiones:
                if route.endswith(end) == True:
                    not_ignore_list.append(route)   #Se guardan las rutas de los archivos que no se ignoran
    for ruta in lista_archivos_r:
        if ruta not in not_ignore_list:
            ignore_list.append(ruta)
    return (dir_list,ignore_list)
#--------------------------------------------------------------------------------------------------------------------------


src = input('Introduce la ruta de la carpeta que quieres copiar:')
dest = input('Introduce la ruta del destido de la carpeta copiada:')
n = int(input('¿Cuántos TIPOS de archivos quieres separar (.pdf,.txt...)? Introduce el número:'))

flist = []       #se inicializa la lista de los tipos de archivos que van a ser copiados
ignore_list = [] #se inicializa la lista de las rutas de los archivos a ignorar en el copiado para la función .copytree()

for i in range(n):
    file_extension = input('Extensión de los archivos a copiar:')
    flist.append(file_extension)      #Se crea una lista con las extensiones de los archivos que se quieren separar

lv1_files = os.listdir(src) #lista de nombres de archivos dentro del directorio principal
lv1_files_r = []       #Inicialización de la lista de las rutas los archivos de primer nivel

for dir in lv1_files:
    lv1_files_r.append(os.path.join(src,dir))      #Se guardan las rutas de los archivos de primer nivel

sub_dir_1 = []                                     #lista de subdirectorios de nivel 1
lv1_copy = []                                      #lista auxiliar de archivos de nivel 1 que se copiarán

for route in lv1_files_r:
    if os.path.isdir(route) == True:
        sub_dir_1.append(route)                           #Se gaurdan las rutas de los subdirectorios de nivel 1
    else:
        for end in flist:
            if route.endswith(end) == True:
                lv1_copy.append(route)



        ignore_list.append(route)

print(sub_dir_1)


#shutil.copytree(src, dest, ignore = ignore_list)






