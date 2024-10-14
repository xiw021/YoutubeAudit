#%%
import pandas as pd
import random
import numpy as np
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
# Account 1 Female Interest: Food,BeautyFashion,Film
random.seed(1)
interest1 = food
interest2 = fashionbeauty
interest3 = film

#%%
#  6 news channels VS 6 entertain channels
# interest 1
news_sample = random.sample(news, 6)
for news_item in news_sample: # CNN BloombergPolitics ABCnews CBSNews PBSNewsHour Reuters
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 6)
for ent in sample1: # Caribbeanpot Natashaskitchen LauraInTheKitchen Cheaplazyvegan PreppyKitchen Foodwishes
    print(ent['channel'][0])

#%%
newswatchlist = []
for news_channel in news_sample:
    temp = news_channel.sample(n=30)
    if len(newswatchlist) == 0:
        newswatchlist = temp
    else:
        newswatchlist = pd.concat([newswatchlist, temp])
## shuffle
newswatchlist = newswatchlist.sample(frac=1)
newswatchlist = newswatchlist.reset_index()
entwatchlist = []
for ent_channel in sample1:
    temp = ent_channel.sample(n=30)
    if len(entwatchlist) == 0:
        entwatchlist = temp
    else:
        entwatchlist = pd.concat([entwatchlist, temp])
## shuffle
entwatchlist = entwatchlist.sample(frac=1)
entwatchlist = entwatchlist.reset_index()
## generate watch list
watchlist_url = []
watchlist_title = []
pd_watchlist = []
percents = (0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)
for percent in percents:
    print(percent)
    newswatchlist = []
    for news_channel in news_sample:
        temp = news_channel.sample(n=30)
        if len(newswatchlist) == 0:
            newswatchlist = temp
        else:
            newswatchlist = pd.concat([newswatchlist, temp])
    ## shuffle
    newswatchlist = newswatchlist.sample(frac=1)
    newswatchlist = newswatchlist.reset_index()
    entwatchlist = []
    for ent_channel in sample1:
        temp = ent_channel.sample(n=30)
        if len(entwatchlist) == 0:
            entwatchlist = temp
        else:
            entwatchlist = pd.concat([entwatchlist, temp])
    ## shuffle
    entwatchlist = entwatchlist.sample(frac=1)
    entwatchlist = entwatchlist.reset_index()
    ## generate watch list
    pd_watchlist = []
    for i in range(9):
        #print(int(i * percent * 20),(i + 1) * percent * 20)
        #print(int(i * (1 - percent) * 20), (i + 1) * (1 - percent) * 20)
        #print(i)
        watchlist_url = []
        watchlist_title = []
        watchlist_url = watchlist_url + list(newswatchlist[int(i*percent*20):int((i+1)*percent*20)]['url'])
        watchlist_title = watchlist_title + list(newswatchlist[int(i * percent * 20):int((i + 1) * percent * 20)]['title'])
        watchlist_url = watchlist_url + list(entwatchlist[int(i * (1-percent) * 20): int((i + 1) * (1-percent) * 20)]['url'])
        watchlist_title = watchlist_title + list(entwatchlist[int(i * (1 - percent) * 20): int((i + 1) * (1 - percent) * 20)]['title'])
        print(len(watchlist_url),len(watchlist_title))
        temp = {'url': watchlist_url, 'title': watchlist_title}
        temp = pd.DataFrame(data=temp)
        temp = temp.sample(frac=1)
        if len(pd_watchlist) == 0:
            pd_watchlist = temp
        else:
            pd_watchlist = pd.concat([pd_watchlist, temp])
    pd_watchlist['percent'] = percent
    pd_watchlist['interest'] = 3
    pd_watchlist['account'] = 10
    filename = '10_'+'3_'+str(percent) + '.csv'
    #pd_watchlist.to_csv(filename)

#%%
random.seed(1)
interest1 = food
interest2 = fashionbeauty
interest3 = film
# interest 2
news_sample = random.sample(news, 6)
for news_item in news_sample: # CNN BloombergPolitics ABCnews CBSNews PBSNewsHour Reuters
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 3)
sample2 = random.sample(interest2, 3)
sample1 = sample1 + sample2
for ent in sample1: # Caribbeanpot Natashaskitchen LauraInTheKitchen NikitaDragun itsjudytime CarliBybel
    print(ent['channel'][0])

#%%
# interest 3
random.seed(1)
interest1 = food
interest2 = fashionbeauty
interest3 = film
news_sample = random.sample(news, 6)
for news_item in news_sample: # CNN BloombergPolitics ABCnews CBSNews PBSNewsHour Reuters
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 2)
sample2 = random.sample(interest2, 2)
sample3 = random.sample(interest3, 2)
sample1 = sample1 + sample2 + sample3
for ent in sample1: # Caribbeanpot Natashaskitchen LauraLee NikitaDragun TheThings IsaacCarlson
    print(ent['channel'][0])
#%%
# Account 2 Female Interest: BeautyFashion, Film, game,
random.seed(2)
#  6 news channels VS 6 entertain channels
# interest 1
interest1 = fashionbeauty
interest2 = film
interest3 = game

#%%
# interest 1
news_sample = random.sample(news, 6) # CSPAN NBCnews ABCnews PBSNewsHour WashintonPost CNN
for news_item in news_sample:
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 6) # RealMenRealStyle Teachingmensfashion NikitaDragun Evelina Vogue CarliBybel
for ent in sample1:
    print(ent['channel'][0])

#%%
random.seed(2)
#  6 news channels VS 6 entertain channels
interest1 = fashionbeauty
interest2 = film
interest3 = game
# interest 2
news_sample = random.sample(news, 6)
for news_item in news_sample: # CSPAN NBCnews ABCnews PBSNewsHour WashintonPost CNN
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 3)
sample2 = random.sample(interest2, 3)
sample1 = sample1 + sample2
for ent in sample1: # RealMenRealStyle Teachingmensfashion NikitaDragun FilmRise Screenrant IsaacCarlson
    print(ent['channel'][0])

#%%
random.seed(2)
#  6 news channels VS 6 entertain channels
interest1 = fashionbeauty
interest2 = film
interest3 = game
news_sample = random.sample(news, 6)
for news_item in news_sample: # CSPAN NBCnews ABCnews PBSNewsHour WashintonPost CNN
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 2)
sample2 = random.sample(interest2, 2)
sample3 = random.sample(interest3, 2)
sample1 = sample1 + sample2 + sample3
for ent in sample1: # RealMenRealStyle Teachingmensfashion Filmonger Screenrant IGN FuriousFade
    print(ent['channel'][0])
#%%
# Account 3 Female Interest: Film,Food,sports
random.seed(3)
interest1 = film
interest2 = food
interest3 = sports
#  6 news channels VS 6 entertain channels
# interest 1
news_sample = random.sample(news, 6) # MSNBC BloombergPolitics FoxNews CNN WashintonPost Reuters
for news_item in news_sample:
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 6) # Filmonger RapidTrailer WaltDisney IsaacCarlson universalPictures Artspear
for ent in sample1:
    print(ent['channel'][0])
#%%
random.seed(3)
interest1 = film
interest2 = food
interest3 = sports
# interest 2
news_sample = random.sample(news, 6)
for news_item in news_sample: # MSNBC BloombergPolitics FoxNews CNN WashintonPost Reuters
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 3)
sample2 = random.sample(interest2, 3)
sample1 = sample1 + sample2
for ent in sample1: # Filmonger RapidTrailer WaltDisney Justonecookbook Gordonramsay Natashaskitchen
    print(ent['channel'][0])
#%%
random.seed(3)
interest1 = film
interest2 = food
interest3 = sports
news_sample = random.sample(news, 6)
for news_item in news_sample: # MSNBC BloombergPolitics FoxNews CNN WashintonPost Reuters
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 2)
sample2 = random.sample(interest2, 2)
sample3 = random.sample(interest3, 2)
sample1 = sample1 + sample2 + sample3
for ent in sample1: # Filmonger RapidTrailer Epicmealtime Justonecookbook brailleSkateboarding Ridechannel
    print(ent['channel'][0])
#%%
# Account 4 Female Interest: Game, Sports, food
random.seed(4)
interest1 = game
interest2 = sports
interest3 = food

#%%
#  6 news channels VS 6 entertain channels
# interest 1
news_sample = random.sample(news, 6) # MSNBC CBSNews ABCnews NowThisNews Reuters CNN
for news_item in news_sample:
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 6) # Videogamedunkey Polygon PlayStation GhostRobo Chaos IGN
for ent in sample1:
    print(ent['channel'][0])
#%%
random.seed(4)
interest1 = game
interest2 = sports
interest3 = food
# interest 2
news_sample = random.sample(news, 6)
for news_item in news_sample: # MSNBC CBSNews ABCnews NowThisNews Reuters CNN
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 3)
sample2 = random.sample(interest2, 3)
sample1 = sample1 + sample2
for ent in sample1: # Videogamedunkey Polygon PlayStation Rebound ShaolinCenter NFL
    print(ent['channel'][0])

#%%
random.seed(4)
interest1 = game
interest2 = sports
interest3 = food
news_sample = random.sample(news, 6)
for news_item in news_sample: # MSNBC CBSNews ABCnews NowThisNews Reuters CNN
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 2)
sample2 = random.sample(interest2, 2)
sample3 = random.sample(interest3, 2)
sample1 = sample1 + sample2 + sample3
for ent in sample1: # Videogamedunkey Polygon brailleSkateboarding Rebound sortedfood pickuplimes
    print(ent['channel'][0])

#%%
# Account 5 Female Interest: Sports,Game,BeautyFashion
random.seed(5)
interest1 = sports
interest2 = game
interest3 = fashionbeauty

#%%
#  6 news channels VS 6 entertain channels
# interest 1
news_sample = random.sample(news, 6) # BloombergPolitics CBSNews PBSNewsHour WashintonPost FoxNews NBCnews
for news_item in news_sample:
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 6) # XGames Ridechannel NBA Thefumble brailleSkateboarding ESPN
for ent in sample1:
    print(ent['channel'][0])

#%%
random.seed(5)
interest1 = sports
interest2 = game
interest3 = fashionbeauty
# interest 2
news_sample = random.sample(news, 6)
for news_item in news_sample: # BloombergPolitics CBSNews PBSNewsHour WashintonPost FoxNews NBCnews
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 3)
sample2 = random.sample(interest2, 3)
sample1 = sample1 + sample2
for ent in sample1: # XGames Ridechannel NBA AFGguides PlayStation Boogie2988
    print(ent['channel'][0])

#%%
random.seed(5)
interest1 = sports
interest2 = game
interest3 = fashionbeauty
news_sample = random.sample(news, 6)
for news_item in news_sample: # BloombergPolitics CBSNews PBSNewsHour WashintonPost FoxNews NBCnews
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 2)
sample2 = random.sample(interest2, 2)
sample3 = random.sample(interest3, 2)
sample1 = sample1 + sample2 + sample3
for ent in sample1: # XGames Ridechannel WhatCultureGaming Uberhaxornova NikitaDragun AlexCosta
    print(ent['channel'][0])
#%%
# Account 6 Male Interest: BeautyFashion,Sports,Game
random.seed(6)
interest1 = fashionbeauty
interest2 = sports
interest3 = game

#%%
#  6 news channels VS 6 entertain channels
# interest 1
news_sample = random.sample(news, 6) #TheWhiteHouse BloombergPolitics ABCnews Reuters CBSNews NBCnews
for news_item in news_sample:
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 6) # AlexCosta AlyssaForever NikitaDragun MichellePhan LauraLee IngridNilsen
for ent in sample1:
    print(ent['channel'][0])

#%%
random.seed(6)
interest1 = fashionbeauty
interest2 = sports
interest3 = game
# interest 2
news_sample = random.sample(news, 6)
for news_item in news_sample: # TheWhiteHouse BloombergPolitics ABCnews Reuters CBSNews NBCnews
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 3)
sample2 = random.sample(interest2, 3)
sample1 = sample1 + sample2
for ent in sample1: # AlexCosta AlyssaForever NikitaDragun TheWorldofBoxing Ridechannel TheMaxLife
    print(ent['channel'][0])

#%%
random.seed(6)
interest1 = fashionbeauty
interest2 = sports
interest3 = game
news_sample = random.sample(news, 6)
for news_item in news_sample: # TheWhiteHouse BloombergPolitics ABCnews Reuters CBSNews NBCnews
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 2)
sample2 = random.sample(interest2, 2)
sample3 = random.sample(interest3, 2)
sample1 = sample1 + sample2 + sample3
for ent in sample1: # AlexCosta AlyssaForever Thefumble TheWorldofBoxing GameXplain WhatCultureGaming
    print(ent['channel'][0])
#%%
# Account 7 Male Interest: Food, BeautyFashion,Film
random.seed(7)
interest1 = food
interest2 = fashionbeauty
interest3 = film

#  6 news channels VS 6 entertain channels
# interest 1
news_sample = random.sample(news, 6) #WashintonPost CNN NowThisNews Associatedpress NBCnews ABCnews
for news_item in news_sample:
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 6) #LauraInTheKitchen sortedfood Epicmealtime Gugafoods Justonecookbook Gordonramsay
for ent in sample1:
    print(ent['channel'][0])

#%%
random.seed(7)
interest1 = food
interest2 = fashionbeauty
interest3 = film
# interest 2
news_sample = random.sample(news, 6)
for news_item in news_sample: # WashintonPost CNN NowThisNews Associatedpress NBCnews ABCnews
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 3)
sample2 = random.sample(interest2, 3)
sample1 = sample1 + sample2
for ent in sample1: # LauraInTheKitchen sortedfood Epicmealtime IngridNilsen MichellePhan AlexCosta
    print(ent['channel'][0])

#%%
random.seed(7)
interest1 = food
interest2 = fashionbeauty
interest3 = film
news_sample = random.sample(news, 6)
for news_item in news_sample: # WashintonPost CNN NowThisNews Associatedpress NBCnews ABCnews
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 2)
sample2 = random.sample(interest2, 2)
sample3 = random.sample(interest3, 2)
sample1 = sample1 + sample2 + sample3
for ent in sample1: # LauraInTheKitchen sortedfood AlphaM IngridNilsen RapidTrailer universalPictures
    print(ent['channel'][0])

#%%
# Account 8 Male Interest: Film, Food, sports,
random.seed(8)
interest1 = film
interest2 = food
interest3 = sports
#  6 news channels VS 6 entertain channels
# interest 1
news_sample = random.sample(news, 6) #MSNBC WashintonPost NowThisNews CNN CSPAN NBCnews
for news_item in news_sample:
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 6) # WaltDisney Deadmeat MovieclipTrailers shupupCartoons Smasher TheThings
for ent in sample1:
    print(ent['channel'][0])

#%%
random.seed(8)
interest1 = film
interest2 = food
interest3 = sports
# interest 2
news_sample = random.sample(news, 6)
for news_item in news_sample: # MSNBC WashintonPost NowThisNews CNN CSPAN NBCnews
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 3)
sample2 = random.sample(interest2, 3)
sample1 = sample1 + sample2
for ent in sample1: # WaltDisney Deadmeat MovieclipTrailers Caribbeanpot sortedfood Foodwishes
    print(ent['channel'][0])
#%%
random.seed(8)
interest1 = film
interest2 = food
interest3 = sports
news_sample = random.sample(news, 6)
for news_item in news_sample:  # MSNBC WashintonPost NowThisNews CNN CSPAN NBCnews
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 2)
sample2 = random.sample(interest2, 2)
sample3 = random.sample(interest3, 2)
sample1 = sample1 + sample2 + sample3
for ent in sample1: # WaltDisney Deadmeat Foodwishes Caribbeanpot ShaolinCenter NBA
    print(ent['channel'][0])
#%%
# Account 9 Male Interest: Game, Film, BeautyFashion,
random.seed(9)
interest1 = game
interest2 = film
interest3 = fashionbeauty
#  6 news channels VS 6 entertain channels
# interest 1
news_sample = random.sample(news, 6) #Reuters BloombergPolitics WashintonPost CBSNews CNN TheWhiteHouse
for news_item in news_sample:
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 6) # Polygon AFGguides PlayStation MKIceAndFire Chaos GameXplain
for ent in sample1:
    print(ent['channel'][0])


#%%
random.seed(9)
interest1 = game
interest2 = film
interest3 = fashionbeauty
# interest 2
news_sample = random.sample(news, 6)
for news_item in news_sample: # Reuters BloombergPolitics WashintonPost CBSNews CNN TheWhiteHouse
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 3)
sample2 = random.sample(interest2, 3)
sample1 = sample1 + sample2
for ent in sample1: # Polygon AFGguides PlayStation MovieTheorists shupupCartoons Artspear
    print(ent['channel'][0])

#%%
random.seed(9)
interest1 = game
interest2 = film
interest3 = fashionbeauty
news_sample = random.sample(news, 6)
for news_item in news_sample:  # Reuters BloombergPolitics WashintonPost CBSNews CNN TheWhiteHouse
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 2)
sample2 = random.sample(interest2, 2)
sample3 = random.sample(interest3, 2)
sample1 = sample1 + sample2 + sample3
for ent in sample1: #Polygon AFGguides universalPictures MovieTheorists Madeyewlook LauraLee
    print(ent['channel'][0])
#%%
# Account 10 Male Interest: Sports, game, food,
random.seed(10)
interest1 = sports
interest2 = game
interest3 = food
#  6 news channels VS 6 entertain channels
# interest 1
news_sample = random.sample(news, 6) #BloombergPolitics NBCnews NowThisNews Reuters CSPAN TheWhiteHouse
for news_item in news_sample:
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 6) # NBA Ridechannel tmzsports NFL ESPN brailleSkateboarding

for ent in sample1:
    print(ent['channel'][0])

#%%
random.seed(10)
interest1 = sports
interest2 = game
interest3 = food
# interest 2
news_sample = random.sample(news, 6)
for news_item in news_sample: # BloombergPolitics NBCnews NowThisNews Reuters CSPAN TheWhiteHouse
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 3)
sample2 = random.sample(interest2, 3)
sample1 = sample1 + sample2
for ent in sample1: # NBA Ridechannel tmzsports Polygon IGN AFGguides
    print(ent['channel'][0])
#%%
random.seed(10)
interest1 = sports
interest2 = game
interest3 = food
news_sample = random.sample(news, 6)
for news_item in news_sample:  # BloombergPolitics NBCnews NowThisNews Reuters CSPAN TheWhiteHouse
    print(news_item['channel'][0])
sample1 = random.sample(interest1, 2)
sample2 = random.sample(interest2, 2)
sample3 = random.sample(interest3, 2)
sample1 = sample1 + sample2 + sample3
for ent in sample1: # NBA Ridechannel Polygon GameXplain LauraInTheKitchen pickuplimes
    print(ent['channel'][0])