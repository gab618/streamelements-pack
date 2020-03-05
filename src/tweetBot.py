import oauth2
import json
import urllib.parse


def tweetBot(sender, message):
    #twitter keys
    consumer_key = 'YOUR_CONSUMER_KEY_HERE'
    consumer_secret = 'YOUR_CONSUMER_SECRET_HERE'
    token_key = 'YOUR_TOKEN_KEY_HERE'
    token_secret = 'YOUR_TOKEN_SECRET_HERE'

    #auth
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    token = oauth2.Token(token_key, token_secret)
    cliente = oauth2.Client(consumer, token)


    #exec
    query = sender+": "+message
    if (len(query) >280):
        return 'Limite de caracteres ultrapassado ('+str(len(query) - 280)+')'
    query_codificada = urllib.parse.quote(query, safe='')
    print((query_codificada))
    requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')

    #exibir no terminal
    #decodificar = requisicao[1].decode()
    #objeto = json.loads(decodificar)
    return 'Tweetado com sucesso 👍 @'+sender
