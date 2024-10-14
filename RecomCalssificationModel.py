#%%
import pandas as pd
import random
import numpy as np
import random
import re
import nltk
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')
import pickle
import sklearn
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#%%
NBCnews = pd.read_csv('newslists/NBCnewslistDF.csv')
NBCnews = NBCnews.loc[NBCnews['predPoli'] == 1].reset_index()
NBCnews = NBCnews[["title", "url",'view','label']]
NBCnews['channel'] = 'NBCnews'

ABCnews = pd.read_csv('newslists/ABCnewslistDF.csv')
ABCnews = ABCnews.loc[ABCnews['predPoli'] == 1].reset_index()
ABCnews = ABCnews[["title", "url",'view','label']]
ABCnews['channel'] = 'ABCnews'

CNN = pd.read_csv('newslists/CNNlistDF.csv')
CNN = CNN.loc[CNN['predPoli'] == 1].reset_index()
CNN = CNN[["title", "url",'view','label']]
CNN['channel'] = 'CNN'

MSNBC = pd.read_csv('newslists/MSNBClistDF.csv')
MSNBC = MSNBC.loc[MSNBC['predPoli'] == 1].reset_index()
MSNBC = MSNBC[["title", "url",'view','label']]
MSNBC['channel'] = 'MSNBC'

CBSNews = pd.read_csv('newslists/CBSNewslistDF.csv')
CBSNews = CBSNews.loc[CBSNews['predPoli'] == 1].reset_index()
CBSNews = CBSNews[["title", "url",'view','label']]
CBSNews['channel'] = 'CBSNews'

WashintonPost = pd.read_csv('newslists/WashintonPostlistDF.csv')
WashintonPost = WashintonPost.loc[WashintonPost['predPoli'] == 1].reset_index()
WashintonPost = WashintonPost[["title", "url",'view','label']]
WashintonPost['channel'] = 'WashintonPost'

NowThisNews = pd.read_csv('newslists/NowThisNewslistDF.csv')
NowThisNews = NowThisNews.loc[NowThisNews['predPoli'] == 1].reset_index()
NowThisNews = NowThisNews[["title", "url",'view','label']]
NowThisNews['channel'] = 'NowThisNews'

Reuters = pd.read_csv('newslists/ReuterslistDF.csv')
Reuters = Reuters.loc[Reuters['predPoli'] == 1].reset_index()
Reuters = Reuters[["title", "url",'view','label']]
Reuters['channel'] = 'Reuters'

FoxNews = pd.read_csv('newslists/FoxNewslistDF.csv')
FoxNews = FoxNews.loc[FoxNews['predPoli'] == 1].reset_index()
FoxNews = FoxNews[["title", "url",'view','label']]
FoxNews['channel'] = 'FoxNews'

BloombergPolitics = pd.read_csv('newslists/BloombergPoliticslistDF.csv')
BloombergPolitics = BloombergPolitics.loc[BloombergPolitics['predPoli'] == 1].reset_index()
BloombergPolitics = BloombergPolitics[["title", "url",'view','label']]
BloombergPolitics['channel'] = 'BloombergPolitics'

Associatedpress = pd.read_csv('newslists/AssociatedpresslistDF.csv')
Associatedpress = Associatedpress.loc[Associatedpress['predPoli'] == 1].reset_index()
Associatedpress = Associatedpress[["title", "url",'view','label']]
Associatedpress['channel'] = 'Associatedpress'

PBSNewsHour = pd.read_csv('newslists/PBSNewsHourlistDF.csv')
PBSNewsHour = PBSNewsHour.loc[PBSNewsHour['predPoli'] == 1].reset_index()
PBSNewsHour = PBSNewsHour[["title", "url",'view','label']]
PBSNewsHour['channel'] = 'PBSNewsHour'

TheWhiteHouse = pd.read_csv('newslists/TheWhiteHouselistDF.csv')
TheWhiteHouse = TheWhiteHouse.loc[TheWhiteHouse['predPoli'] == 1].reset_index()
TheWhiteHouse = TheWhiteHouse[["title", "url",'view','label']]
TheWhiteHouse['channel'] = 'TheWhiteHouse'

CSPAN = pd.read_csv('newslists/CSPANlistDF.csv')
CSPAN = CSPAN.loc[CSPAN['predPoli'] == 1].reset_index()
CSPAN = CSPAN[["title", "url",'view','label']]
CSPAN['channel'] = 'CSPAN'

news = [NBCnews,ABCnews,CNN,MSNBC,CBSNews,WashintonPost,NowThisNews,Reuters,FoxNews,BloombergPolitics,Associatedpress,PBSNewsHour,TheWhiteHouse,CSPAN]

brailleSkateboarding = pd.read_csv('entertain/sports/brailleSkateboardinglistDF.csv')
brailleSkateboarding['channel'] = 'brailleSkateboarding'

DingProductions = pd.read_csv('entertain/sports/DingProductionslistDF.csv')
DingProductions['channel'] = 'DingProductions'

ESPN = pd.read_csv('entertain/sports/ESPNlistDF.csv')
ESPN['channel'] = 'ESPN'

NBA = pd.read_csv('entertain/sports/NBAlistDF.csv')
NBA['channel'] = 'NBA'

NFL = pd.read_csv('entertain/sports/NFLlistDF.csv')
NFL['channel'] = 'NFL'

NHL = pd.read_csv('entertain/sports/NHLlistDF.csv')
NHL['channel'] = 'NHL'

Rebound = pd.read_csv('entertain/sports/ReboundlistDF.csv')
Rebound['channel'] = 'Rebound'

Ridechannel = pd.read_csv('entertain/sports/RidechannellistDF.csv')
Ridechannel['channel'] = 'Ridechannel'

ShaolinCenter = pd.read_csv('entertain/sports/ShaolinCenterlistDF.csv')
ShaolinCenter['channel'] = 'ShaolinCenter'

TheWorldofBoxing  = pd.read_csv('entertain/sports/TheWorldofBoxinglistDF.csv')
TheWorldofBoxing['channel'] = 'TheWorldofBoxing'

Thefumble = pd.read_csv('entertain/sports/ThefumblelistDF.csv')
Thefumble['channel'] = 'Thefumble'

TheMaxLife = pd.read_csv('entertain/sports/TheMaxLifelistDF.csv')
TheMaxLife['channel'] = 'TheMaxLife'

tmzsports = pd.read_csv('entertain/sports/tmzsportslistDF.csv')
tmzsports['channel'] = 'tmzsports'

XGames = pd.read_csv('entertain/sports/XGameslistDF.csv')
XGames['channel'] = 'XGames'


sports = [brailleSkateboarding,DingProductions,ESPN,NBA,NFL,NHL,Rebound,Ridechannel,ShaolinCenter,TheWorldofBoxing,Thefumble,TheMaxLife,tmzsports,XGames]

PlayStation = pd.read_csv('entertain/game/PlayStationlistDF.csv')
PlayStation['channel'] = 'PlayStation'
Videogamedunkey = pd.read_csv('entertain/game/VideogamedunkeylistDF.csv')
Videogamedunkey['channel'] = 'Videogamedunkey'
Boogie2988 = pd.read_csv('entertain/game/Boogie2988listDF.csv')
Boogie2988['channel'] = 'Boogie2988'
Uberhaxornova = pd.read_csv('entertain/game/UberhaxornovalistDF.csv')
Uberhaxornova['channel'] = 'Uberhaxornova'
IGN = pd.read_csv('entertain/game/IGNlistDF.csv')
IGN['channel'] = 'IGN'
MKIceAndFire = pd.read_csv('entertain/game/MKIceAndFirelistDF.csv')
MKIceAndFire['channel'] = 'MKIceAndFire'
GhostRobo = pd.read_csv('entertain/game/GhostRobolistDF.csv')
GhostRobo['channel'] = 'GhostRobo'
GameXplain = pd.read_csv('entertain/game/GameXplainlistDF.csv')
GameXplain['channel'] = 'GameXplain'
Chaos = pd.read_csv('entertain/game/ChaoslistDF.csv')
Chaos['channel'] = 'Chaos'
FuriousFade = pd.read_csv('entertain/game/FuriousFadelistDF.csv')
FuriousFade['channel'] = 'FuriousFade'
AFGguides = pd.read_csv('entertain/game/AFGguideslistDF.csv')
AFGguides['channel'] = 'AFGguides'
UbisoftNorthAmerica = pd.read_csv('entertain/game/UbisoftNorthAmericalistDF.csv')
UbisoftNorthAmerica['channel'] = 'UbisoftNorthAmerica'
WhatCultureGaming = pd.read_csv('entertain/game/WhatCultureGaminglistDF.csv')
WhatCultureGaming['channel'] = 'WhatCultureGaming'
Polygon = pd.read_csv('entertain/game/PolygonlistDF.csv')
Polygon['channel'] = 'Polygon'

game = [PlayStation,Videogamedunkey,Boogie2988,Uberhaxornova,IGN,MKIceAndFire,GhostRobo,GameXplain,Chaos,FuriousFade,AFGguides,UbisoftNorthAmerica,WhatCultureGaming,Polygon]

Gordonramsay = pd.read_csv('entertain/Food/GordonramsaylistDF.csv')
Gordonramsay['channel'] = 'Gordonramsay'
Epicmealtime = pd.read_csv('entertain/Food/EpicmealtimelistDF.csv')
Epicmealtime['channel'] = 'Epicmealtime'
Maangchi = pd.read_csv('entertain/Food/MaangchilistDF.csv')
Maangchi['channel'] = 'Maangchi'
Foodwishes = pd.read_csv('entertain/Food/FoodwisheslistDF.csv')
Foodwishes['channel'] = 'Foodwishes'
pickuplimes = pd.read_csv('entertain/Food/pickuplimeslistDF.csv')
pickuplimes['channel'] = 'pickuplimes'
Gugafoods = pd.read_csv('entertain/Food/GugafoodslistDF.csv')
Gugafoods['channel'] = 'Gugafoods'
PreppyKitchen = pd.read_csv('entertain/Food/PreppyKitchenlistDF.csv')
PreppyKitchen['channel'] = 'PreppyKitchen'
Natashaskitchen = pd.read_csv('entertain/Food/NatashaskitchenlistDF.csv')
Natashaskitchen['channel'] = 'Natashaskitchen'
sortedfood = pd.read_csv('entertain/Food/sortedfoodlistDF.csv')
sortedfood['channel'] = 'sortedfood'
Justonecookbook = pd.read_csv('entertain/Food/JustonecookbooklistDF.csv')
Justonecookbook['channel'] = 'Justonecookbook'
Cheaplazyvegan = pd.read_csv('entertain/Food/CheaplazyveganlistDF.csv')
Cheaplazyvegan['channel'] = 'Cheaplazyvegan'
MathaStewart = pd.read_csv('entertain/Food/MathaStewartlistDF.csv')
MathaStewart['channel'] = 'MathaStewart'
Caribbeanpot = pd.read_csv('entertain/Food/CaribbeanpotlistDF.csv')
Caribbeanpot['channel'] = 'Caribbeanpot'
LauraInTheKitchen = pd.read_csv('entertain/Food/LauraInTheKitchenlistDF.csv')
LauraInTheKitchen['channel'] = 'LauraInTheKitchen'

food = [Gordonramsay,Epicmealtime,Maangchi,Foodwishes,pickuplimes,Gugafoods,PreppyKitchen,Natashaskitchen,sortedfood,Justonecookbook,Cheaplazyvegan,MathaStewart,Caribbeanpot,LauraInTheKitchen]

universalPictures = pd.read_csv('entertain/film/universalPictureslistDF.csv')
universalPictures['channel'] = 'universalPictures'
WaltDisney = pd.read_csv('entertain/film/WaltDisneylistDF.csv')
WaltDisney['channel'] = 'WaltDisney'
Deadmeat = pd.read_csv('entertain/film/DeadmeatlistDF.csv')
Deadmeat['channel'] = 'Deadmeat'
MovieclipTrailers = pd.read_csv('entertain/film/MovieclipTrailerslistDF.csv')
MovieclipTrailers['channel'] = 'MovieclipTrailers'
Screenrant = pd.read_csv('entertain/film/ScreenrantlistDF.csv')
Screenrant['channel'] = 'Screenrant'
MovieTheorists = pd.read_csv('entertain/film/MovieTheoristslistDF.csv')
MovieTheorists['channel'] = 'MovieTheorists'
TheThings = pd.read_csv('entertain/film/TheThingslistDF.csv')
TheThings['channel'] = 'TheThings'
Artspear = pd.read_csv('entertain/film/ArtspearlistDF.csv')
Artspear['channel'] = 'Artspear'
shupupCartoons = pd.read_csv('entertain/film/shupupCartoonslistDF.csv')
shupupCartoons['channel'] = 'shupupCartoons'
RapidTrailer = pd.read_csv('entertain/film/RapidTrailerlistDF.csv')
RapidTrailer['channel'] = 'RapidTrailer'
Filmonger = pd.read_csv('entertain/film/FilmongerlistDF.csv')
Filmonger['channel'] = 'Filmonger'
Smasher = pd.read_csv('entertain/film/SmasherlistDF.csv')
Smasher['channel'] = 'Smasher'
IsaacCarlson = pd.read_csv('entertain/film/IsaacCarlsonlistDF.csv')
IsaacCarlson['channel'] = 'IsaacCarlson'
FilmRise = pd.read_csv('entertain/film/FilmRiselistDF.csv')
FilmRise['channel'] = 'FilmRise'

film = [universalPictures,WaltDisney,Deadmeat,MovieclipTrailers,Screenrant,MovieTheorists,TheThings,Artspear,shupupCartoons,RapidTrailer,Filmonger,Smasher,IsaacCarlson,FilmRise]

AlexCosta = pd.read_csv('entertain/fashionbeauty/AlexCostalistDF.csv')
AlexCosta['channel'] = 'AlexCosta'
AlphaM = pd.read_csv('entertain/fashionbeauty/AlphaMlistDF.csv')
AlphaM['channel'] = 'AlphaM'
AlyssaForever = pd.read_csv('entertain/fashionbeauty/AlyssaForeverlistDF.csv')
AlyssaForever['channel'] = 'AlyssaForever'
CarliBybel = pd.read_csv('entertain/fashionbeauty/CarliBybellistDF.csv')
CarliBybel['channel'] = 'CarliBybel'
Evelina = pd.read_csv('entertain/fashionbeauty/EvelinalistDF.csv')
Evelina['channel'] = 'Evelina'
IngridNilsen = pd.read_csv('entertain/fashionbeauty/IngridNilsenlistDF.csv')
IngridNilsen['channel'] = 'IngridNilsen'
itsjudytime = pd.read_csv('entertain/fashionbeauty/itsjudytimelistDF.csv')
itsjudytime['channel'] = 'itsjudytime'
LauraLee = pd.read_csv('entertain/fashionbeauty/LauraLeelistDF.csv')
LauraLee['channel'] = 'LauraLee'
Madeyewlook = pd.read_csv('entertain/fashionbeauty/MadeyewlooklistDF.csv')
Madeyewlook['channel'] = 'Madeyewlook'
MichellePhan = pd.read_csv('entertain/fashionbeauty/MichellePhanlistDF.csv')
MichellePhan['channel'] = 'MichellePhan'
NikitaDragun = pd.read_csv('entertain/fashionbeauty/NikitaDragunlistDF.csv')
NikitaDragun['channel'] = 'NikitaDragun'
RealMenRealStyle = pd.read_csv('entertain/fashionbeauty/RealMenRealStylelistDF.csv')
RealMenRealStyle['channel'] = 'RealMenRealStyle'
Teachingmensfashion = pd.read_csv('entertain/fashionbeauty/TeachingmensfashionlistDF.csv')
Teachingmensfashion['channel'] = 'Teachingmensfashion'
Vogue = pd.read_csv('entertain/fashionbeauty/VoguelistDF.csv')
Vogue['channel'] = 'Vogue'

fashionbeauty = [AlexCosta,AlphaM,AlyssaForever,CarliBybel,Evelina,IngridNilsen,itsjudytime,LauraLee,Madeyewlook,MichellePhan,NikitaDragun,RealMenRealStyle,Teachingmensfashion,Vogue]

#%%
del NBCnews,ABCnews,CNN,MSNBC,CBSNews,WashintonPost,NowThisNews,Reuters,FoxNews,BloombergPolitics,Associatedpress,PBSNewsHour,TheWhiteHouse,CSPAN
del brailleSkateboarding,DingProductions,ESPN,NBA,NFL,NHL,Rebound,Ridechannel,ShaolinCenter,TheWorldofBoxing,Thefumble,TheMaxLife,tmzsports,XGames
del AlexCosta,AlphaM,AlyssaForever,CarliBybel,Evelina,IngridNilsen,itsjudytime,LauraLee,Madeyewlook,MichellePhan,NikitaDragun,RealMenRealStyle,Teachingmensfashion,Vogue
del universalPictures,WaltDisney,Deadmeat,MovieclipTrailers,Screenrant,MovieTheorists,TheThings,Artspear,shupupCartoons,RapidTrailer,Filmonger,Smasher,IsaacCarlson,FilmRise
del PlayStation,Videogamedunkey,Boogie2988,Uberhaxornova,IGN,MKIceAndFire,GhostRobo,GameXplain,Chaos,FuriousFade,AFGguides,UbisoftNorthAmerica,WhatCultureGaming,Polygon
del Gordonramsay,Epicmealtime,Maangchi,Foodwishes,pickuplimes,Gugafoods,PreppyKitchen,Natashaskitchen,sortedfood,Justonecookbook,Cheaplazyvegan,MathaStewart,Caribbeanpot,LauraInTheKitchen

#%%
news = pd.concat(news)
game = pd.concat(game)
food = pd.concat(food)
film = pd.concat(film)
sports = pd.concat(sports)
fashionbeauty = pd.concat(fashionbeauty)

#%%
ent = pd.concat([game,food,film,sports,fashionbeauty])

#%%
del game,food,film,sports,fashionbeauty

#%%
ent = ent[["title"]]

#%%
news['poli'] = 1
ent['poli'] = 0

#%%
news_temp = news.sample(n = 30000)
ent_temp = ent.sample(n = 30000)

#%%
train_model = pd.concat([news_temp,ent_temp])

#%%
train_model = train_model.reset_index()

#%%
random.seed(10)

documents = []

stemmer = WordNetLemmatizer()

for i in range(len(train_model['title'])):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(train_model['title'][i]))
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    # Converting to Lowercase
    document = document.lower()
    # Lemmatization
    document = document.split()
    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    documents.append(document)


#%%
from sklearn.feature_extraction.text import TfidfVectorizer
tfidfconverter = TfidfVectorizer(max_features=5000, min_df=50, max_df=0.6, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(documents).toarray()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, train_model['poli'], test_size=0.3, random_state=0)

#%%
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

#%%
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

#%%
'''[[8618  432]
 [ 360 8590]]
              precision    recall  f1-score   support
           0       0.96      0.95      0.96      9050
           1       0.95      0.96      0.96      8950
    accuracy                           0.96     18000
   macro avg       0.96      0.96      0.96     18000
weighted avg       0.96      0.96      0.96     18000
0.956
'''
#%%
with open('poli_classifier', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)

#%%
with open('poli_tfidfconverter', 'wb') as picklefile:
    pickle.dump(tfidfconverter,picklefile)

#%%
file = open("poli_classifier",'rb')
classifier = pickle.load(file)
file.close()
file = open("poli_tfidfconverter",'rb')
tfidfconverter = pickle.load(file)
file.close()

#%%
def get_pred_poli(title,model):
    documents = []
    stemmer = WordNetLemmatizer()
    for i in range(len(title)):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(title[i]))
        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        # Converting to Lowercase
        document = document.lower()
        # Lemmatization
        document = document.split()
        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)
        documents.append(document)
    #tfidfconverter = TfidfVectorizer(max_features=6000, min_df=5, max_df=0.5, stop_words=stopwords.words('english'))
    X = tfidfconverter.transform(documents).toarray()
    return model.predict(X)
#%%
recommend = []
account = [5,6,7,8,9,10]
interest = [1,2,3]
percent = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #
stage = [0,1,2,3,4,5,6,7,8] #

filename = []
for acc in account:
    for inte in interest:
        for per in percent:
            for sta in stage:
                temp_file = 'recommend-round2-machine1/recom_' + str(acc) +'_' + str(inte) + '_' + str(per) + '_' + str(sta) + '.csv'
                filename.append(temp_file)

for i in range(len(filename)):
    print(i)
    temp_file = pd.read_csv(filename[i])
    tempPred = get_pred_poli(temp_file['title'], classifier)
    temp_file['predPoli'] = tempPred
    recommend.append(temp_file)

#%%
recommend = pd.concat(recommend)
recommend = recommend.reset_index()
#%%
temp = recommend.groupby(["account","interest","percent"])["predPoli"].mean().to_frame(name = 'averagePoli').reset_index()


#%%

Bypercent = recommend.groupby(["percent"])["predPoli"].mean().to_frame(name = 'averagePoli').reset_index()

#%%
ByInterest = temp.groupby(["percent","interest"])["clean_poli"].mean().to_frame(name = 'averagePoli').reset_index()
#%%
baseline = []


#%%
account = [5,6,7,8,9,10]#
percent = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
interest = [1,2,3]


for acc in account:
    print(acc)
    for inte in interest:
        print(inte)
        for per in percent:
            try:
                temp_file = 'baseline-round2-machine1/baseline_' + str(acc) + '_' + str(inte) + '_' + str(per) + '.csv'
                temp_file = pd.read_csv(temp_file)
                temp_file['account'] = acc
                temp_file['interest'] = inte
                temp_file['percent'] = per
                tempPred = get_pred_poli(temp_file['title'], classifier)
                temp_file['predPoli_baseline'] = tempPred
                baseline.append(temp_file)
            except:
                print('baseline/baseline_' + str(acc) + '_' + str(inte) + '_' + str(per) + '.csv')


#%%
baseline = pd.concat(baseline)
baseline = baseline.reset_index()


#%%
temp_baseline = baseline.groupby(["account","interest","percent"])["predPoli_baseline"].mean().to_frame(name = 'averagePoli_baseline').reset_index()
temp = temp.merge(temp_baseline, how='left', on=['account','interest','percent'])
temp['clean_poli'] = temp['averagePoli'] - temp['averagePoli_baseline']

#%%
recommend.to_csv('Recommend_preded.csv')
baseline.to_csv('Baseline_preded.csv')



#%%
account = [1,2,3,4,5,6,7,8,9,10]#
percent = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
interest = [1,2,3]

watchfile = []

for acc in account:
    print(acc)
    for inte in interest:
        print(inte)
        for per in percent:
            try:
                temp_file = '/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/watchlist/' + str(acc) + "_" + str(inte) + '_' + str(per) + '.csv'
                temp_file = pd.read_csv(temp_file)
                temp_file['account'] = acc
                temp_file['interest'] = inte
                temp_file['percent'] = per
                tempPred = get_pred_poli(temp_file['title'], classifier)
                temp_file['predPoli_baseline'] = tempPred
                watchfile.append(temp_file)
            except:
                print('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/watchlist/' + str(acc) + "_" + str(inte) + '_' + str(per) + '.csv')

#%%
watchfile = pd.concat(watchfile)
watchfile = watchfile.reset_index()

#%%
temp_watchfile = watchfile.groupby(["account","interest","percent"])["predPoli_baseline"].mean().to_frame(name = 'averagePoli_predhist').reset_index()
temp = temp.merge(temp_watchfile, how='left', on=['account','interest','percent'])
#temp['clean_poli'] = temp['averagePoli'] - temp['averagePoli_baseline']

#%%
baseline_sample = baseline
baseline_sample = baseline_sample.drop_duplicates(subset=['title'])
baseline_sample = baseline_sample.sample(n = 10000)
baseline_sample.to_csv('baseline_sample_audit.csv')


#%%
recommend_sample = recommend
recommend_sample = recommend_sample.drop_duplicates(subset=['title'])
recommend_sample = recommend_sample.sample(n = 10000)

#%%
baseline.to_csv('baseline_withCode.csv')

#%%

#%%
#recommend = []
account = [1,2,3,4]
interest = [1,2,3]
percent = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #
stage = [0,1,2,3,4,5,6,7,8] #

filename = []
for acc in account:
    for inte in interest:
        for per in percent:
            for sta in stage:
                temp_file = 'recommend-round2-machine3/recom_' + str(acc) +'_' + str(inte) + '_' + str(per) + '_' + str(sta) + '.csv'
                filename.append(temp_file)

for i in range(len(filename)):
    print(i)
    temp_file = pd.read_csv(filename[i])
    #tempPred = get_pred_poli(temp_file['title'], classifier)
    #temp_file['predPoli'] = tempPred
    recommend.append(temp_file)

#%%
recommend = pd.concat(recommend)
recommend = recommend.reset_index()

#%%
recommend_cleaned = recommend[["title", "url"]]
baseline_cleaned = baseline[["title", "url"]]

#%%
baseline_remove_dup = baseline.drop_duplicates(subset=['url'])
#%%
cleaned = pd.concat([recommend_cleaned,baseline_cleaned])
cleaned = cleaned.drop_duplicates(subset=['url'])


#%%
## Food classifier

game = game[["title", "url",'view','label','channel']]
food = food[["title", "url",'view','label','channel']]
film = film[["title", "url",'view','label','channel']]
sports = sports[["title", "url",'view','label','channel']]
fashionbeauty = fashionbeauty[["title", "url",'view','label','channel']]
nonfood = pd.concat([game,news,film,sports,fashionbeauty])

food['Food'] = 1
nonfood['Food'] = 0


food_temp = food.sample(n = 13264)
food_temp = food_temp[["title", "Food"]]
nonfood_temp = nonfood.sample(n = 13264)
nonfood_temp = nonfood_temp[["title", "Food"]]
food_train = pd.read_csv('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/training/FoodTraining.csv')
train_model = pd.concat([food_temp,nonfood_temp,food_train])

train_model = train_model.reset_index()
#%%
random.seed(10)

documents = []

stemmer = WordNetLemmatizer()

for i in range(len(train_model['title'])):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(train_model['title'][i]))
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    # Converting to Lowercase
    document = document.lower()
    # Lemmatization
    document = document.split()
    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    documents.append(document)


from sklearn.feature_extraction.text import TfidfVectorizer
tfidfconverter = TfidfVectorizer(max_features=5000, min_df=50, max_df=0.6, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(documents).toarray()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, train_model['Food'], test_size=0.0001, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

with open('food_classifier', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)

with open('food_tfidfconverter', 'wb') as picklefile:
    pickle.dump(tfidfconverter,picklefile)

#%%
food_recommend_audit = cleaned.sample(n = 5000)
food_recommend_audit = food_recommend_audit.reset_index()
tempPred = get_pred_poli(food_recommend_audit['title'], classifier)
food_recommend_audit['code'] = tempPred
food_recommend_audit = food_recommend_audit.loc[food_recommend_audit['code'] == 1]

food_recommend_audit.to_csv('food_recommend_audit_add2.csv')

#%%

## game classifier

game = game[["title", "url",'view','label','channel']]
food = food[["title", "url",'view','label','channel']]
film = film[["title", "url",'view','label','channel']]
sports = sports[["title", "url",'view','label','channel']]
fashionbeauty = fashionbeauty[["title", "url",'view','label','channel']]
nongame = pd.concat([food,news,film,sports,fashionbeauty])

game['code'] = 1
nongame['code'] = 0


game_temp = game.sample(n = 5000)
nongame_temp = nongame.sample(n = 5000)


train_model = pd.concat([game_temp,nongame_temp])

train_model = train_model.reset_index()

random.seed(10)

documents = []

stemmer = WordNetLemmatizer()

for i in range(len(train_model['title'])):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(train_model['title'][i]))
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    # Converting to Lowercase
    document = document.lower()
    # Lemmatization
    document = document.split()
    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    documents.append(document)


from sklearn.feature_extraction.text import TfidfVectorizer
tfidfconverter = TfidfVectorizer(max_features=5000, min_df=50, max_df=0.6, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(documents).toarray()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, train_model['code'], test_size=0.3, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

with open('game_classifier', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)

with open('game_tfidfconverter', 'wb') as picklefile:
    pickle.dump(tfidfconverter,picklefile)

cleaned_audit = cleaned.sample(n = 2000)
cleaned_audit = cleaned_audit.reset_index()
tempPred = get_pred_poli(cleaned_audit['title'], classifier)
cleaned_audit['code'] = tempPred
cleaned_audit = cleaned_audit.loc[cleaned_audit['code'] == 1]

cleaned_audit.to_csv('game_recommend_audit.csv')

#%%

## fashionbeauty classifier

game = game[["title", "url",'view','label','channel']]
food = food[["title", "url",'view','label','channel']]
film = film[["title", "url",'view','label','channel']]
sports = sports[["title", "url",'view','label','channel']]
fashionbeauty = fashionbeauty[["title", "url",'view','label','channel']]
nonfashionbeauty = pd.concat([food,news,film,sports,game])

fashionbeauty['code'] = 1
nonfashionbeauty['code'] = 0


fashionbeauty_temp = fashionbeauty.sample(n = 5000)
nonfashionbeauty_temp = nonfashionbeauty.sample(n = 5000)


train_model = pd.concat([fashionbeauty_temp,nonfashionbeauty_temp])

train_model = train_model.reset_index()

random.seed(10)

documents = []

stemmer = WordNetLemmatizer()

for i in range(len(train_model['title'])):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(train_model['title'][i]))
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    # Converting to Lowercase
    document = document.lower()
    # Lemmatization
    document = document.split()
    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    documents.append(document)


from sklearn.feature_extraction.text import TfidfVectorizer
tfidfconverter = TfidfVectorizer(max_features=5000, min_df=50, max_df=0.6, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(documents).toarray()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, train_model['code'], test_size=0.3, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

with open('fashionbeauty_classifier', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)

with open('fashionbeauty_tfidfconverter', 'wb') as picklefile:
    pickle.dump(tfidfconverter,picklefile)

cleaned_audit = cleaned.sample(n = 2000)
cleaned_audit = cleaned_audit.reset_index()
tempPred = get_pred_poli(cleaned_audit['title'], classifier)
cleaned_audit['code'] = tempPred
cleaned_audit = cleaned_audit.loc[cleaned_audit['code'] == 1]

cleaned_audit.to_csv('fashionbeauty_recommend_audit.csv')


#%%

## film classifier

game = game[["title", "url",'view','label','channel']]
food = food[["title", "url",'view','label','channel']]
film = film[["title", "url",'view','label','channel']]
sports = sports[["title", "url",'view','label','channel']]
fashionbeauty = fashionbeauty[["title", "url",'view','label','channel']]
nonfilm = pd.concat([food,news,fashionbeauty,sports,game])

film['code'] = 1
nonfilm['code'] = 0


film_temp = film.sample(n = 5000)
nonfilm_temp = nonfilm.sample(n = 5000)


train_model = pd.concat([film_temp,nonfilm_temp])

train_model = train_model.reset_index()

random.seed(10)

documents = []

stemmer = WordNetLemmatizer()

for i in range(len(train_model['title'])):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(train_model['title'][i]))
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    # Converting to Lowercase
    document = document.lower()
    # Lemmatization
    document = document.split()
    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    documents.append(document)


from sklearn.feature_extraction.text import TfidfVectorizer
tfidfconverter = TfidfVectorizer(max_features=5000, min_df=50, max_df=0.6, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(documents).toarray()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, train_model['code'], test_size=0.3, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

with open('film_classifier', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)

with open('film_tfidfconverter', 'wb') as picklefile:
    pickle.dump(tfidfconverter,picklefile)

cleaned_audit = cleaned.sample(n = 2000)
cleaned_audit = cleaned_audit.reset_index()
tempPred = get_pred_poli(cleaned_audit['title'], classifier)
cleaned_audit['code'] = tempPred
cleaned_audit = cleaned_audit.loc[cleaned_audit['code'] == 1]

cleaned_audit.to_csv('film_recommend_audit.csv')

#%%
## sports classifier

game = game[["title", "url",'view','label','channel']]
food = food[["title", "url",'view','label','channel']]
film = film[["title", "url",'view','label','channel']]
sports = sports[["title", "url",'view','label','channel']]
fashionbeauty = fashionbeauty[["title", "url",'view','label','channel']]
nonsports = pd.concat([food,news,fashionbeauty,film,game])

sports['code'] = 1
nonsports['code'] = 0


sports_temp = sports.sample(n = 20348)
sports_temp = sports_temp[["title", "code"]]
nonsports_temp = nonsports.sample(n = 20348)
nonsports_temp = nonsports_temp[["title", "code"]]
sports_train = pd.read_csv('/Users/wuxiaohan/Desktop/ucsd/Research/SeminarPaper/YouTubeBot/training/SportsTraining.csv')
train_model = pd.concat([sports_temp,nonfood_temp,food_train])

train_model = pd.concat([sports_temp,nonsports_temp,sports_train])

train_model = train_model.reset_index()
#%%
random.seed(10)

documents = []

stemmer = WordNetLemmatizer()

for i in range(len(train_model['title'])):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(train_model['title'][i]))
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    # Converting to Lowercase
    document = document.lower()
    # Lemmatization
    document = document.split()
    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    documents.append(document)


from sklearn.feature_extraction.text import TfidfVectorizer
tfidfconverter = TfidfVectorizer(max_features=5000, min_df=50, max_df=0.6, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(documents).toarray()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, train_model['code'], test_size=0.0001, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

with open('sports_classifier', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)

with open('sports_tfidfconverter', 'wb') as picklefile:
    pickle.dump(tfidfconverter,picklefile)
#%%
cleaned_audit = cleaned.sample(n = 2000)
cleaned_audit = cleaned_audit.reset_index()
tempPred = get_pred_poli(cleaned_audit['title'], classifier)
cleaned_audit['code'] = tempPred
cleaned_audit = cleaned_audit.loc[cleaned_audit['code'] == 1]

cleaned_audit.to_csv('sports_recommend_audit.csv')

#%%
#total classifier
recommend_coded = pd.read_csv('recommend_random_audit.csv')

recommend_coded = recommend_coded.reset_index()

recommend_coded.loc[(recommend_coded.code == 2),'code'] = 1
recommend_coded.loc[(recommend_coded.code == 3),'code'] = 1
recommend_coded.loc[(recommend_coded.code == 9),'code'] = 0

train_model = recommend_coded
train_model.loc[(train_model.code != 8),'code']=0
#%%

train_model = pd.read_csv('../YouTubeBot/training/NewsTraining.csv')
#%%
entertain = ent[["title"]]
news1 = news[['title']]
#%%
news1['code'] = 1
entertain['code'] = 0

#%%
news_temp = news1.sample(n = 30000)
entertain_temp = entertain.sample(n = 30000)

#%%
train_model = pd.concat([train_model,news_temp,entertain_temp])

#%%
train_model = train_model.reset_index()

documents = []

stemmer = WordNetLemmatizer()

for i in range(len(train_model['title'])):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(train_model['title'][i]))
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    # Converting to Lowercase
    document = document.lower()
    # Lemmatization
    document = document.split()
    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    documents.append(document)


from sklearn.feature_extraction.text import TfidfVectorizer
tfidfconverter = TfidfVectorizer(max_features=10000, min_df = 50, max_df=0.6, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(documents).toarray()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, train_model['code'], test_size=0.2, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))


#%%
with open('poli_classifier', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)
with open('poli_tfidfconverter', 'wb') as picklefile:
    pickle.dump(tfidfconverter,picklefile)

'''
[[8193  389]
 [ 474 5720]]
              precision    recall  f1-score   support
           0       0.95      0.95      0.95      8582
           1       0.94      0.92      0.93      6194
    accuracy                           0.94     14776
   macro avg       0.94      0.94      0.94     14776
weighted avg       0.94      0.94      0.94     14776
0.9415944775311316
'''



