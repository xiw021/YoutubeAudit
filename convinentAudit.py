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
import pickle


#%%
recommend = pd.read_csv('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/recommend_sample_audit.csv') # 3176
#recommend = pd.read_csv('/Users/wuxiaohan/Desktop/baseline_sample_audit.csv') # 1000
#recommend = pd.read_csv('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/food_recommend_audit_add2.csv')
recommend['url'] = 'https://www.youtube.com' + recommend['url']

#%%

s = Service('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/chromedriver')
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(service=s,options=chrome_options)

title = []
code = []
for i in range(3177,len(recommend)):
    print(i)
    driver.get(recommend['url'][i])
    value = input("Please enter the code:\n")
    print(f'You entered {value}')
    title.append(recommend['title'][i])
    code.append(value)



#%%
code[141] = 6

#%%
# initialize data of lists.
data = {'title': title,
        'code': code}

# Create DataFrame
df = pd.DataFrame(data)

df.to_csv('food_random_audit3.csv')


#%%
df = pd.read_csv('food_random_audit.csv')
df = df.drop_duplicates(subset=['title'])
df.to_csv('food_random_audit.csv')

