import requests
import json


class WordpressRest:
    tokenkey = None

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_jwtoken()

    def login_jwtoken(self):
        post_url = "http://localhost/wp-json/jwt-auth/v1/token"
        myobj = {'username': self.username,
                 'password': self.password}

        x = requests.post(post_url, data=myobj).json()
        token = x["token"]
        self.tokenkey = "Bearer " + token
