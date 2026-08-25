import re
import nltk
import pandas as pd
from mysql.connector import connect, Error
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import pos_tag
try:
    conn = connect(host="localhost", user="root", password="imro9459", database="nlp_project")
    df = pd.read_sql("SELECT * FROM products", conn)
    conn.close()  # Close connection after loading
except Error as e:
    print(f"Database error: {e}")
    df = pd.DataFrame() 
# text clean

def clean_text(text):
    text=str(text).lower()
    text=re.sub(r'[^a-zA-Z\s]','',text)
    text=re.sub(r'\s+',' ',text).strip()
    return text
df['clean_text']=df['description'].apply(clean_text)
# Tokenization
def tokenize_text(text):
    return text.split()
df['tokens']=df['clean_text'].apply(tokenize_text)

# stopwords removal
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))
nltk.download('wordnet', quiet=True)
def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]
df['tokens_without_stopwords'] = df['tokens'].apply(remove_stopwords)
# lemmatizer
lemmatizer=WordNetLemmatizer()
def lemmatize_tokens(tokens): 
    return [lemmatizer.lemmatize(word) for word in tokens]
df['lemmatized_tokens']=df['tokens_without_stopwords'].apply(lemmatize_tokens)
df['text']=df['lemmatized_tokens'].apply(lambda x:" ".join(x))
# tf-idf vectorizer
tfidf=TfidfVectorizer()
X=tfidf.fit_transform(df['text'])

# pos-taggin
nltk.download('averaged_perceptron_tagger_eng',quiet=True)
def pos_taggin(tokens):
    return pos_tag(tokens)
df['pos_tags']=df['lemmatized_tokens'].apply(pos_taggin)
