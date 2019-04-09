import pika
import sys
from controller.kernel import openfile
from bs4 import BeautifulSoup
import requests
from controller.kernel import match_class


class Server:

    sservidor = ""
    listaJuegos = {}

    def __init__(self):
        self.sservidor = sys.argv[0]
        self.listaJuegos = {'vampire Bloodline 2': 'https://www.allkeyshop.com/blog/buy-vampire-the-masquerade-bloodlines-2-cd-key-compare-prices/',
                            'sekiro': 'https://www.allkeyshop.com/blog/buy-sekiro-shadows-die-twice-cd-key-compare-prices/',
                            'the division 2': 'https://www.allkeyshop.com/blog/buy-tom-clancys-the-division-2-cd-key-compare-prices/'
                            }

    # Función que devuelve un objeto conexion a RabbitMQ server
    def conexion(self, sservidor):
        oConexion = pika.BlockingConnection(pika.ConnectionParameters(sservidor))
        return oConexion

    # Cerramos la conexión con RabbitMQ server
    def cerrarConexion(self, sservidor):
        oConexion = self.conexion(self, sservidor)
        oConexion.close()

    def ListaDeJuegos(self):
        archivo = openfile("records.txt", "a+")
        for key, value in self.listaJuegos.items():
            name = key
            url = value
            result = requests.get(url)
            c = result.content
            parseador = BeautifulSoup(c, 'html5lib')
            precios = parseador.findAll(match_class(["price"]))
            # Precios del juego indicado.
            lListaPrecios = []
            archivo.write(name + ": ")
            pos = archivo.tell()
            archivo.seek(pos)
            for precio in precios:
                # Obtenemos el precio dentro de la etiqueta span
                sTexto = precio.span.text
                fPrecioFlotante = float(sTexto.join(sTexto.split()).replace("€", ""))
                archivo.write(sTexto.join(sTexto.split()).replace("€", "") + " ,")
                pos = archivo.tell()
                archivo.seek(pos)
                # Añadimos los precios en la lista
                lListaPrecios.append(fPrecioFlotante)
            archivo.write("\n")
            pos = archivo.tell()
            archivo.seek(pos)


def main():
    principal = Server()
    #Descarga en el fichero los juegos scrapeados
    principal.ListaDeJuegos()
    cnx = principal.conexion("localhost")
    channel = cnx.channel()
    channel.queue_declare(queue='payload')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(
        queue='payload', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()








