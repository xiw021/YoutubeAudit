#%%
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from urllib.request import urlopen
import html
import pandas as pd
import random
import socket
#%%  # https://www.delftstack.com/howto/python/get-ip-address-python/  https://free-proxy-list.net/blog/rotating-proxy-selenium

#%%
from selenium import webdriver
#PROXY = "192.168.1.216:2000" # IP:PORT or HOST:PORT
s = Service('chromedriver')
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument("--incognito")
driver2 = webdriver.Chrome(service=s,options=chrome_options)
driver2.get("https://www.youtube.com")

#%%

### 记得清除 watch history  记得更新 baseline, IP ADDRESS!! playspeed autoplay！！！！！！！
account = 5
interest = 3
percent = 1

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]

watchlist_filename = '/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/watchlist/' + str(account) + "_" + str(interest) + '_' + str(percent) + '.csv'
watchlist = pd.read_csv(watchlist_filename)
if len(watchlist['url']) == 179:
   watchlist = watchlist[['url','title','percent','interest']]
   watchlist.loc[len(watchlist.url)] = [watchlist['url'][0],watchlist['title'][0],watchlist['percent'][0],watchlist['interest'][0]]

watchlist['url'] = 'https://www.youtube.com' + watchlist['url']
watchlist = list(watchlist['url'])

#%%
baseline = []
for i in range(10):
   print(i)
   for j in range(6):
       driver2.execute_script("window.scrollTo(0, window.scrollY + 1500)")
       time.sleep(1)
   content = driver2.page_source.encode('utf-8')
   soup = BeautifulSoup(content, 'html.parser')
   rows = soup.find_all('ytd-rich-grid-row', {'class': 'style-scope ytd-rich-grid-renderer'})
   for row in rows:
       items = row.find_all('ytd-rich-item-renderer', 'style-scope ytd-rich-grid-row')
       for item in items:
           title = None
           url = None
           label = None
           channel = None
           view = None
           if len(item.find_all('ytd-display-ad-renderer')) > 0:
               continue
           try:
               title = item.find_all('a', {'id': 'video-title-link'})[0]['title']
           except:
               pass
           try:
               url = item.find_all('a', {'id': 'video-title-link'})[0]['href']
           except:
               pass
           try:
               label = item.find_all('a', {'id': 'video-title-link'})[0]['aria-label']
           except:
               pass
           try:
               channel = list(item.find_all('div', {'class': 'style-scope ytd-channel-name'})[0].find_all('a', {
               'class': 'yt-simple-endpoint style-scope yt-formatted-string'})[0])[0]
           except:
               pass
           try:
               view = list(item.find_all('span', {'class': 'style-scope ytd-video-meta-block'})[0])[0]
           except:
               pass
           templist = [title, url, channel, view, label]
           baseline.append(templist)
   driver2.refresh()
   time.sleep(2)
baselineDF = pd.DataFrame(baseline, columns=['title', 'url', 'channel', 'view', 'label'])
filename = 'baseline/baseline_' + str(account) + '_' + str(interest) + '_' + str(percent) + '.csv'
baselineDF.to_csv(filename)

#%%
for i in range(9):
   watch_stage = watchlist[i*20:(i+1)*20]
   for j in range(20):
       driver2.get(watch_stage[j])
       time.sleep(20)
   recommendation = []
   url = 'https://www.youtube.com/'
   driver2.get(url)
   for k in range(6):
       for m in range(6):
           driver2.execute_script("window.scrollTo(0, window.scrollY + 1500)")
           time.sleep(1)
       content = driver2.page_source.encode('utf-8')
       soup = BeautifulSoup(content, 'html.parser')
       rows = soup.find_all('ytd-rich-grid-row', {'class': 'style-scope ytd-rich-grid-renderer'})
       for row in rows:
           items = row.find_all('ytd-rich-item-renderer', 'style-scope ytd-rich-grid-row')
           for item in items:
               title = None
               url = None
               label = None
               channel = None
               view = None
               if len(item.find_all('ytd-display-ad-renderer')) > 0:
                   continue
               try:
                   title = item.find_all('a', {'id': 'video-title-link'})[0]['title']
               except:
                   pass
               try:
                   url = item.find_all('a', {'id': 'video-title-link'})[0]['href']
               except:
                   pass
               try:
                   label = item.find_all('a', {'id': 'video-title-link'})[0]['aria-label']
               except:
                   pass
               try:
                   channel = list(item.find_all('div', {'class': 'style-scope ytd-channel-name'})[0].find_all('a', {
                       'class': 'yt-simple-endpoint style-scope yt-formatted-string'})[0])[0]
               except:
                   pass
               try:
                   view = list(item.find_all('span', {'class': 'style-scope ytd-video-meta-block'})[0])[0]
               except:
                   pass
               templist = [title, url, channel, view, label]
               recommendation.append(templist)
       driver2.refresh()
       time.sleep(2)
   recommendationDF = pd.DataFrame(recommendation, columns=['title', 'url', 'channel', 'view', 'label'])
   recommendationDF['account'] = account
   recommendationDF['interest'] = interest
   recommendationDF['percent'] = percent
   recommendationDF['stage'] = i
   recommendationDF['IP'] = IP
   filename = 'recommend/recom_' + str(account) + '_' + str(interest) + '_' + str(percent) + '_' + str(i) + '.csv'
   recommendationDF.to_csv(filename)
