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
file = open("../YouTubeBot/models/sports_classifier",'rb')
classifier = pickle.load(file)
file.close()
file = open("../YouTubeBot/models/sports_tfidfconverter",'rb')
tfidfconverter = pickle.load(file)
file.close()
#%%
recommend = []
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
    tempPred = get_pred_poli(temp_file['title'], classifier)
    temp_file['predPoli'] = tempPred
    recommend.append(temp_file)

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

recommend = pd.concat(recommend)
recommend = recommend.reset_index()

#%%
recommend.to_csv('recommend_withFoodCode.csv')
recommend.to_csv('recommend_withSportsCode.csv')


#%%
baseline = []
account = [5,10]#
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
#baseline.to_csv('baseline_withFoodCode.csv')
baseline.to_csv('baseline_withSportsCode.csv')