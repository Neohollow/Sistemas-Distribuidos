import pika
from tkinter import *


# Opciones disponibles que el cliente pueda seleccionar
OPTIONS = ["vampire Bloodline 2", "sekiro", "the division 2"]

#Iniciamos sesión con Google

# Aqui cargaremos toda la interfaz grafica.
top = Tk()
top.title = "Cliente"
top.geometry("100x100")

# Añadimos una rejilla
mainframe = Frame(top)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

tkvar = StringVar(top)
tkvar.set(OPTIONS[0])

popupMenu = OptionMenu(mainframe, tkvar, *OPTIONS)
Label(mainframe, text="Elige un juego").grid(row = 1, column = 1)
popupMenu.grid(row=2, column=1)


# Evento, cuando cambia el valor de la lista desplegable.
def change_dropdown(*args):
    sjuego = tkvar.get()
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='payload')
    channel.basic_publish(exchange='', routing_key='payload', body=sjuego)


# link function to change dropdown
tkvar.trace('w', change_dropdown)
top.mainloop()
