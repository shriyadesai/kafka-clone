#libraries
import pika
import os
import sys
from pika.exchange_type import ExchangeType
import datetime


#fetch producer id
p_id=sys.argv[1]

#bindings
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

#creating channel
channel = connection.channel()
channel.exchange_declare(exchange='topic', exchange_type=ExchangeType.topic)

#Accept messages and topic from user
message=input(str("Enter Message : "))
topic=input(str("Enter Topic Name: "))

#check if messages present in directory
topic_list=[]
path = './'+topic
if not os.path.exists(path):
    os.makedirs(path)
filename =  'messages.txt'

#Mapping topics with messages and pid 
with open(os.path.join(path, filename), 'a') as temp_file:
    temp_file.write(p_id+':'+message+"\n")

#publish message to broker
channel.basic_publish(exchange='topic', routing_key=topic, body=p_id+':'+message)
current_time = datetime.datetime.now()
with open(os.path.join('./', 'logs_producer.txt'), 'a') as log_file:
    log_file.write(p_id+':'+message+':'+topic+':'+str(current_time)+"\n") 

print(f'Sent message: {message}')



connection.close()