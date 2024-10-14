#%%
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from urllib.request import urlopen
import html
import pandas as pd
import random
#%%

######## Baseline with no login
baseline = []
for i in range(10):
    print(i)
#    username = 'qwe.ytbtest1@gmail.com'
#    password = 'p9kMk78s'
    s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
    # object of ChromeOptions class
    o = webdriver.ChromeOptions()
    # adding specific Chrome Profile Path
    # o.add_arguments = {'user-data-dir':'/Users/wuxiaohan/Library/Application\ Support/Google/Chrome/Profile\ 3 '}
    # set chromedriver.exe path
    driver = webdriver.Chrome(service=s, options=o)
    url = 'https://www.youtube.com/'
    driver.get(url)
    for j in range(6):
        driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
        time.sleep(1)
    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    driver.close()
    rows = soup.find_all('ytd-rich-grid-row', {'class': 'style-scope ytd-rich-grid-renderer'})
    for row in rows:
        items = row.find_all('ytd-rich-item-renderer', {'class':'style-scope ytd-rich-grid-row'})
        for item in items:
            title = item.find_all('a', {'id': 'video-title-link'})[0]['title']
            url = item.find_all('a', {'id': 'video-title-link'})[0]['href']
            label = item.find_all('a', {'id': 'video-title-link'})[0]['aria-label']
            channel = list(item.find_all('div', {'class': 'style-scope ytd-channel-name'})[0].find_all('a', {
                'class': 'yt-simple-endpoint style-scope yt-formatted-string'})[0])[0]
            view = list(item.find_all('span', {'class': 'style-scope ytd-video-meta-block'})[0])[0]
            templist = [title, url, channel, view, label]
            baseline.append(templist)
baselineDF = pd.DataFrame(baseline, columns=['title', 'url', 'channel', 'view', 'label'])
baselineDF.to_csv('defaultBasedline.csv')


#%%
username = 'qwe.ytbtest1@gmail.com'
password = 'p9kMk78s'
s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
#object of ChromeOptions class
o = webdriver.ChromeOptions()
#adding specific Chrome Profile Path
#o.add_arguments = {'user-data-dir':'/Users/wuxiaohan/Library/Application\ Support/Google/Chrome/Profile\ 3 '}
#set chromedriver.exe path
driver = webdriver.Chrome(service=s,options=o)
url = 'https://www.youtube.com/'
driver.get(url)
#%%
baseline = []
for i in range(10):
    print(i)
    for j in range(6):
        driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
        time.sleep(1)
    content = driver.page_source.encode('utf-8')
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
    driver.refresh()
    time.sleep(2)
baselineDF = pd.DataFrame(baseline, columns=['title', 'url', 'channel', 'view', 'label'])
baselineDF.to_csv('qweytbtest1Basedline.csv')


#%% # get news
Media_list = ['NBCnews',
'ABCnews',
'CNN',
'MSNBC',
'CBSNews',
'WashintonPost',
'NowThisNews',
'Reuters',
'FoxNews',
'BloombergPolitics',
'Associatedpress',
'PBSNewsHour',
'TheWhiteHouse',
'C-SPAN',
'NewYorkTimes',
'bbcnews',
'VICEnews',
'BloombergQuicktake']
url_list = ['https://www.youtube.com/c/NBCNews/videos',
'https://www.youtube.com/c/ABCNews/videos',
'https://www.youtube.com/user/CNN/videos',
'https://www.youtube.com/c/msnbc/videos',
'https://www.youtube.com/c/CBSNews/videos',
'https://www.youtube.com/c/WashingtonPost/videos',
'https://www.youtube.com/c/nowthisnews/videos',
'https://www.youtube.com/c/Reuters/videos',
'https://www.youtube.com/c/FoxNews/videos',
'https://www.youtube.com/c/BloombergPolitics/videos',
'https://www.youtube.com/c/ap/videos',
'https://www.youtube.com/c/PBSNewsHour/videos',
'https://www.youtube.com/c/WhiteHouse/videos',
'https://www.youtube.com/c/C-SPAN/videos',
'https://www.youtube.com/c/nytimes/videos',
'https://www.youtube.com/c/BBCNews/videos',
'https://www.youtube.com/c/VICENews/videos',
'https://www.youtube.com/BloombergTV/videos']
#%%
for i in range(len(url_list)):
    print(i)
    newslist = []
    s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
    # object of ChromeOptions class
    o = webdriver.ChromeOptions()
    # adding specific Chrome Profile Path
    # o.add_arguments = {'user-data-dir':'/Users/wuxiaohan/Library/Application\ Support/Google/Chrome/Profile\ 3 '}
    # set chromedriver.exe path
    driver = webdriver.Chrome(service=s, options=o)
    url = url_list[i]
    driver.get(url)
    for j in range(180):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(1)
    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    driver.close()
    items = soup.find_all('ytd-grid-video-renderer', {'class': 'style-scope ytd-grid-renderer'})
    for item in items:
        title = None
        url = None
        label = None
        channel = None
        view = None
        try:
            title = item.find_all('a', {'id': 'video-title'})[0]['title']
        except:
            pass
        try:
            url = item.find_all('a', {'id': 'video-title'})[0]['href']
        except:
            pass
        try:
            label = item.find_all('a', {'id': 'video-title'})[0]['aria-label']
        except:
            pass
        try:
            view = list(item.find_all('span', {'class': 'style-scope ytd-grid-video-renderer'})[0])[0]
        except:
            pass
        templist = [title, url, view, label]
        newslist.append(templist)
        newslistDF = pd.DataFrame(newslist, columns=['title', 'url', 'view', 'label'])
        filename = Media_list[i] + 'listDF.csv'
        newslistDF.to_csv(filename)

#%%
# get fashionBeauty
Media_list = ['itsjudytime',
'MichellePhan',
'Evelina',
'IngridNilsen',
'LauraLee',
'Teachingmensfashion',
'AlyssaForever']
url_list = ['https://www.youtube.com/c/ItsJudyTime/videos',
'https://www.youtube.com/c/MichellePhan/videos',
'https://www.youtube.com/c/evelina/videos',
'https://www.youtube.com/c/ingridnilsen/videos',
'https://www.youtube.com/c/lauralaura88leelee/videos',
'https://www.youtube.com/c/Teachingmensfashion/videos',
'https://www.youtube.com/c/CurlyByNature21/videos']

#%%
for i in range(0,len(Media_list)):
    print(i)
    newslist = []
    s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
    # object of ChromeOptions class
    o = webdriver.ChromeOptions()
    # adding specific Chrome Profile Path
    # o.add_arguments = {'user-data-dir':'/Users/wuxiaohan/Library/Application\ Support/Google/Chrome/Profile\ 3 '}
    # set chromedriver.exe path
    driver = webdriver.Chrome(service=s, options=o)
    url = url_list[i]
    driver.get(url)
    for j in range(60):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(1)
    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    driver.close()
    items = soup.find_all('ytd-grid-video-renderer', {'class': 'style-scope ytd-grid-renderer'})
    for item in items:
        title = None
        url = None
        label = None
        channel = None
        view = None
        try:
            title = item.find_all('a', {'id': 'video-title'})[0]['title']
        except:
            pass
        try:
            url = item.find_all('a', {'id': 'video-title'})[0]['href']
        except:
            pass
        try:
            label = item.find_all('a', {'id': 'video-title'})[0]['aria-label']
        except:
            pass
        try:
            view = list(item.find_all('span', {'class': 'style-scope ytd-grid-video-renderer'})[0])[0]
        except:
            pass
        templist = [title, url, view, label]
        newslist.append(templist)
        newslistDF = pd.DataFrame(newslist, columns=['title', 'url', 'view', 'label'])
        filename = Media_list[i] + 'listDF.csv'
        newslistDF.to_csv(filename)


#%%
# getting sports
Media_list = ['Rebound',
'NHL',
'Thefumble',
'brailleSkateboarding',
'Ridechannel',
'ShaolinCenter',
'TheMaxLife',
'tmzsports',
'DingProductions']
url_list = ['https://www.youtube.com/c/ReboundCentral/videos',
'https://www.youtube.com/c/NHL/videos',
'https://www.youtube.com/c/thefumble/videos',
'https://www.youtube.com/c/brailleskateboarding/videos',
'https://www.youtube.com/c/ride/videos',
'https://www.youtube.com/c/ShaolinCenter/videos',
'https://www.youtube.com/c/TheMacLife/videos',
'https://www.youtube.com/c/TMZSports/videos',
'https://www.youtube.com/c/DingProductions/videos']

#%%

for i in range(len(Media_list)):
    print(i)
    newslist = []
    s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
    # object of ChromeOptions class
    o = webdriver.ChromeOptions()
    # adding specific Chrome Profile Path
    # o.add_arguments = {'user-data-dir':'/Users/wuxiaohan/Library/Application\ Support/Google/Chrome/Profile\ 3 '}
    # set chromedriver.exe path
    driver = webdriver.Chrome(service=s, options=o)
    url = url_list[i]
    driver.get(url)
    for j in range(60):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(1)
    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    #driver.close()
    items = soup.find_all('ytd-grid-video-renderer', {'class': 'style-scope ytd-grid-renderer'})
    for item in items:
        title = None
        url = None
        label = None
        channel = None
        view = None
        try:
            title = item.find_all('a', {'id': 'video-title'})[0]['title']
        except:
            pass
        try:
            url = item.find_all('a', {'id': 'video-title'})[0]['href']
        except:
            pass
        try:
            label = item.find_all('a', {'id': 'video-title'})[0]['aria-label']
        except:
            pass
        try:
            view = list(item.find_all('span', {'class': 'style-scope ytd-grid-video-renderer'})[0])[0]
        except:
            pass
        templist = [title, url, view, label]
        newslist.append(templist)
        newslistDF = pd.DataFrame(newslist, columns=['title', 'url', 'view', 'label'])
        filename = Media_list[i] + 'listDF.csv'
        newslistDF.to_csv(filename)
#%%
# getting games
Media_list = ['PlayStation',
'Videogamedunkey',
'Boogie2988',
'Uberhaxornova',
'Dykgaming',
'IGN',
'MKIceAndFire',
'GhostRobo',
'GameXplain',
'Chaos',
'FuriousFade',
'AFGguides',
'Ubisoft North America',
'WhatCultureGaming',
'Polygon']
url_list = ['https://www.youtube.com/c/PlayStation/videos',
'https://www.youtube.com/user/videogamedunkey/videos',
'https://www.youtube.com/user/boogie2988/videos',
'https://www.youtube.com/user/UberHaxorNova/videos',
'https://www.youtube.com/user/DYKGaming/videos',
'https://www.youtube.com/c/IGN/videos',
'https://www.youtube.com/c/MKIceAndFire/videos',
'https://www.youtube.com/user/GhostRobo/videos',
'https://www.youtube.com/user/GameXplain/videos',
'https://www.youtube.com/c/chaosxsilencer/videos',
'https://www.youtube.com/c/FuriousFade/videos',
'https://www.youtube.com/c/AFGuidesHD/videos',
'https://www.youtube.com/c/UbisoftNA/videos',
'https://www.youtube.com/c/WhatCultureGaming/videos',
'https://www.youtube.com/c/polygon/videos']
#%%
for i in range(len(Media_list)):
    print(i)
    newslist = []
    s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
    # object of ChromeOptions class
    o = webdriver.ChromeOptions()
    # adding specific Chrome Profile Path
    # o.add_arguments = {'user-data-dir':'/Users/wuxiaohan/Library/Application\ Support/Google/Chrome/Profile\ 3 '}
    # set chromedriver.exe path
    driver = webdriver.Chrome(service=s, options=o)
    url = url_list[i]
    driver.get(url)
    for j in range(60):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(1)
    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    #driver.close()
    items = soup.find_all('ytd-grid-video-renderer', {'class': 'style-scope ytd-grid-renderer'})
    for item in items:
        title = None
        url = None
        label = None
        channel = None
        view = None
        try:
            title = item.find_all('a', {'id': 'video-title'})[0]['title']
        except:
            pass
        try:
            url = item.find_all('a', {'id': 'video-title'})[0]['href']
        except:
            pass
        try:
            label = item.find_all('a', {'id': 'video-title'})[0]['aria-label']
        except:
            pass
        try:
            view = list(item.find_all('span', {'class': 'style-scope ytd-grid-video-renderer'})[0])[0]
        except:
            pass
        templist = [title, url, view, label]
        newslist.append(templist)
        newslistDF = pd.DataFrame(newslist, columns=['title', 'url', 'view', 'label'])
        filename = Media_list[i] + 'listDF.csv'
        newslistDF.to_csv(filename)

#%%
# getting food
Media_list = ['Gordonramsay',
'Epicmealtime',
'Maangchi',
'Foodwishes',
'pickuplimes',
'Gugafoods',
'PreppyKitchen',
'Natashaskitchen',
'sortedfood',
'Justonecookbook',
'Cheaplazyvegan',
'MathaStewart',
'Caribbeanpot',
'LauraInTheKitchen']
url_list = ['https://www.youtube.com/user/gordonramsay/videos',
'https://www.youtube.com/c/epicmealtime/videos',
'https://www.youtube.com/user/Maangchi/videos',
'https://www.youtube.com/c/foodwishes/videos',
'https://www.youtube.com/c/PickUpLimes/videos',
'https://www.youtube.com/c/GugaFoods/videos',
'https://www.youtube.com/c/PreppyKitchen/videos',
'https://www.youtube.com/c/Natashaskitchen/videos',
'https://www.youtube.com/c/SORTEDFood/videos',
'https://www.youtube.com/c/JustonecookbookRecipes/videos',
'https://www.youtube.com/c/CheapLazyVegan/videos',
'https://www.youtube.com/c/MarthaStewart/videos',
'https://www.youtube.com/c/caribbeanpot/videos',
'https://www.youtube.com/c/LauraintheKitchen/videos']
#%%
for i in range(len(Media_list)):
    print(i)
    newslist = []
    s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
    # object of ChromeOptions class
    o = webdriver.ChromeOptions()
    # adding specific Chrome Profile Path
    # o.add_arguments = {'user-data-dir':'/Users/wuxiaohan/Library/Application\ Support/Google/Chrome/Profile\ 3 '}
    # set chromedriver.exe path
    driver = webdriver.Chrome(service=s, options=o)
    url = url_list[i]
    driver.get(url)
    for j in range(60):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(1)
    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    #driver.close()
    items = soup.find_all('ytd-grid-video-renderer', {'class': 'style-scope ytd-grid-renderer'})
    for item in items:
        title = None
        url = None
        label = None
        channel = None
        view = None
        try:
            title = item.find_all('a', {'id': 'video-title'})[0]['title']
        except:
            pass
        try:
            url = item.find_all('a', {'id': 'video-title'})[0]['href']
        except:
            pass
        try:
            label = item.find_all('a', {'id': 'video-title'})[0]['aria-label']
        except:
            pass
        try:
            view = list(item.find_all('span', {'class': 'style-scope ytd-grid-video-renderer'})[0])[0]
        except:
            pass
        templist = [title, url, view, label]
        newslist.append(templist)
        newslistDF = pd.DataFrame(newslist, columns=['title', 'url', 'view', 'label'])
        filename = Media_list[i] + 'listDF.csv'
        newslistDF.to_csv(filename)


#%%
# getting film
Media_list = ['universalPictures',
'WaltDisney',
'Deadmeat',
'MovieclipTrailers',
'Screenrant',
'MovieTheorists',
'TheThings',
'Artspear',
'shupupCartoons',
'RapidTrailer',
'Filmonger',
'Smasher',
'IsaacCarlson',
'FilmRise']
url_list = ['https://www.youtube.com/c/UniversalPictures/videos',
'https://www.youtube.com/user/disneyanimation/videos',
'https://www.youtube.com/c/DeadMeat/videos',
'https://www.youtube.com/c/MovieclipsTRAILERS/videos',
'https://www.youtube.com/c/ScreenRant/videos',
'https://www.youtube.com/c/FilmTheorists/videos',
'https://www.youtube.com/c/TheThings/videos',
'https://www.youtube.com/c/ArtSpearEntertainment/videos',
'https://www.youtube.com/c/shutupcartoons/videos',
'https://www.youtube.com/c/RapidTrailer/videos',
'https://www.youtube.com/c/FilMonger/videos',
'https://www.youtube.com/c/Smasher/videos',
'https://www.youtube.com/c/WotsoVideos/videos',
'https://www.youtube.com/c/FilmRiseMovies/videos']
#%%
for i in range(len(Media_list)):
    print(i)
    newslist = []
    s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
    # object of ChromeOptions class
    o = webdriver.ChromeOptions()
    # adding specific Chrome Profile Path
    # o.add_arguments = {'user-data-dir':'/Users/wuxiaohan/Library/Application\ Support/Google/Chrome/Profile\ 3 '}
    # set chromedriver.exe path
    driver = webdriver.Chrome(service=s, options=o)
    url = url_list[i]
    driver.get(url)
    for j in range(60):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(1)
    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    #driver.close()
    items = soup.find_all('ytd-grid-video-renderer', {'class': 'style-scope ytd-grid-renderer'})
    for item in items:
        title = None
        url = None
        label = None
        channel = None
        view = None
        try:
            title = item.find_all('a', {'id': 'video-title'})[0]['title']
        except:
            pass
        try:
            url = item.find_all('a', {'id': 'video-title'})[0]['href']
        except:
            pass
        try:
            label = item.find_all('a', {'id': 'video-title'})[0]['aria-label']
        except:
            pass
        try:
            view = list(item.find_all('span', {'class': 'style-scope ytd-grid-video-renderer'})[0])[0]
        except:
            pass
        templist = [title, url, view, label]
        newslist.append(templist)
        newslistDF = pd.DataFrame(newslist, columns=['title', 'url', 'view', 'label'])
        filename = Media_list[i] + 'listDF.csv'
        newslistDF.to_csv(filename)

#%%
url_poli_list = ['https://www.youtube.com/playlist?list=PL0tDb4jw6kPzup2yudYvQmoBt2CXXtklx',
                 'https://www.youtube.com/playlist?list=PLQOa26lW-uI9RrbA-IHtpjtGZ9oBOS5Gn',
                 'https://www.youtube.com/playlist?list=PL6XRrncXkMaVTxK67HPBMRmJBar_wBwbx',
                 'https://www.youtube.com/playlist?list=PLDIVi-vBsOEzEoc4l5NZ1ALZKFheB5Hjx',
                 'https://www.youtube.com/playlist?list=PLEb3ThbkPrFYLCBonpC7yPxoIvzbsvSAP',
                 'https://www.youtube.com/playlist?list=PLVix8d69sPe7m8ZjUktnSg-DoCgjiM2N4',
                 'https://www.youtube.com/playlist?list=PLZhRxE9191zMtf4g-bQVKAqV_OrtWhMsJ',
                 'https://www.youtube.com/playlist?list=PLlTLHnxSVuIyeEZPBIQF_krewJkY2JSwi',
                 'https://www.youtube.com/playlist?list=PLSN-rgQVTh0UpQN38LF3sNS_cxA3WAtV0',
                 'https://www.youtube.com/playlist?list=PLnwt1fUa-EVjm1Mua83aSYnYAUSNQhu1w',
                 'https://www.youtube.com/playlist?list=PLgawtcOBBjr-dSQW46DKUQWm8OoJ5zz4h',
                 'https://www.youtube.com/playlist?list=PLf0o4wbW8SXpVQCkBrbZjv4uRZrtYTX_a']
#%%
title = []
for i in range(len(url_poli_list)):
    s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
    # object of ChromeOptions class
    o = webdriver.ChromeOptions()
    # adding specific Chrome Profile Path
    # o.add_arguments = {'user-data-dir':'/Users/wuxiaohan/Library/Application\ Support/Google/Chrome/Profile\ 3 '}
    # set chromedriver.exe path
    driver = webdriver.Chrome(service=s, options=o)
    driver.get(url_poli_list[i])
    for j in range(30):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(1)
    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    titles = soup.find_all('a', {'id': 'video-title'})
    for item in titles:
        title.append(item['title'])
#%%
poli_sample = random.sample(title, 1200)
#%%
poli_sample = pd.DataFrame(poli_sample, columns = ['title'])
poli_sample.to_csv('polinews_sample.csv')

#%%
url_nonpoli_list = ['https://www.youtube.com/playlist?list=PL0tDb4jw6kPzzJmLxNb6Dafns2ju4GJ0E',
'https://www.youtube.com/playlist?list=PL0tDb4jw6kPy4rHtqPvumUB9B4DxPDRDf',
'https://www.youtube.com/playlist?list=PL0tDb4jw6kPzgWaN0Uutlq-gIirWAhUan',
'https://www.youtube.com/playlist?list=PL0tDb4jw6kPxEnxsfG6kiJZqMT_2Ci-Nn',
'https://www.youtube.com/playlist?list=PLQOa26lW-uI8WiHcj37H27ewnelsNKe6u',
'https://www.youtube.com/playlist?list=PLQOa26lW-uI9tT6o5Cc3ShxQzNcZhvApu',
'https://www.youtube.com/playlist?list=PL6XRrncXkMaUOQ1eMN5vFRc1KXE8AIn31',
'https://www.youtube.com/playlist?list=PL6XRrncXkMaWBU84P36CGEBTXOu-_V5Dp',
'https://www.youtube.com/playlist?list=PLAAAB0742973FF23D',
'https://www.youtube.com/playlist?list=PLE047FDA7C66422D8',
'https://www.youtube.com/playlist?list=PLEb3ThbkPrFbOO8lcTckW8SegHOwEknzM']
#%%
url_nonpoli_list = ['https://www.youtube.com/playlist?list=PL6XRrncXkMaXUslfXVzn1YbP5OcjZOo8Y',
'https://www.youtube.com/playlist?list=PL841EE38723FBCA00',
'https://www.youtube.com/playlist?list=PL6XRrncXkMaUDoHYLRfgyBptsGVv9ekAm',
'https://www.youtube.com/playlist?list=PLVix8d69sPe5iZ3pUB9WoOo3Z9dQ2_ThU']
#%%
title = []
for i in range(len(url_nonpoli_list)):
    s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
    # object of ChromeOptions class
    o = webdriver.ChromeOptions()
    # adding specific Chrome Profile Path
    # o.add_arguments = {'user-data-dir':'/Users/wuxiaohan/Library/Application\ Support/Google/Chrome/Profile\ 3 '}
    # set chromedriver.exe path
    driver = webdriver.Chrome(service=s, options=o)
    driver.get(url_nonpoli_list[i])
    for j in range(30):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(1)
    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    titles = soup.find_all('a', {'id': 'video-title'})
    for item in titles:
        title.append(item['title'])

#%%
nonpoli_sample = pd.DataFrame(title, columns = ['title'])
nonpoli_sample.to_csv('nonpolinews_sample2.csv')

#%%
with open("test.html", "w") as f:
    f.write(driver.page_source)
#%%

# Save HTML to a file
with open("soup.html", "wb") as f:
    while True:
        chunk = html.read(1024)
        if not chunk:
            break
        f.write(chunk)
# Read HTML from a file
with open("soup.html", "rb") as f:
    soup = BeautifulSoup(f.read(), "lxml")

print(soup.title)