import json
import random
from datetime import datetime, timedelta, date

from bs4 import BeautifulSoup

from Comment import Comment
import requests
import re


class PostComments(Comment):
    def __init__(self, context, rate, post_id, name, token):
        super().__init__(context, rate)
        self.post_id = post_id
        self.name = name
        self.token = token.tokenkey


    def send_comment(self,):
        post_url = "http://localhost/wp-comments-post.php"

        myobj = {'rating': self.rate,
                 'comment': self.context,
                 'author': self.name,
                 'submit': 'Submit',
                 'comment_post_ID': self.post_id,
                 'comment_parent': '0'}

        post_request = requests.post(post_url, data=myobj)
        regex_comment_id = re.findall('<div id="comment-(.*?)" class="comment_container"><img alt',
                                      str(post_request.content))

        print(regex_comment_id)
        if regex_comment_id != [] or int(regex_comment_id[-1]) >= 0:
            self.edit_comment(regex_comment_id[-1])

        #17609
        #1005002505477256


    def edit_comment(self, comment_id):
        post_url = "http://localhost/wp-json/wp/v2/comments/" + str(comment_id)

        print(post_url)

        curlHeaders = {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        postDict = {
            "date_gmt": self.gen_datetime(),
            "status": "approved"
        }

        x = requests.post(post_url, json=postDict, headers=curlHeaders)

    @staticmethod
    def gen_datetime():
        start_date = date.today().replace(day=1, month=1).toordinal()
        end_date = date.today().toordinal()
        random_day = date.fromordinal(random.randint(start_date, end_date))
        json_datetime = str(random_day) + "T10:16:34"
        return json_datetime

