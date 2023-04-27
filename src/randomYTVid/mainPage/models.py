from django.db import models


import json
import urllib.request
import string
import random
import webbrowser


# Create your models here.

class Videos(models.Model):

    videoID = models.CharField(max_length=100)


    @classmethod 
    def create(self):
        vidIdList = []
        count = 50
        API_KEY = '' 
        randy = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

        urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,randy)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        results = json.loads(data.decode(encoding))

        for data in results['items']:
            videoId = (data['id']['videoId'])
            randomVid = self(videoID = videoId)
            randomVid.save(force_insert=True)
            vidIdList.append(randomVid)

        return vidIdList

    def __str__(self):
        return self.videoID






    




