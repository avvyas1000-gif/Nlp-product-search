# NLP Product Search

An NLP-based product search system that allows users to search for products using natural-language queries.

The system processes user queries using text preprocessing, regex-based pattern extraction, TF-IDF vectorization, cosine similarity, and product filtering to return relevant products.

## Features

* Natural-language product search
* Text preprocessing and cleaning
* Regex-based pattern extraction
* TF-IDF vectorization
* Cosine similarity
* Product filtering
* Similarity-based product ranking
* FastAPI REST API
* Interactive API documentation
* Test implementation

## Tech Stack

* **Python** — Core programming language
* **FastAPI** — REST API development
* **Pandas** — Dataset handling
* **NumPy** — Numerical operations
* **Scikit-learn** — TF-IDF and cosine similarity
* **NLTK** — NLP preprocessing
* **Regex** — Pattern extraction
* **Uvicorn** — ASGI server

## How It Works

The search pipeline follows these steps:

```text
User Query
    ↓
Text Preprocessing
    ↓
Regex / Pattern Extraction
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Product Filtering
    ↓
Product Ranking
    ↓
Search Results
```

For example, a user can search:

```text
black running shoes for men
```

The system processes the query, extracts relevant information, compares it with the product dataset, calculates similarity scores, and returns relevant products.

## NLP Processing

### Text Preprocessing

The input text is cleaned and normalized before processing.

The preprocessing pipeline includes operations such as:

* Lowercasing
* Removing unnecessary characters
* Tokenization
* Stopword removal
* Text normalization

### Pattern Extraction

Regex-based patterns are used to identify predefined product-related information from the search query.

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

### TF-IDF

TF-IDF converts product text and the user's query into numerical vectors.

This allows the system to compare the textual representation of the query with product information.

### Cosine Similarity

Cosine similarity is used to calculate the similarity between the search query and products.

Products with higher similarity scores are considered more relevant and can be ranked higher in the results.

## Project Structure

```text
nlp-product-search/
│
├── app.py
├── main.py
├── preprocessing.py
├── ner.py
├── filter.py
├── hld.py
├── lld.py
├── test.py
├── products.csv
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── README.md
├── LICENSE
└── .gitignore
```

### File Description

| File               | Description                              |
| ------------------ | ---------------------------------------- |
| `app.py`           | FastAPI application and API endpoints    |
| `main.py`          | Main search functionality                |
| `preprocessing.py` | Text preprocessing and TF-IDF processing |
| `ner.py`           | Pattern/entity extraction                |
| `filter.py`        | Product filtering and ranking            |
| `hld.py`           | High-Level Design                        |
| `lld.py`           | Low-Level Design                         |
| `test.py`          | Test cases                               |
| `products.csv`     | Synthetic product dataset                |
| `requirements.txt` | Python dependencies                      |
| `pyproject.toml`   | Project configuration                    |
| `uv.lock`          | Locked dependency versions               |

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd nlp-product-search
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

Using `requirements.txt`:

```bash
pip install -r requirements.txt
```

If you are using `uv`:

```bash
uv sync
```

## Running the Project

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger interface to send search queries and test the API.

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

## Example Query

Example search query:

```text
black running shoes for men
```

The system processes the query and returns products ranked according to their relevance.

## Running Tests

To run the test file:

```bash
python test.py
```

## Dataset

The project uses `products.csv`, a synthetic product dataset created for development and testing purposes.

It is not an official product catalog and is not affiliated with any specific brand.

## Project Workflow

```text
User
  ↓
Search Query
  ↓
FastAPI
  ↓
Preprocessing
  ↓
Pattern Extraction
  ↓
TF-IDF
  ↓
Cosine Similarity
  ↓
Filtering
  ↓
Ranking
  ↓
Relevant Products
```

## Future Improvements

Possible improvements include:

* Semantic search using sentence embeddings
* Fuzzy matching
* Hybrid keyword and semantic search
* Vector database integration
* Improved query understanding
* Search result caching
* Database integration
* Advanced ranking techniques

## License

This project is licensed under the MIT License.
