import requests
import json
import base64
from PIL import Image
from io import BytesIO

class APIwhats():

    def __init__(self):

        
        self.authorization = {
            'X-Client-id': '5876656',
            'X-Client-secret': '74a161d238d15ac1ea740dcb9273d741' 
        }
        self.instance = 'E54AB23BCB' 
        
        self.get_token = {
            'Access-token' : f'{self.token()}',
            }
    def token(self):

        request = requests.post(url='https://api-whats.com/api/v1/oauth/token/', headers=self.authorization)

        response = request.json()

        return response['access_token']

    def envia_message(self, message, numero):
        print(self.get_token)
        request = requests.post(url=f'https://api-whats.com/api/v1/message/send/?instance={self.instance}&phone={numero}&message={message}', headers=self.get_token)
        print(request.url)
        response = request.json()

        return response

    def verifica(self):
        request = requests.post(url='https://api-whats.com/api/v1/instance/verify/{}'.format(self.instance), headers=self.get_token)
        print(request.url)
        response = request.json()

        return response

    def gerar_qrcode(self):
        print(self.get_token)
        request = requests.post(url="https://api-whats.com/api/v1/instance/qrcode/E54AB23BCB", headers=self.get_token)
        print(request.url)
        response = request.json()
        print(response)
        if response['status'] == 'success':

            data = response['qrcode']
            data = data.partition(',')[2]

            im = Image.open(BytesIO(base64.b64decode(data)))
            im.save('image.png', 'PNG')
            return response
        else:
            return 'error'


