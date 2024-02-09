import requests
import json
class Bot:
    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"
        
    def get_updates(self, offset=None):
        method = "getUpdates"
        params = {'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result = resp.json()
        return result
    
    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = "sendMessage"
        resp = requests.post(self.api_url + method, params).json()
        return resp
    
    def getRisposta(self, last_update_id):
        while True:
            #sleep(5)
            data = self.get_updates(last_update_id)
            if len(data['result']) > 0:
                last_update_id = last_update_id + 1
                return data
    
    def sendKeyboard(self, chat_id, options):
        url = f"{self.api_url}sendMessage"
        keyboard = {
            "keyboard": [[{"text": option} for option in options]],
            "resize_keyboard": True, 
            "one_time_keyboard": True
        }
        payload = {
            "chat_id": chat_id,
            "text": "Seleziona un opzione",
            "reply_markup": json.dumps(keyboard)
        }
        requests.post(url, data=payload)
    