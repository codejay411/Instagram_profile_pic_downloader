import requests
from bs4 import BeautifulSoup as bs
import json
import random
import os.path
import urllib.request as urllib2

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    insta_url = 'https://www.instagram.com/'
    if (request.method == "POST"):
        mydict=request.form
        insta_username=str(mydict['name'])

        # url
        url=insta_url+insta_username

        r=requests.get(url)
        source=r.content
        # source = urllib2.urlopen(url)
        soup = bs(source, 'lxml')
        # print(soup)
        image_link=soup.find_all("meta")[15].attrs['content']
        
        

        # render on the template
        return render_template('index.html', image_link=image_link)
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)