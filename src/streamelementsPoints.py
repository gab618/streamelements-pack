import requests
import json

def givePoints(user, points, channel, jwt_token):
    try:
        url = "https://api.streamelements.com/kappa/v2/points/"+channel+"/"+user+"/"+points
        headers = {
            'accept': "application/json",
            'content-type': "Content-Type",
            'authorization': 'Bearer '+jwt_token
                }
        response = requests.request("PUT", url, headers=headers)
        responseData = json.loads(response.text)
        print(responseData)
        return responseData
    except Exception as e:
            return 'Error: ', e