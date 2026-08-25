from preprocessing import df
from ner import extraction
from filter import filter_products
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import tfidf, df

query=input("Enter your query: ")
entities=extraction(query)
print("Entities:",entities)

result=filter_products(entities)

if result.empty:
    print("No products found")
else:
    query_vector=tfidf.transform([query])
    filtered_vectors=tfidf.transform(result['text'])
    similarity=cosine_similarity(query_vector,filtered_vectors).flatten()
    result=result.copy()
    result['similarity']=similarity
    result=result.sort_values('similarity',ascending=False)
    print(result[['product_id','product_name','description','price','category','brand','color','style','use_case','similarity']].head(10))