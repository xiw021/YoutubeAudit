#%%
import pandas as pd
import random

random.seed(10)
#%%
NBCnews = pd.read_csv('newslists/NBCnewslistDF.csv')
ABCnews = pd.read_csv('newslists/ABCnewslistDF.csv')
CNN = pd.read_csv('newslists/CNNlistDF.csv')
MSNBC = pd.read_csv('newslists/MSNBClistDF.csv')
CBSNews = pd.read_csv('newslists/CBSNewslistDF.csv')
WashintonPost = pd.read_csv('newslists/WashintonPostlistDF.csv')
NowThisNews = pd.read_csv('newslists/NowThisNewslistDF.csv')
Reuters = pd.read_csv('newslists/ReuterslistDF.csv')
FoxNews = pd.read_csv('newslists/FoxNewslistDF.csv')
BloombergPolitics = pd.read_csv('newslists/BloombergPoliticslistDF.csv')
Associatedpress = pd.read_csv('newslists/AssociatedpresslistDF.csv')
PBSNewsHour = pd.read_csv('newslists/PBSNewsHourlistDF.csv')
TheWhiteHouse = pd.read_csv('newslists/TheWhiteHouselistDF.csv')
CSPAN = pd.read_csv('newslists/CSPANlistDF.csv')

news = pd.concat([NBCnews,ABCnews,CNN,MSNBC,CBSNews,WashintonPost,NowThisNews,Reuters,FoxNews,BloombergPolitics,Associatedpress,PBSNewsHour,TheWhiteHouse,CSPAN])
news_sample = random.sample(list(news.title), 2000)

#%%
AlexCosta = pd.read_csv('entertain/fashionbeauty/AlexCostalistDF.csv')
AlphaM = pd.read_csv('entertain/fashionbeauty/AlphaMlistDF.csv')
AlyssaForever = pd.read_csv('entertain/fashionbeauty/AlyssaForeverlistDF.csv')
CarliBybel = pd.read_csv('entertain/fashionbeauty/CarliBybellistDF.csv')
Evelina = pd.read_csv('entertain/fashionbeauty/EvelinalistDF.csv')
IngridNilsen = pd.read_csv('entertain/fashionbeauty/IngridNilsenlistDF.csv')
itsjudytime = pd.read_csv('entertain/fashionbeauty/itsjudytimelistDF.csv')
LauraLee = pd.read_csv('entertain/fashionbeauty/LauraLeelistDF.csv')
Madeyewlook = pd.read_csv('entertain/fashionbeauty/MadeyewlooklistDF.csv')
MichellePhan = pd.read_csv('entertain/fashionbeauty/MichellePhanlistDF.csv')
NikitaDragun = pd.read_csv('entertain/fashionbeauty/NikitaDragunlistDF.csv')
RealMenRealStyle = pd.read_csv('entertain/fashionbeauty/RealMenRealStylelistDF.csv')
Teachingmensfashion = pd.read_csv('entertain/fashionbeauty/TeachingmensfashionlistDF.csv')
Vogue = pd.read_csv('entertain/fashionbeauty/VoguelistDF.csv')

fashionbeauty = pd.concat([AlexCosta,AlphaM,AlyssaForever,CarliBybel,Evelina,IngridNilsen,itsjudytime,LauraLee,Madeyewlook,MichellePhan,NikitaDragun,RealMenRealStyle,Teachingmensfashion,Vogue])
fashionbeauty_sample = random.sample(list(fashionbeauty.title), 500)

#%%
brailleSkateboarding = pd.read_csv('entertain/sports/brailleSkateboardinglistDF.csv')
DingProductions = pd.read_csv('entertain/sports/DingProductionslistDF.csv')
ESPN = pd.read_csv('entertain/sports/ESPNlistDF.csv')
NBA = pd.read_csv('entertain/sports/NBAlistDF.csv')
NFL = pd.read_csv('entertain/sports/NFLlistDF.csv')
NHL = pd.read_csv('entertain/sports/NHLlistDF.csv')
Rebound = pd.read_csv('entertain/sports/ReboundlistDF.csv')
Ridechannel = pd.read_csv('entertain/sports/RidechannellistDF.csv')
ShaolinCenter = pd.read_csv('entertain/sports/ShaolinCenterlistDF.csv')
TheWorldofBoxing  = pd.read_csv('entertain/sports/TheWorldofBoxinglistDF.csv')
Thefumble = pd.read_csv('entertain/sports/ThefumblelistDF.csv')
TheMaxLife = pd.read_csv('entertain/sports/TheMaxLifelistDF.csv')
tmzsports = pd.read_csv('entertain/sports/tmzsportslistDF.csv')
XGames = pd.read_csv('entertain/sports/XGameslistDF.csv')

#%%
sports = pd.concat([brailleSkateboarding,DingProductions,ESPN,NBA,NFL,NHL,Rebound,Ridechannel,ShaolinCenter,TheWorldofBoxing,Thefumble,TheMaxLife,tmzsports,XGames])
sports_sample = random.sample(list(sports.title), 500)



#%%
PlayStation = pd.read_csv('entertain/game/PlayStationlistDF.csv')
Videogamedunkey = pd.read_csv('entertain/game/VideogamedunkeylistDF.csv')
Boogie2988 = pd.read_csv('entertain/game/Boogie2988listDF.csv')
Uberhaxornova = pd.read_csv('entertain/game/UberhaxornovalistDF.csv')
IGN = pd.read_csv('entertain/game/IGNlistDF.csv')
MKIceAndFire = pd.read_csv('entertain/game/MKIceAndFirelistDF.csv')
GhostRobo = pd.read_csv('entertain/game/GhostRobolistDF.csv')
GameXplain = pd.read_csv('entertain/game/GameXplainlistDF.csv')
Chaos = pd.read_csv('entertain/game/ChaoslistDF.csv')
FuriousFade = pd.read_csv('entertain/game/FuriousFadelistDF.csv')
AFGguides = pd.read_csv('entertain/game/AFGguideslistDF.csv')
UbisoftNorthAmerica = pd.read_csv('entertain/game/UbisoftNorthAmericalistDF.csv')
WhatCultureGaming = pd.read_csv('entertain/game/WhatCultureGaminglistDF.csv')
Polygon = pd.read_csv('entertain/game/PolygonlistDF.csv')
#%%
game = pd.concat([PlayStation,
Videogamedunkey,
Boogie2988,
Uberhaxornova,
IGN,
MKIceAndFire,
GhostRobo,
GameXplain,
Chaos,
FuriousFade,
AFGguides,
UbisoftNorthAmerica,
WhatCultureGaming,
Polygon])
game_sample = random.sample(list(game.title), 500)

#%%
Gordonramsay = pd.read_csv('entertain/Food/GordonramsaylistDF.csv')
Epicmealtime = pd.read_csv('entertain/Food/EpicmealtimelistDF.csv')
Maangchi = pd.read_csv('entertain/Food/MaangchilistDF.csv')
Foodwishes = pd.read_csv('entertain/Food/FoodwisheslistDF.csv')
pickuplimes = pd.read_csv('entertain/Food/pickuplimeslistDF.csv')
Gugafoods = pd.read_csv('entertain/Food/GugafoodslistDF.csv')
PreppyKitchen = pd.read_csv('entertain/Food/PreppyKitchenlistDF.csv')
Natashaskitchen = pd.read_csv('entertain/Food/NatashaskitchenlistDF.csv')
sortedfood = pd.read_csv('entertain/Food/sortedfoodlistDF.csv')
Justonecookbook = pd.read_csv('entertain/Food/JustonecookbooklistDF.csv')
Cheaplazyvegan = pd.read_csv('entertain/Food/CheaplazyveganlistDF.csv')
MathaStewart = pd.read_csv('entertain/Food/MathaStewartlistDF.csv')
Caribbeanpot = pd.read_csv('entertain/Food/CaribbeanpotlistDF.csv')
LauraInTheKitchen = pd.read_csv('entertain/Food/LauraInTheKitchenlistDF.csv')

food = pd.concat([Gordonramsay,Epicmealtime,Maangchi,Foodwishes,pickuplimes,Gugafoods,PreppyKitchen,Natashaskitchen,sortedfood,Justonecookbook,Cheaplazyvegan,MathaStewart,Caribbeanpot,LauraInTheKitchen])
food_sample = random.sample(list(food.title), 500)


#%%

universalPictures = pd.read_csv('entertain/film/universalPictureslistDF.csv')
WaltDisney = pd.read_csv('entertain/film/WaltDisneylistDF.csv')
Deadmeat = pd.read_csv('entertain/film/DeadmeatlistDF.csv')
MovieclipTrailers = pd.read_csv('entertain/film/MovieclipTrailerslistDF.csv')
Screenrant = pd.read_csv('entertain/film/ScreenrantlistDF.csv')
MovieTheorists = pd.read_csv('entertain/film/MovieTheoristslistDF.csv')
TheThings = pd.read_csv('entertain/film/TheThingslistDF.csv')
Artspear = pd.read_csv('entertain/film/ArtspearlistDF.csv')
shupupCartoons = pd.read_csv('entertain/film/shupupCartoonslistDF.csv')
RapidTrailer = pd.read_csv('entertain/film/RapidTrailerlistDF.csv')
Filmonger = pd.read_csv('entertain/film/FilmongerlistDF.csv')
Smasher = pd.read_csv('entertain/film/SmasherlistDF.csv')
IsaacCarlson = pd.read_csv('entertain/film/IsaacCarlsonlistDF.csv')
FilmRise = pd.read_csv('entertain/film/FilmRiselistDF.csv')

film = pd.concat([universalPictures,
WaltDisney,
Deadmeat,
MovieclipTrailers,
Screenrant,
MovieTheorists,
TheThings,
Artspear,
shupupCartoons,
RapidTrailer,
Filmonger,
Smasher,
IsaacCarlson,
FilmRise])

film_sample = random.sample(list(film.title), 500)

#%%
sample = news_sample + film_sample + food_sample + sports_sample + game_sample + fashionbeauty_sample
#%%
sample_df = pd.DataFrame(sample, columns = ['title'])
sample_df.to_csv('audit_sample.csv')