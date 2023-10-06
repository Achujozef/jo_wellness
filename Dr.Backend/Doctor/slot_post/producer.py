import pika, json
import ssl 
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.set_ciphers('ECDHE-RSA-AES128-GCM-SHA256')

params = pika.URLParameters('amqps://frqdhaxu:jWcYqPPsZ2rM6Ou_jNJS8fEn31ktTnDO@crow.rmq.cloudamqp.com/frqdhaxu')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    print('Rabit on Producer')
    # properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='User', body='hello')
