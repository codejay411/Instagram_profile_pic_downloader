import requests
from bs4 import BeautifulSoup as bs
import json
from flask import request
import os
import random
import os.path
import urllib.request as urllib2

from flask import Flask, render_template
import sys
import logging
app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/insta', methods=["POST"])
def insta():
    insta_url = 'https://www.instagram.com/'
    mydict=request.form
    insta_username=str(mydict['name'])
    # url
    url=insta_url+insta_username
    r=requests.get(url)
    source=r.content
    # source = urllib2.urlopen(url)
    soup = bs(source, 'lxml')
    # print(soup)
    #image_link=soup.find_all("meta")[15].get('content')
    image_link=soup.find("meta",  property="og:image")["content"]
    # render on the template
    return render_template('index.html', image_link=image_link)

    # insta_url = 'https://www.instagram.com/'
    # if (request.method == "POST"):
    #     mydict=request.form
    #     insta_username=str(mydict['name'])

    #     # url
    #     url=insta_url+insta_username

    #     r=requests.get(url)
    #     source=r.content
    #     # source = urllib2.urlopen(url)
    #     soup = bs(source, 'lxml')
    #     # print(soup)
    #     image_link=soup.find_all("meta")[15].attrs['content']
        
        

        # render on the template
    #     return render_template('index.html', image_link=image_link)
    # return render_template('index.html')




if __name__ == "__main__":
    app.debug = True
    app.run()