import requests
from flask import request
import os
import random
from instascrape import Profile

from flask import Flask, render_template
import sys
import logging
from instascrape import Profile 
app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/insta', methods=["POST"])
def insta():
    mydict=request.form
    insta_username=str(mydict['name'])

    google = Profile(insta_username)
    google.scrape(keys=['profile_pic_url_hd'])
    print(google['profile_pic_url_hd'])
    image_link=google['profile_pic_url_hd']


    # render on the template
    return render_template('index.html', image_link=image_link)




if __name__ == "__main__":
    app.debug = True
    app.run()
