import random
from streamelementsPoints import givePoints
def jokenpo(user, choice, channel, jwt_token):
    botChoice = random.randint(1,3)
    if(choice == 'pedra'):
        if (botChoice == 1): #win
            response =  givePoints(user,'2',channel,jwt_token)
            amount = response['amount']
            return '/me @'+user+' solou o bot com uma pedrada 👊 PogChamp (+'+str(amount)+')'
        elif (botChoice == 2): #lose
            return '/me @'+user+' perdeu! O bot te solou com um papel 👋 BibleThump'
        elif (botChoice == 3): #draw
            return '/me Empate! @'+user+' e o bot lançaram a pedra 👊 ResidentSleeper'

    elif (choice == 'papel'):
        if (botChoice == 1): #win
            response =  givePoints(user,'2',channel,jwt_token)
            amount = response['amount']
            return '/me @'+user+' solou o bot no papel 👋 PogChamp (+'+str(amount)+')'
        elif (botChoice == 2): #lose
            return '/me @'+user+' perdeu! O bot te solou na tesourada ✌ BibleThump'
        elif (botChoice == 3): #draw
            return '/me Empate! @'+user+' e o bot lançaram papel 👋 ResidentSleeper'

    elif (choice == 'tesoura'):
        if (botChoice == 1): #win
            response =  givePoints(user,'2',channel,jwt_token)
            amount = response['amount']
            return '/me @'+user+' solou o bot com uma tesouurada no pescoço ✌ Poggers (+'+str(amount)+')'
        elif (botChoice == 2): #lose
            return '/me @'+user+' perdeu! O bot te solou na pedrada 👊 BibleThump'
        elif (botChoice == 3): #draw
            return '/me Empate! @'+user+' e o bot lançaram a ✌ ResidentSleeper'

    else:
        return '/me @'+user+' Escolha *'+choice+'* inválida. Opções: pedra, papel, tesoura'


