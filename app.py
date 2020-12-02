import flask
from flask import request
#import pandas as pd
from datetime import datetime as dt
import pika 

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    connection = pika.BlockingConnection(pika.URLParameters("amqps://urfvnqok:kDPF6YteXqwoKytSirWyl_HAisUjTGYl@woodpecker.rmq.cloudamqp.com/urfvnqok"))
    channel = connection.channel()
    #channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    routing_key = "Chatbot.PedidoConeccion"
    message = '{ "url": https://botdisenio.herokuapp.com/webhooks/my_connector/webhook/ }'
    channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
    connection.close()
    #year = int(request.args['year'])
    return "Hello world"
    
