import requests
import json
import base64
from PIL import Image
from io import BytesIO

class CHATapi():

    def __init__(self):

        self.base_url = 'https://api.chat-api.com/instance331153'

        self.token = 'vbdmed2airok5m30'

    def send_message(self, num, message):
        
        body = {
            "phone": num,
            "body" : message
        }

        request = requests.post(url=f'{self.base_url}/sendMessage?token={self.token}', data=body)

        response = request.json()

        return response

    def gerar_qrcode(self):
        
        request = requests.get(url='{}/qr_code?token={}'.format(self.base_url, self.token))
       
        if request.ok:
           
            with open('app/static/qrcode.png', 'wb') as imagem:
                for dado in request.iter_content(1024):
                    if not dado:
                        pass
                    else:
                        imagem.write(dado)
                        print(dado)
        else:
            print(request)

CHATapi().gerar_qrcode()