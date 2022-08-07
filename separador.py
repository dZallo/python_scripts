"""
PNM 05/08/2022
Este script tiene el cometido de tomar un directorio, que puede tener varios niveles de subdirectorios, hacer una copia
con la misma jerarquía, pero sólo manteniendo los archivos de la extensión que le hayamos indicado

"""
#--------------------------------------------------------------------------------------------------------------------------
from fnmatch import filter
from os.path import isdir,join
from shutil import copytree
#--------------------------------------------------------------------------------------------------------------------------
def include_patterns(*patterns):
    """Factory function that can be used with copytree() ignore parameter.

    Arguments define a sequence of glob-style patterns
    that are used to specify what files to NOT ignore.
    Creates and returns a function that determines this for each directory
    in the file hierarchy rooted at the source directory when used with
    shutil.copytree().
    """

    def _ignore_patterns(path, names):
        keep = set(name for pattern in patterns
                   for name in filter(names, pattern))
        ignore = set(name for name in names
                     if name not in keep and not isdir(join(path, name)))
        return ignore

    return _ignore_patterns
#--------------------------------------------------------------------------------------------------------------------------
src = input('Introduce la ruta de la carpeta que quieres copiar:')
dest = input('Introduce la ruta del destido de la carpeta copiada:')
#n = int(input('¿Cuántos TIPOS de archivos quieres separar (.pdf,.txt...)? Introduce el número:'))

flist = []       #se inicializa la lista de los tipos de archivos que van a ser copiados

#for i in range(n):
#    file_extension = input('Extensión de los archivos a copiar:')
#   flist.append('*' + file_extension)      #Se crea una lista con las extensiones de los archivos que se quieren separar

copia = input ('Introduce la extensión del archivo que quieres aislar (incluye el punto):')
copia = '*' + copia

copytree(src, dest, ignore=include_patterns(copia))

