import numpy as np
import cv2
import imutils
import datetime
import socketio
import base64

from control import *

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event 
def my_message(data):
    print('message received with ', data)
    sio.emit('message', {'response': 5})


@sio.event
def disconnect():
    print("I'm disconnected!")


def notificacion():
    #await asyncio.emit('msg', {'noti':'¡¡¡¡Arma detectada!!!!'})
    sio.emit('msg',{'notificacion':'¡¡¡¡Arma detectada!!!!'})

if __name__ == '__main__':
    transmitir = False
    sio.connect('http://localhost:8080')
    sio.emit('msg', {'response': 'Holaaaaaaaaa soy la vigilanci'})
    detectar_arma(sio)
    sio.wait()




