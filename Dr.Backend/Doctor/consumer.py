import pika, json, os, django



params = pika.URLParameters('amqps://frqdhaxu:jWcYqPPsZ2rM6Ou_jNJS8fEn31ktTnDO@crow.rmq.cloudamqp.com/frqdhaxu')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='Doctor')


def callback(ch, method, properties, body):
    print('Received in Doctor COnsumer')
    print(body)

channel.basic_consume(queue='Doctor', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
