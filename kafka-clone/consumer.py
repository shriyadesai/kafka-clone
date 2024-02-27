#libraries
import pika
import os
import sys
from pika.exchange_type import ExchangeType
import datetime





#fetch consumer id and subscribed topic
c_id=sys.argv[1]
subscribed_to=sys.argv[2]

# Flag To recieve previous messages or latest messages
flag=int(input("1:For all messages" + "\n" + "2:Latest "))

path = './'+subscribed_to

if flag == 1:
    #Reading old messages
    file1= open(os.path.join(path, 'messages.txt'), 'r')
    Lines = file1.readlines()
    for line in Lines:
        print("Old Message: {}".format( line.strip()))
    #inserting old messages into the logs file with all details
        current_time = datetime.datetime.now()
        
        

        with open(os.path.join('./', 'logs_consumer.txt'), 'a') as log_file:
            log_file.write(line.strip()+','+subscribed_to+','+c_id+','+str(current_time)+"\n")



def on_message_received(ch, method, properties, body):
    print('Received new message: ',body.decode())
    #inserting new messages into the logs file with all details
    with open(os.path.join('./', 'logs_consumer.txt'), 'a') as log_file:
        log_file.write(body.decode()+','+subscribed_to+','+c_id+str(current_time)+"\n")    

#bindings
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

#creating channel 
channel = connection.channel()
channel.exchange_declare(exchange='topic', exchange_type=ExchangeType.topic)
queue = channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(exchange='topic', queue=queue.method.queue, routing_key=subscribed_to)

#consume messages from broker
channel.basic_consume(queue=queue.method.queue, auto_ack=True,
    on_message_callback=on_message_received)

print('Consumer %s Started Consuming '%(c_id))

channel.start_consuming()