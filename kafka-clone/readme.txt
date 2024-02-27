

TOPIC: YET ANOTHER KAFKA (YAK) 

PRE-REQUISITES: RabbitMQ and python3

1)To run this we need to have RabbitMQ installed locally on our system.
2)Producers are dynamic
3)Consumers are dynamic
4)Topics are dynamic
5)Topics are stored in local FS
6)Log file entries are made each time a consumer receives a message for a particular topic from any producer.
7)This log file is maintained in the local FS for other brokers to look into, on event of a leader broker failure.
8)When the producer is called, it is asked to enter the topic and corresponding message.
9)The same is also being put into the local FS dynamically which is grouped by topics.
10)The consumer is asked with two things:
	1)Mention the topic it wants to subscribe to
	2)Mention if it wants all the previous messages from the time of topic creation.
11)Whenever producer sends a message, it is put into the log_producer file with datetime
12)In either cases, all messages received by the consumer will be updated in the logs file with datetime
 

