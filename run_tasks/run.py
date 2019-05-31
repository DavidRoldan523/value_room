import time
from timeloop import Timeloop
from datetime import timedelta
import requests as requests_python

work_pila = Timeloop()


@work_pila.job(interval=timedelta(seconds=20))
def facebook_work():
    session_facebook = requests_python.Session()
    response = session_facebook.post('http://localhost:8000/api/v1/facebook/posts/',
                                      data={'page_id': '113387205347979',
                                            'token': 'EAAD3osazFggBAPzVrnNqgukFcOCUC6V93rBDm4L5TC7I3qYVKjCXOZCsSZAwiqL0ZAtm3LDmQVpgeByLlgumm1vwyGUZCbScdTyTPsiZBwilaPKagpc485ZBRSWKMtS8prsGXFZCZBrQIx0CzuX4lX0UiZAZCm261bfemmxPBVHmXLRpNfxK22igZA7a0ZARZCKLnekTFkEw09U0izQZDZD',
                                            'fields': 'id',
                                            'since': '2019-05-20',
                                            'until': '2019-05-29'},
                                      headers={'Authorization': 'Token 0141e2a9a2722fd0e31cae0d67517293b67c87ec'})
    print(response.json())
    print("10s job current time : {}".format(time.ctime()))


if __name__ == "__main__":
    work_pila.start(block=True)
