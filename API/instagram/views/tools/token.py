import requests as requests_python

class Token:
    def __init__(self):
        self.client_id = '272278490387976'
        self.client_secret = '817e43a3a93beb7da194c28a7013950d'
        self.fb_exchange_token = 'EAAD3osazFggBAO3y3V6olXlnM1yLeGQa6hWE2TEmH9XIM92pg4g6Ee6CZBf094sw1HHZCAK73cZC03pzxIrZACFr1FtzBbA0dSmRGMACzbEY23otq7upXWXPYubU3wLGLho3jGIKIcOe356dZCaWtkf2SZCicRx8YQiQILlh2COQZDZD'

    def get_fb_token(self):
        url_posts = f"https://graph.facebook.com/oauth/access_token?" \
            f"client_id={self.client_id}" \
            f"&client_secret={self.client_secret}" \
            f"&grant_type=fb_exchange_token" \
            f"&fb_exchange_token={self.fb_exchange_token}"
        response = requests_python.get(url_posts)
        token = response.json()
        return token['access_token']
