from flask import Flask
from flask import request
import sys
import os
sys.path.append(os.path.abspath("./src")) #para poder importar as funções do diretório src
from jokenpo import jokenpo
from roleta import roleta
from tweetBot import tweetBot

JWT_TOKEN = "YOUR_JWT_TOKEN_HERE"
CHANNEL = 'YOUR_CHANNEL_ID_HERE'

app = Flask(__name__)

@app.route('/')
def mainPage():
    return 'StreamElements pack by @ezrealblindado'

@app.route('/roleta')
def roletaPage():
    try:
        user = request.args.get('user')
        return roleta(user, CHANNEL, JWT_TOKEN)
    except Exception as e:
        return 'Falha na requisição: ', e

@app.route('/jokenpo')
def jokenpoPage():
    try:
        user = request.args.get('user')
        choice = request.args.get('choice')
        return jokenpo(user, choice, CHANNEL, JWT_TOKEN)
    except Exception as e:
        return 'Falha na requisição: ', e

@app.route('/tweetBot')
def tweetBotPage():
    try:
        sender = request.args.get('sender')
        message = request.args.get('message')
        return tweetBot(sender, message)
    except Exception as e:
        return 'Falha na requisição: ', e

@app.route('/timeout')
def timeoutPage():
    user = request.args.get('user')
    return '/timeout '+user+' 5 Mama aaa';

