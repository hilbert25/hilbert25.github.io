# -*- coding: UTF-8 -*-
import re
import time
import urllib2
import codecs
from bs4 import BeautifulSoup
#China 51 ,England 8, Spanish 7 ,Germany 9 ,Italy 13,Franch 16
countrys = [7,8,9,13,16,51]
def getData(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers = {"User-Agent": user_agent}
    request = urllib2.Request(url, headers=headers)
    data = urllib2.urlopen(request).read()
    return data

def getMatch(id):
    data_url = u'http://www.dongqiudi.com/data?competition=%d'
    data = getData(data_url%id)
    teams  = re.findall(r'team\/[0-9]*\.html',data)
    return teams #https://www.dongqiudi.com/team/50001794.html"

def getTeamPlayers(id):
    time.sleep(1.5)
    try:
        data_url = u'https://www.dongqiudi.com/%s'
        data = getData(data_url%id)
        players = re.findall(r'player\/[0-9]*\.html', data)
        club = re.findall(r'\"name\">([\s\S]*)</h1>',data)
        print club[0]
        player_list = []
        for player in players:
            getPlayers(player)
    except:
        pass

def getPlayers(id):
    try:
        data_url = u'https://www.dongqiudi.com/%s'
        data = getData(data_url % id)
        soup = BeautifulSoup(data,"html.parser")
        name = soup.findAll("h1",{"class":"name"})[0].string
        position = soup.findAll("ul",{"class":"detail_info"})[0].select("span")[3].string
        personal_info = BeautifulSoup(str(soup.findAll("div",{"class":"player_info"})[0]),"html.parser")
        player_img = personal_info.findAll("img",{"class":"player_img"})[0]
        out.write(unicode(name)+","+unicode(player_img.get('src'))+","+unicode(id)+"\n")
        print name,player_img.get('src'),id
        # print name,pic
        # if position == u'门将':
        #     speed = soup.findAll("div",{"class":"item item2"})[0].select('span')[0].string
        #     speed = 0 if speed == '-' else int(speed)
        #     shoot = 1
        #     guard = soup.findAll("div",{"class":"item item0"})[0].select('span')[0].string
        #     guard = 0 if guard == '-' else int(guard)
        # else:
        #     speed = soup.findAll("div",{"class":"item item0"})[0].select('span')[0].string
        #     speed = 0 if speed == '-' else int(speed)
        #     guard = soup.findAll("div",{"class":"item item2"})[0].select('span')[0].string
        #     guard = 0 if guard == '-' else int(guard)
        #     shoot = soup.findAll("div",{"class":"item item5"})[0].select('span')[0].string
        #     shoot = 0 if shoot == '-' else int(shoot)
        # print name,pic,position,speed,guard,shoot
        # if position * speed * shoot!=0:
        #     file.write(unicode(name)+","+unicode(pic)+","+unicode(position)+","+str(speed)+","+str(guard)+","+str(shoot)+"\n")
    except Exception, e:
        print e

file
out = codecs.open('img.txt','w+','utf-8')
for country in countrys:
    teams = getMatch(country)
    file = codecs.open(str(country)+'.txt','w','utf-8')
    for team in teams:
        getTeamPlayers(team)

