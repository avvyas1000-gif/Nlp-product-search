from fastapi import FastAPI
from pydantic import BaseModel
from preprocessing import tfidf
from ner import extraction
from filter import filter_products
from sklearn.metrics.pairwise import cosine_similarity

app=FastAPI(title="NLP Product Search API")

class SearchRequest(BaseModel):
    query:str

@app.get("/")
def home():
    return{"message":"NLP Product Search API is running"}

@app.post("/search")
def search_products(request:SearchRequest):
    query=request.query
    entities=extraction(query)
    result=filter_products(entities)
    if result.empty:
        return{
            "query":query,
            "entities":entities,
             "result":[]
            }
    query_vector=tfidf.transform([query])
    product_vectors=tfidf.transform(result['text'])
    similarity=cosine_similarity(query_vector,product_vectors).flatten()

    result=result.copy()
    result['similarity']=similarity
    result=result.sort_values('similarity',ascending=False)

    products=result[['product_id','product_name','description','price',
         'category','brand','color','style','use_case','similarity']].head(10)   
    return {
        "query":query,
        "entities":entities,
        "results":products.to_dict(orient="records")
    }