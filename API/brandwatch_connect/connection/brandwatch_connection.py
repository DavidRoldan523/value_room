import requests as requests_python


class BrandWatchConnection:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def connect(self):
        url = f"https://api.brandwatch.com/oauth/token" \
              f"?username={self.username}" \
              f"&grant_type=api-password" \
              f"&client_id=brandwatch-api-client"
        response = requests_python.post(url, data={'password': f'{self.password}'})
        return response.json()['access_token']
