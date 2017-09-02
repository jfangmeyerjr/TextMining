import pandas as pd
import numpy as np

#Read data
df = pd.read_csv('Amazon_Unlocked_Mobile.csv')

#Sample data to speed computation
ds = df.sample(frac = 0.1, random_state = 10)

# print(df.head())
# print(ds.head())

#Drop missing
ds.dropna(inplace = True)

#Remove neutral rating of 3
ds = ds[ds['Rating'] != 3]

# Code 4 and 5 Positive and 1 and 2 Negative
ds['Positive Rating'] = np.where(ds['Rating'] > 3, 1, 0)
# print(ds.head())

#Explore
# print(ds['Positive Rating'].mean())
# command line: python -m pip install sklearn
# Got old version
# $ pip install -U scikit-learn
from sklearn.model_selection import train_test_split
#Split data
X_train, X_test, y_train, y_test = train_test_split(
    ds['Reviews'],
    ds['Positive Rating'],
    random_state = 0
)
# print('X_train first instance:\n', X_train.iloc[0],
#     '\nX_train shape: ', X_train.shape)

## COUNT VECTORIZER
from sklearn.feature_extraction.text import CountVectorizer
#Fit CountVectorizer to training data
vec = CountVectorizer().fit(X_train) #what kind of object is this?
# print(vec.get_feature_names()[::2000])
# print(len(vec.get_feature_names()))

#transform all reviews into a document-term matrix
X_train_vectorized = vec.transform(X_train)
# print(X_train_vectorized)

from sklearn.linear_model import LogisticRegression
#Train model with vectorized data
logreg1 = LogisticRegression()
logreg1.fit(X_train_vectorized, y_train)

from sklearn.metrics import roc_auc_score
#transformed test Documents
X_test_vectorized = vec.transform(X_test)
#Predict positive sentiment
logreg1_preds = logreg1.predict(X_test_vectorized)
#Check performance, must be at least %Positive, which was around 75%
# print('AUC: ', roc_auc_score(y_test, logreg1_preds))

# Find most correlated words to positive outcome
#get feature names as numpy array
feature_names = np.array(vec.get_feature_names())
#Sort coefficients low to high
sorted_feature_coefs = logreg1.coef_[0].argsort()
# print(feature_names[sorted_feature_coefs])
#print smallest and largest coefficients
# print('Least correlated to Positive Review:\n{}\n'
#     .format(feature_names[sorted_feature_coefs[:10]]))
# print('Most correlated to Positive Review:\n{}\n'
#     .format(feature_names[sorted_feature_coefs[:-11:-1]]))

## TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
#Fit TfidfVectorizer to training data, with minimum doc freq =5
tfidfvec = TfidfVectorizer(min_df=5).fit(X_train)
# print(len(tfidfvec.get_feature_names()), len(vec.get_feature_names()))

X_train_tfidfvec = tfidfvec.transform(X_train)

logreg2 = LogisticRegression()
logreg2.fit(X_train_tfidfvec, y_train)

#if we vectorize with .transform() the training x's, we must do same with test x's
logreg2_preds = logreg2.predict(tfidfvec.transform(X_test))

# print('AUC tfidf: {}\nAUC standard: {}'.format(
#     roc_auc_score(y_test, logreg2_preds),
#     roc_auc_score(y_test, logreg1_preds)))
#AUC was better without tfidf, but only by 1%. Perhaps the gain in memory and meaningful featuers in tfidf merits giving up 1%

tfidf_feat_names = np.array(tfidfvec.get_feature_names())
sorted_tfidf_index = X_train_tfidfvec.max(0).toarray()[0].argsort()

# print('Least used:\n{}\nMost used:\n{}'
#     .format(
#     tfidf_feat_names[sorted_tfidf_index[:10]],
#     tfidf_feat_names[sorted_tfidf_index[:-11:-1]]
#     ))

sorted_tfidfcoefs = logreg2.coef_[0].argsort()

# print('Lowest correlation:\n{}\nHighest correlation:\n{}'
#     .format(
#     tfidf_feat_names[sorted_tfidfcoefs[:10]],
#     tfidf_feat_names[sorted_tfidfcoefs[:-11:-1]]
#     ))

# print(logreg2.predict(tfidfvec
#     .transform(['not an issue, phone is working',
#                 'an issue, phone is not working'])))
# predicts [0 0] both negative
# print(logreg2.predict(tfidfvec
#     .transform(['an issue, phone is working',
#                 'an issue, phone is not working'])))
# # predicts [1 0] positive Negative
#
# print(logreg2.predict(tfidfvec
#     .transform(['issue',
#                 'not'])))
# predicts [1 0] positive Negative
# print(logreg2.predict(tfidfvec
#     .transform(['bad',
#                 'good'])))
# predicts [0 1] negative positive

## N GRAMS
# grab 1 and 2 grams with CountVectorizer
nvect = CountVectorizer(min_df=5, ngram_range=(1,2)).fit(X_train)

X_train_nvect = nvect.transform(X_train)

# print(len(nvect.get_feature_names()))

logreg3 = LogisticRegression()
logreg3.fit(X_train_nvect, y_train)

logreg3_preds = logreg3.predict(nvect.transform(X_test))
# print('AUC: ', roc_auc_score(y_test, logreg3_preds))

ngram_feature_names = np.array(nvect.get_feature_names())
sorted_nvect_coef_index = logreg3.coef_[0].argsort()
# print('Smalles coef:\n{}\nLargest Coefs:\n{}'
#     .format(
#     ngram_feature_names[sorted_nvect_coef_index[:10]],
#     ngram_feature_names[sorted_nvect_coef_index[:-11:-1]]
#     ))

# print(logreg3.predict(nvect.transform([
#     'not an issue, phone is working',
#     'an issue, phone is not working'
# ])))
# gets it right [1 0]
print(logreg3.predict(nvect.transform([
    'not working',
    'working',
    'sort of working',
    'working alright',
    'might work'
])))

