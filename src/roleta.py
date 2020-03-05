import random
from streamelementsPoints import givePoints

def roleta(user, channel, jwt_token):
    bala = random.randint(1,5)
    if bala == 1:
        return '/timeout '+user+' 5 Mama timeout!'
    if bala == 2:
        return '/timeout '+user+' 10 Farma timeout ai kkk'
    if bala == 3:
        return '/timeout '+user+' 15 só o !quote 31 né velho xD'
    if bala == 4 or bala == 5:
        try:
            response = givePoints(user,'4',channel,jwt_token)
            saida = (user+' stackou 4 e agora possui '+str(response['newAmount'])+' stacks da gota PogChamp')
            return saida

        except Exception as e:
            return 'Erro: ', e
