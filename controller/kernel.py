import os

def match_class(target):
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    return do_match


# accionWorR especifica si se lee o se escribe en el fichero
def openfile(nombre, accionWorR):
    f = open(nombre, accionWorR)
    return f


def archivovacio(nombre):
    return os.path.getsize(nombre) == 0


#Eliminamos el fichero.
def removefile(strfile):
    os.remove(strfile)


#Comprobamos si existe el fichero.
def fileexist(strfile):
    return os.path.isfile(strfile)

