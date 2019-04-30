import os
import dropbox

# Esto nos sirve para buscar una etiqueta dentro de beautiful soup.
def match_class(target):
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    return do_match


# accionWorR especifica si se lee o se escribe en el fichero
def openfile(nombre, accionWorR):
    f = open(nombre, accionWorR)
    return f


# Comprobamos si el archivo pasado es vacío o no.
def archivovacio(nombre):
    return os.path.getsize(nombre) == 0


# Eliminamos el fichero.
def removefile(strfile):
    os.remove(strfile)


# Comprobamos si existe el fichero.
def fileexist(strfile):
    return os.path.isfile(strfile)


# Subida de fichero a Dropbox
def uploadfile(pathoffile):
    token = "581k3OkOEn8AAAAAAAAA-Kpojn4mgoJObCJqpvRw5m6GFZG2LNsL1YtJhfe8QoxX"
    dbx = dropbox.Dropbox(token)
    user = dbx.users_get_current_account()
    with open(pathoffile, "rb") as f:
        data = f.read()
    print("Uploading file")
    response = dbx.files_upload(data, str("/")+pathoffile, mute=True)