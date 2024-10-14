# https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/
# https://stackabuse.com/text-classification-with-python-and-scikit-learn/
#%%
import pandas as pd
import random
import numpy as np
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
random.seed(10)
df1 = pd.read_csv('auditdata_collection/auditedData/PoliVSNonPoli.csv')

#%%
documents = []

stemmer = WordNetLemmatizer()

for i in range(len(df1['title'])):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(df1['title'][i]))
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
tfidfconverter = TfidfVectorizer(max_features=5000, min_df=5, max_df=0.5, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(documents).toarray()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, df1['label'], test_size=0.2, random_state=0)
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=2000, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
#%%
classifier = RandomForestClassifier(n_estimators=2000, random_state=0)
classifier.fit(X, df1['label'])

#%%
with open('text_classifier', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)


####### Use random forest model above.
#%%
trainDF = pd.DataFrame()
trainDF['text'] = documents
trainDF['label'] = df1['label']

#%%
# split the dataset into training and validation datasets
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble

import pandas, xgboost, numpy, textblob, string
#from keras.preprocessing import text, sequence
#from keras import layers, models, optimizers
#%%
train_x, valid_x, train_y, valid_y = model_selection.train_test_split(trainDF['text'], trainDF['label'])
# label encode the target variable
encoder = preprocessing.LabelEncoder()
train_y = encoder.fit_transform(train_y)
valid_y = encoder.fit_transform(valid_y)

#%%
# create a count vectorizer object
count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
count_vect.fit(trainDF['text'])

# transform the training and validation data using count vectorizer object
xtrain_count =  count_vect.transform(train_x)
xvalid_count =  count_vect.transform(valid_x)

#%%# word level tf-idf
tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000, min_df=5, max_df=0.5, stop_words=stopwords.words('english'))
tfidf_vect.fit(trainDF['text'])
xtrain_tfidf =  tfidf_vect.transform(train_x)
xvalid_tfidf =  tfidf_vect.transform(valid_x)

# ngram level tf-idf
tfidf_vect_ngram = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', ngram_range=(2,3), max_features=5000, min_df=5, max_df=0.5, stop_words=stopwords.words('english'))
tfidf_vect_ngram.fit(trainDF['text'])
xtrain_tfidf_ngram =  tfidf_vect_ngram.transform(train_x)
xvalid_tfidf_ngram =  tfidf_vect_ngram.transform(valid_x)

# characters level tf-idf
tfidf_vect_ngram_chars = TfidfVectorizer(analyzer='char', token_pattern=r'\w{1,}', ngram_range=(2,3), max_features=5000, min_df=5, max_df=0.5, stop_words=stopwords.words('english'))
tfidf_vect_ngram_chars.fit(trainDF['text'])
xtrain_tfidf_ngram_chars =  tfidf_vect_ngram_chars.transform(train_x)
xvalid_tfidf_ngram_chars =  tfidf_vect_ngram_chars.transform(valid_x)

#%%
def train_model(classifier, feature_vector_train, label, feature_vector_valid, is_neural_net=False):
    # fit the training dataset on the classifier
    classifier.fit(feature_vector_train, label)

    # predict the labels on validation dataset
    predictions = classifier.predict(feature_vector_valid)

    if is_neural_net:
        predictions = predictions.argmax(axis=-1)

    return metrics.accuracy_score(predictions, valid_y)

#%%
# Naive Bayes on Count Vectors
accuracy = train_model(naive_bayes.MultinomialNB(), xtrain_count, train_y, xvalid_count)
print("NB, Count Vectors: ", accuracy)

# Naive Bayes on Word Level TF IDF Vectors
accuracy = train_model(naive_bayes.MultinomialNB(), xtrain_tfidf, train_y, xvalid_tfidf)
print("NB, WordLevel TF-IDF: ", accuracy)

#%%
# Linear Classifier on Count Vectors
accuracy = train_model(linear_model.LogisticRegression(), xtrain_count, train_y, xvalid_count)
print("LR, Count Vectors: ", accuracy)

# Linear Classifier on Word Level TF IDF Vectors
accuracy = train_model(linear_model.LogisticRegression(), xtrain_tfidf, train_y, xvalid_tfidf)
print("LR, WordLevel TF-IDF: ", accuracy)

# Linear Classifier on Ngram Level TF IDF Vectors
accuracy = train_model(linear_model.LogisticRegression(), xtrain_tfidf_ngram, train_y, xvalid_tfidf_ngram)
print("LR, N-Gram Vectors: ", accuracy)

# Linear Classifier on Character Level TF IDF Vectors
accuracy = train_model(linear_model.LogisticRegression(), xtrain_tfidf_ngram_chars, train_y, xvalid_tfidf_ngram_chars)
print("LR, CharLevel Vectors: ", accuracy)

# Naive Bayes on Ngram Level TF IDF Vectors
accuracy = train_model(naive_bayes.MultinomialNB(), xtrain_tfidf_ngram, train_y, xvalid_tfidf_ngram)
print("NB, N-Gram Vectors: ", accuracy)

# Naive Bayes on Character Level TF IDF Vectors
accuracy = train_model(naive_bayes.MultinomialNB(), xtrain_tfidf_ngram_chars, train_y, xvalid_tfidf_ngram_chars)
print("NB, CharLevel Vectors: ", accuracy)

#%%
# SVM on Ngram Level TF IDF Vectors
accuracy = train_model(svm.SVC(), xtrain_tfidf, train_y, xvalid_tfidf)
print("SVM, N-Gram Vectors: ", accuracy)

#%%
# RF on Count Vectors
accuracy = train_model(ensemble.RandomForestClassifier(), xtrain_count, train_y, xvalid_count)
print("RF, Count Vectors: ", accuracy)

# RF on Word Level TF IDF Vectors
accuracy = train_model(ensemble.RandomForestClassifier(), xtrain_tfidf, train_y, xvalid_tfidf)
print("RF, WordLevel TF-IDF: ", accuracy)

#%%
# Extereme Gradient Boosting on Count Vectors
accuracy = train_model(xgboost.XGBClassifier(), xtrain_count.tocsc(), train_y, xvalid_count.tocsc())
print("Xgb, Count Vectors: ", accuracy)

# Extereme Gradient Boosting on Word Level TF IDF Vectors
accuracy = train_model(xgboost.XGBClassifier(), xtrain_tfidf.tocsc(), train_y, xvalid_tfidf.tocsc())
print("Xgb, WordLevel TF-IDF: ", accuracy)

# Extereme Gradient Boosting on Character Level TF IDF Vectors
accuracy = train_model(xgboost.XGBClassifier(), xtrain_tfidf_ngram_chars.tocsc(), train_y, xvalid_tfidf_ngram_chars.tocsc())
print("Xgb, CharLevel Vectors: ", accuracy)


########################################################################################################################
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
NBCnews = pd.read_csv('newslists/NBCnewslistDF.csv')
NBCnewsPred = get_pred_poli(NBCnews['title'],classifier)
NBCnews['predPoli'] = NBCnewsPred
NBCnews.to_csv('newslists/NBCnewslistDF.csv')

ABCnews = pd.read_csv('newslists/ABCnewslistDF.csv')
ABCnewsPred = get_pred_poli(ABCnews['title'],classifier)
ABCnews['predPoli'] = ABCnewsPred
ABCnews.to_csv('newslists/ABCnewslistDF.csv')

CNN = pd.read_csv('newslists/CNNlistDF.csv')
CNNPred = get_pred_poli(CNN['title'],classifier)
CNN['predPoli'] = CNNPred
CNN.to_csv('newslists/CNNlistDF.csv')

MSNBC = pd.read_csv('newslists/MSNBClistDF.csv')
MSNBCPred = get_pred_poli(MSNBC['title'],classifier)
MSNBC['predPoli'] = MSNBCPred
MSNBC.to_csv('newslists/MSNBClistDF.csv')

CBSNews = pd.read_csv('newslists/CBSNewslistDF.csv')
CBSNewsPred = get_pred_poli(CBSNews['title'],classifier)
CBSNews['predPoli'] = CBSNewsPred
CBSNews.to_csv('newslists/CBSNewslistDF.csv')

WashintonPost = pd.read_csv('newslists/WashintonPostlistDF.csv')
WashintonPostPred = get_pred_poli(WashintonPost['title'],classifier)
WashintonPost['predPoli'] = WashintonPostPred
WashintonPost.to_csv('newslists/WashintonPostlistDF.csv')

NowThisNews = pd.read_csv('newslists/NowThisNewslistDF.csv')
NowThisNewsPred = get_pred_poli(NowThisNews['title'],classifier)
NowThisNews['predPoli'] = NowThisNewsPred
NowThisNews.to_csv('newslists/NowThisNewslistDF.csv')

Reuters = pd.read_csv('newslists/ReuterslistDF.csv')
ReutersPred = get_pred_poli(Reuters['title'],classifier)
Reuters['predPoli'] = ReutersPred
Reuters.to_csv('newslists/ReuterslistDF.csv')

FoxNews = pd.read_csv('newslists/FoxNewslistDF.csv')
FoxNewsPred = get_pred_poli(FoxNews['title'],classifier)
FoxNews['predPoli'] = FoxNewsPred
FoxNews.to_csv('newslists/FoxNewslistDF.csv')

BloombergPolitics = pd.read_csv('newslists/BloombergPoliticslistDF.csv')
BloombergPoliticsPred = get_pred_poli(BloombergPolitics['title'],classifier)
BloombergPolitics['predPoli'] = BloombergPoliticsPred
BloombergPolitics.to_csv('newslists/BloombergPoliticslistDF.csv')


Associatedpress = pd.read_csv('newslists/AssociatedpresslistDF.csv')
AssociatedpressPred = get_pred_poli(Associatedpress['title'],classifier)
Associatedpress['predPoli'] = AssociatedpressPred
Associatedpress.to_csv('newslists/AssociatedpresslistDF.csv')

PBSNewsHour = pd.read_csv('newslists/PBSNewsHourlistDF.csv')
PBSNewsHourPred = get_pred_poli(PBSNewsHour['title'],classifier)
PBSNewsHour['predPoli'] = PBSNewsHourPred
PBSNewsHour.to_csv('newslists/PBSNewsHourlistDF.csv')

TheWhiteHouse = pd.read_csv('newslists/TheWhiteHouselistDF.csv')
TheWhiteHousePred = get_pred_poli(TheWhiteHouse['title'],classifier)
TheWhiteHouse['predPoli'] = TheWhiteHousePred
TheWhiteHouse.to_csv('newslists/TheWhiteHouselistDF.csv')

CSPAN = pd.read_csv('newslists/CSPANlistDF.csv')
CSPANPred = get_pred_poli(CSPAN['title'],classifier)
CSPAN['predPoli'] = CSPANPred
CSPAN.to_csv('newslists/CSPANlistDF.csv')


