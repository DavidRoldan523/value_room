import requests as requests_python


class DisplayVideoConnect:
    def __init__(self):
        self.client_id = '421700549759-f0buj7jpsfrbqduodfedspd3tl0iljuc.apps.googleusercontent.com'
        self.client_secret = 'uQBNnzk9Agi8zxLRk6B51s9k'
        self.refresh_token = '1/J_aI0_IP7CBxETQ0Lqs5aWHvy3u-wWWkVZ8c-OLeGwE'

    def connect(self):
        url = f"https://oauth2.googleapis.com/token?" \
            f"client_id={self.client_id}" \
            f"&client_secret={self.client_secret}" \
            f"&grant_type=refresh_token" \
            f"&refresh_token={self.refresh_token}"
        response = requests_python.post(url)
        token = response.json()
        return token['access_token']
