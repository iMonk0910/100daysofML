import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def pre_process(text):
    text = text.lower()
    text_tokens = nltk.word_tokenize(text)

    string_list = []
    for i in text_tokens:
        if i.isalnum(): #check alphanumeric
            string_list.append(i)
    
    
    string_list = word for word in string_list if not word in stopwords.words('english')] #remove stopwords

    
    string_list = word for word in string_list if not word in string.punctuation:   #remove punctuation

    #stemming
    ps = PorterStemmer()
    stemmed_list = []
    
    for i in string_list:
        stemmed_list.append(ps.stem(i))

    return " ".join(stemmed_list)

tfidf = pickle.load(open('vectorizer.pkl','rb'))   # vectorizer file
model = pickle.load(open('model.pkl','rb'))        #model

st.title("Email/SMS Spam Classifier")

input_email_sms = st.text_area("Enter the email/SMS")


if st.button('Predict'):
    pre_processed_email_sms = pre_process(input_email_sms)   # preprocess
    
    vector_input = tfidf.transform([pre_processed_email_sms]) # vectorize
    
    result = model.predict(vector_input)[0]  # predict
    
    if result == 1:      
        st.header("Spam")
    else:
        st.header("Not Spam")
        
