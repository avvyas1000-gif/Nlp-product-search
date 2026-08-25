"""
LOW-LEVEL ARCHITECTURE
======================

MODULE DEPENDENCIES:
-------------------
api.py
  ├── ner.py
  │   ├── spaCy (en_core_web_sm)
  │   └── re (regex)
  ├── filter.py
  │   └── preprocessing.py (df)
  └── preprocessing.py
      ├── MySQL Connection
      ├── nltk (stopwords, wordnet)
      ├── sklearn (TfidfVectorizer)
      └── pandas

DATA FLOW (SEQUENCE):
--------------------
1. Client → FastAPI → POST /search
2. FastAPI → ner.extraction(query)
   → Returns: {"product":"shoes", "color":"black", "max_price":3000}
3. FastAPI → filter.filter_products(entities)
   → Returns: Filtered DataFrame
4. FastAPI → tfidf.transform([query])
   → Returns: Query Vector (1 x n)
5. FastAPI → tfidf.transform(result['text'])
   → Returns: Product Vectors (m x n)
6. FastAPI → cosine_similarity(query_vector, product_vectors)
   → Returns: Similarity Scores [0.91, 0.76, 0.42...]
7. FastAPI → Sort products by similarity
   → Returns: Top 10 Products

CODE FLOW (api.py):
------------------
@app.post("/search")
def search_products(request: SearchRequest):
    # Step 1: Extract entities
    entities = extraction(request.query)
    
    # Step 2: Filter products
    result = filter_products(entities)
    
    # Step 3: Check if empty
    if result.empty:
        return {"query": query, "entities": entities, "results": []}
    
    # Step 4: TF-IDF vectorization
    query_vector = tfidf.transform([query])
    product_vectors = tfidf.transform(result['text'])
    
    # Step 5: Cosine similarity
    similarity = cosine_similarity(query_vector, product_vectors).flatten()
    
    # Step 6: Add scores and rank
    result['similarity'] = similarity
    result = result.sort_values('similarity', ascending=False)
    
    # Step 7: Return top 10
    products = result[['product_id', 'product_name', 'description', 
                      'price', 'category', 'brand', 'color', 
                      'style', 'use_case', 'similarity']].head(10)
    
    return {
        "query": query,
        "entities": entities,
        "results": products.to_dict(orient="records")
    }

DATABASE SCHEMA:
---------------
Table: products
├── product_id (VARCHAR, PK)
├── product_name (VARCHAR)
├── description (TEXT)
├── price (DECIMAL)
├── category (VARCHAR)
├── brand (VARCHAR)
├── color (VARCHAR)
├── style (VARCHAR)
└── use_case (VARCHAR)

FILE STRUCTURE:
--------------
project-nlp/
├── api.py          # FastAPI endpoints
├── preprocessing.py # Text cleaning, TF-IDF
├── ner.py          # NER extraction
├── filter.py       # Product filtering
├── search.py       # CLI search
└── main.py         # Entry point
"""

# This is just documentation - no actual code