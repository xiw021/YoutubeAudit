import pandas as pd
import re
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
film = pd.concat(film)
food = pd.concat(food)
game = pd.concat(game)
news = pd.concat(news)
fashionbeauty = pd.concat(fashionbeauty)
sports = pd.concat(sports)

#%%
food = food[['title','url','view','label','channel']]
game = game[['title','url','view','label','channel']]
film = film[['title','url','view','label','channel']]
fashionbeauty = fashionbeauty[['title','url','view','label','channel']]
sports = sports[['title','url','view','label','channel']]
#%%
all = pd.concat([film,food,game,news,fashionbeauty,sports])
#%%
del fashionbeauty,film,food,news,sports,game

#%%
Channels = pd.read_csv('searchPool/Channels.csv')
all = pd.merge(all,Channels,how='left',on='channel')

#%%
all.drop('title', axis=1, inplace=True)
#%%
account = [1,2,3,4,5,6,7,8,9,10]
interest = [1,2,3]
percent = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #

for a in account:
    for i in interest:
        for p in percent:
            filename = 'watchlist/' + str(a)+'_'+str(i) +'_'+ str(p) + '.csv'
            watchhistory = pd.read_csv(filename)
            watchhistory = pd.merge(watchhistory,all,how='left',on='url')
            watchhistory['view'] = watchhistory['label'].str.findall(r'[\d|,]+ views')
            watchhistory['view'] = watchhistory['view'].astype(str)
            watchhistory['view'] = watchhistory['view'].str.replace('[views\[\'\] ,]+', '')
            watchhistory['view'].loc[watchhistory['view'] == ''] = 0
            watchhistory['view'] = watchhistory['view'].astype(int)
            watchhistory['hour'] = watchhistory['label'].str.findall(r'o \d+ hour')
            watchhistory['hour'] = watchhistory['hour'].astype(str)
            watchhistory['hour'] = watchhistory['hour'].str.findall(r'\d+')
            watchhistory['hour'] = watchhistory['hour'].astype(str)
            watchhistory['hour'] = watchhistory['hour'].str.replace('[\[\'\] ,]+', '')
            watchhistory['hour'].loc[watchhistory['hour'] == ''] = 0
            watchhistory['hour'] = watchhistory['hour'].astype(int)
            watchhistory['minute'] = watchhistory['label'].str.findall(r'[o|,] \d+ minute')
            watchhistory['minute'] = watchhistory['minute'].astype(str)
            watchhistory['minute'] = watchhistory['minute'].str.findall(r'\d+')
            watchhistory['minute'] = watchhistory['minute'].astype(str)
            watchhistory['minute'] = watchhistory['minute'].str.replace('[\[\'\] ,]+', '')
            watchhistory['minute'].loc[watchhistory['minute'] == ''] = 0
            watchhistory['minute'] = watchhistory['minute'].astype(int)
            watchhistory['second'] = watchhistory['label'].str.findall(r'[o|,] \d+ second')
            watchhistory['second'] = watchhistory['second'].astype(str)
            watchhistory['second'] = watchhistory['second'].str.findall(r'\d+')
            watchhistory['second'] = watchhistory['second'].astype(str)
            watchhistory['second'] = watchhistory['second'].str.replace('[\[\'\] ,]+', '')
            watchhistory['second'].loc[watchhistory['second'] == ''] = 0
            watchhistory['second'] = watchhistory['second'].astype(int)
            watchhistory['length'] = watchhistory['hour'] * 3600 + watchhistory['minute'] * 60 + watchhistory['second']
            filename = 'watchlistannotate/' + str(a) + '_' + str(i) + '_' + str(p) + '.csv'
            watchhistory.to_csv(filename)
#%%
news_list = ['NBCnews','ABCnews','CNN','MSNBC','CBSNews','WashintonPost','NowThisNews','Reuters',
'FoxNews',
'BloombergPolitics',
'Associatedpress',
'PBSNewsHour',
'TheWhiteHouse',
'CSPAN']


#%%
re.findall(r'[\d|,]+ views', '35 minutes 4,331 views')

#%%
regression_index = []
for a in account:
    for i in interest:
        for p in percent:
            filename = 'watchlist/' + str(a) + '_' + str(i) + '_' + str(p) + '.csv'
            watchhistory = pd.read_csv(filename)
            watchhistory = pd.merge(watchhistory, all, how='left', on='url')
            watchhistory['view'] = watchhistory['label'].str.findall(r'[\d|,]+ views')
            watchhistory['view'] = watchhistory['view'].astype(str)
            watchhistory['view'] = watchhistory['view'].str.replace('[views\[\'\] ,]+', '')
            watchhistory['view'].loc[watchhistory['view'] == ''] = 0
            watchhistory['view'] = watchhistory['view'].astype(int)
            watchhistory['hour'] = watchhistory['label'].str.findall(r'o \d+ hour')
            watchhistory['hour'] = watchhistory['hour'].astype(str)
            watchhistory['hour'] = watchhistory['hour'].str.findall(r'\d+')
            watchhistory['hour'] = watchhistory['hour'].astype(str)
            watchhistory['hour'] = watchhistory['hour'].str.replace('[\[\'\] ,]+', '')
            watchhistory['hour'].loc[watchhistory['hour'] == ''] = 0
            watchhistory['hour'] = watchhistory['hour'].astype(int)
            watchhistory['minute'] = watchhistory['label'].str.findall(r'[o|,] \d+ minute')
            watchhistory['minute'] = watchhistory['minute'].astype(str)
            watchhistory['minute'] = watchhistory['minute'].str.findall(r'\d+')
            watchhistory['minute'] = watchhistory['minute'].astype(str)
            watchhistory['minute'] = watchhistory['minute'].str.replace('[\[\'\] ,]+', '')
            watchhistory['minute'].loc[watchhistory['minute'] == ''] = 0
            watchhistory['minute'] = watchhistory['minute'].astype(int)
            watchhistory['second'] = watchhistory['label'].str.findall(r'[o|,] \d+ second')
            watchhistory['second'] = watchhistory['second'].astype(str)
            watchhistory['second'] = watchhistory['second'].str.findall(r'\d+')
            watchhistory['second'] = watchhistory['second'].astype(str)
            watchhistory['second'] = watchhistory['second'].str.replace('[\[\'\] ,]+', '')
            watchhistory['second'].loc[watchhistory['second'] == ''] = 0
            watchhistory['second'] = watchhistory['second'].astype(int)
            watchhistory['length'] = watchhistory['hour']*3600 + watchhistory['minute']*60 + watchhistory['second']
            watchhistory['percentCovered'] = 40/watchhistory['length']*100
            completeMaleIndex = watchhistory['MaleIndex'].mean()
            watchhistoryTemp = watchhistory[~watchhistory['channel'].isin(news_list)]
            entMaleIndex = watchhistoryTemp['MaleIndex'].mean()
            viewIndex = watchhistory['view'].mean()
            entViewIndex = watchhistoryTemp['view'].mean()
            percentCoverIndex = watchhistory['percentCovered'].mean()
            entPercentCoverIndex = watchhistoryTemp['percentCovered'].mean()
            watchhistoryTempnews = watchhistory[watchhistory['channel'].isin(news_list)]
            newsPercentCoverIndex = watchhistoryTempnews['percentCovered'].mean()
            temp = {'account': a,
                    'interest': i,
                    'percent':p,
                    'completeMaleIndex': completeMaleIndex,
                    'entMaleIndex':entMaleIndex,
                    'viewIndex':viewIndex,
                    'entViewIndex': entViewIndex,
                    'percentCoverIndex':percentCoverIndex,
                    'entPercentCoverIndex':entPercentCoverIndex,
                    'newsPercentCoverIndex':newsPercentCoverIndex}
            regression_index.append(temp)


#%%
regression_datafram = pd.DataFrame(regression_index)

#%%
regression_datafram.to_csv('watch_list_regression.csv')



