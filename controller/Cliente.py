import pika
from tkinter import *

#Aqui cargaremos toda la interfaz grafica.
top = Tk()
top.geometry("100x100")


def helloCallBack():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='payload')

    channel.basic_publish(exchange='', routing_key='payload', body='Hello World!')

    print(" [x] Sent 'Hello World!'")


B = Button(top, text = "Buscar", command = helloCallBack)
B.place(x=50, y=50)
top.mainloop()