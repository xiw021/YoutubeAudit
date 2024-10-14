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
recommend = pd.read_csv('recommend_withCode.csv')
baseline = pd.read_csv('baseline_withCode.csv')

#%%
temp = recommend.groupby(["account","interest","percent"])["predPoli"].mean().to_frame(name = 'averagePoli').reset_index()
temp_baseline = baseline.groupby(["account","interest","percent"])["predPoli_baseline"].mean().to_frame(name = 'averagePoli_baseline').reset_index()
temp = temp.merge(temp_baseline, how='left', on=['account','interest','percent'])
temp['clean_poli'] = temp['averagePoli'] - temp['averagePoli_baseline']

#%%
