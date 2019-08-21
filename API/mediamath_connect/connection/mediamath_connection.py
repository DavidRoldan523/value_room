import terminalone


class MediaMathConnection:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def connect(self):
        """
            t1 = T1(auth_method='oauth2-resourceowner',
            client_id="my_client_id",
            client_secret="my_secret",
            username="my@user",
            # Recomended Connection
            password="mypass")
        """
        return terminalone.T1(self.username, self.password)


