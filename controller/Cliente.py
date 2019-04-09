import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='payload')

channel.basic_publish(exchange='', routing_key='payload', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()