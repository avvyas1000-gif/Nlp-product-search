# NLP Product Search

An NLP-based product search system that processes natural-language queries and retrieves relevant products from a product dataset.

The system combines text preprocessing, regex-based pattern extraction, TF-IDF vectorization, cosine similarity, and product filtering to identify products that are relevant to a user's search query.

A FastAPI backend is used to expose the search functionality through a REST API.

---

## Overview

Traditional product search systems often depend on exact keyword matching.

For example, a user searching for:

```text
black running shoes for men
```

may not get useful results if the product information contains slightly different wording.

This project uses NLP techniques to process both the user query and product information and then calculate their textual similarity.

The system converts text into numerical representations using **TF-IDF** and compares them using **Cosine Similarity**.

---

## Features

* Natural-language product search
* Text preprocessing
* Tokenization
* Stopword removal
* Text normalization
* Regex-based pattern extraction
* TF-IDF vectorization
* Cosine similarity
* Product filtering
* Similarity-based product ranking
* FastAPI REST API
* Interactive API documentation with Swagger UI
* Modular project structure

---

## Technologies Used

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python       | Main programming language    |
| FastAPI      | REST API development         |
| Pandas       | Dataset handling             |
| NumPy        | Numerical operations         |
| Scikit-learn | TF-IDF and cosine similarity |
| NLTK         | NLP preprocessing            |
| Regex        | Pattern extraction           |
| Uvicorn      | ASGI server                  |

---

## System Architecture

```text
                User
                  |
                  v
            Search Query
                  |
                  v
        +-------------------+
        |  FastAPI Backend   |
        +-------------------+
                  |
                  v
        +-------------------+
        | Text Preprocessing |
        +-------------------+
                  |
                  v
        +-------------------+
        | Pattern Extraction |
        |      (Regex)       |
        +-------------------+
                  |
                  v
        +-------------------+
        |   TF-IDF Vectorizer|
        +-------------------+
                  |
                  v
        +-------------------+
        | Cosine Similarity  |
        +-------------------+
                  |
                  v
        +-------------------+
        | Product Filtering  |
        +-------------------+
                  |
                  v
        +-------------------+
        | Product Ranking    |
        +-------------------+
                  |
                  v
           Search Results
```

---

## Project Workflow

### 1. User Query

The user sends a natural-language product search query.

Example:

```text
black running shoes for men
```

The query is passed to the FastAPI search endpoint.

---

### 2. Text Preprocessing

Before comparing the query with products, the text is cleaned and normalized.

The preprocessing pipeline can include:

* Converting text to lowercase
* Removing unnecessary characters
* Removing unwanted symbols
* Tokenization
* Stopword removal
* Normalizing text
* Removing unnecessary tokens

Example:

```text
Original:
Black Running Shoes for Men

Processed:
black running shoes men
```

This produces a cleaner representation for further processing.

---

### 3. Pattern Extraction

Regex-based patterns are used to identify specific information from the user's query.

Depending on the product dataset, patterns can be created for attributes such as:

* Product type
* Gender
* Color
* Size
* Brand
* Category
* Other predefined product attributes

For example:

```text
black running shoes for men
```

can contain information such as:

```text
Color    → black
Category → running shoes
Gender   → men
```

The extracted information can then be used during product filtering.

---

### 4. TF-IDF Vectorization

After preprocessing, the product text and user query are converted into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

TF-IDF gives higher importance to words that are useful for distinguishing one document from another.

For example, common words that appear in many products receive relatively less importance, while more specific product terms receive higher importance.

The vectorizer transforms text into a numerical representation:

```text
Text
 ↓
TF-IDF Vectorizer
 ↓
Numerical Vector
```

---

### 5. Cosine Similarity

Once the query and products have been converted into vectors, cosine similarity is used to measure their similarity.

The similarity score ranges from:

```text
0 → Low similarity
1 → High similarity
```

Conceptually:

```text
User Query
     |
     v
TF-IDF Vector
     |
     +------ Product 1 → Similarity Score
     |
     +------ Product 2 → Similarity Score
     |
     +------ Product 3 → Similarity Score
```

Products with higher similarity scores are considered more relevant to the query.

---

### 6. Product Filtering

After calculating similarity, additional filtering rules can be applied.

For example, if the user searches for:

```text
men black running shoes
```

the system can prioritize products matching:

```text
Gender → Men
Color  → Black
Type   → Running Shoes
```

This helps reduce irrelevant products.

---

### 7. Product Ranking

The matching products are ranked according to their relevance.

A simplified result could look like:

```text
Product                          Similarity
------------------------------------------------
Black Running Shoes              0.91
Men's Running Sneakers           0.86
Black Sports Shoes               0.78
Casual Walking Shoes             0.52
```

The highest-scoring products are returned first.

---

# Project Structure

```text
nlp-product-search/
│
├── data/
│   └── products.csv
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── preprocessing.py
│   ├── ner.py
│   └── filter.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

### File Description

#### `main.py`

Contains the FastAPI application and API endpoints.

#### `preprocessing.py`

Contains the text preprocessing and TF-IDF-related functionality.

#### `ner.py`

Contains pattern/entity extraction logic used to identify useful information from search queries.

#### `filter.py`

Contains product filtering and ranking-related logic.

#### `products.csv`

Contains the product information used by the search system.

#### `requirements.txt`

Contains the Python dependencies required to run the project.

---

# API

The project provides a REST API using FastAPI.

## Start the Server

Run:

```bash
uvicorn app.main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically provides interactive documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

---

# Search Endpoint

The search API accepts a natural-language query.

Example request:

```json
{
    "query": "black running shoes for men"
}
```

The backend processes the query and returns relevant products based on the implemented search logic.

Example response structure:

```json
{
    "results": [
        {
            "product": "Black Running Shoes",
            "score": 0.91
        },
        {
            "product": "Men's Running Sneakers",
            "score": 0.86
        }
    ]
}
```

The exact response fields depend on the implementation of the API.

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd nlp-product-search
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# Example Queries

The system can process queries such as:

```text
black running shoes
```

```text
white sneakers for men
```

```text
red sports shoes
```

```text
comfortable running shoes
```

```text
men's casual shoes
```

The exact queries supported depend on the product attributes available in the dataset and the patterns implemented in the project.

---

# NLP Pipeline

The complete NLP pipeline can be summarized as:

```text
Raw Query
    ↓
Lowercase
    ↓
Text Cleaning
    ↓
Tokenization
    ↓
Stopword Removal
    ↓
Pattern Extraction
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Product Filtering
    ↓
Ranking
    ↓
Final Results
```

---

# Why TF-IDF?

TF-IDF was selected because it provides a simple and interpretable way to represent textual information.

It considers:

* How frequently a term appears in a document
* How common the term is across the entire dataset

This makes it useful for comparing product descriptions with search queries.

---

# Why Cosine Similarity?

Cosine similarity measures the angle between two vectors rather than simply comparing their raw values.

This makes it useful for comparing:

```text
Search Query Vector
        ↓
Product Vector
```

A higher cosine similarity indicates that the query and product have more similar textual representations.

---

# Limitations

This project primarily uses traditional NLP and information-retrieval techniques.

Some limitations include:

* TF-IDF does not understand the deeper semantic meaning of words.
* Synonyms may not always be recognized as related.
* Results depend on the quality of the product dataset.
* Regex-based extraction depends on predefined patterns.
* Complex natural-language queries may require additional processing.
* Similarity scores depend on the vocabulary present in the dataset.

---

# Possible Improvements

The system can be extended with:

* Word embeddings
* Sentence Transformers
* Semantic search
* Vector databases
* Fuzzy matching
* Better entity extraction
* Advanced query understanding
* Hybrid keyword + semantic search
* Search result caching
* Pagination
* Authentication
* Database integration
* Search analytics

---

# Learning Outcomes

This project covers practical implementation of:

* Natural Language Processing
* Text preprocessing
* Regular expressions
* TF-IDF
* Vector similarity
* Information retrieval
* Product filtering
* Ranking systems
* REST API development
* FastAPI

---

# Future Scope

A future version of the system could use transformer-based embeddings to perform semantic search.

For example, queries such as:

```text
shoes suitable for daily jogging
```

and:

```text
comfortable shoes for running every day
```

could be treated as semantically similar even when they do not share many exact words.

This could be implemented using sentence embeddings and a vector database.

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

# Author

**Ankit Vyas**

This project was developed as part of my learning and practice in NLP, Machine Learning, and Python API development.
