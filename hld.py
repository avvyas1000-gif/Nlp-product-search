"""
HIGH-LEVEL ARCHITECTURE
=======================

┌─────────────────────────────────────────────────────────────┐
│                    CLIENT (Web/Mobile)                     │
│                  Natural Language Query                    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    API GATEWAY (FastAPI)                   │
│                  POST /search Endpoint                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    NLP PROCESSING PIPELINE                 │
├─────────────────────────────────────────────────────────────┤
│  1. Text Preprocessing  →  clean_text(), tokenization     │
│  2. NER Extraction      →  product, color, brand, price   │
│  3. POS Tagging         →  identify adjectives/nouns      │
│  4. TF-IDF Vectorization → convert text to vectors        │
│  5. Cosine Similarity   →  calculate relevance scores     │
│  6. Product Filtering   →  apply entity-based filters     │
│  7. Product Ranking     →  sort by relevance              │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    DATA LAYER                              │
│         ┌──────────────┐    ┌──────────────────┐         │
│         │   MySQL DB   │    │  TF-IDF Cache   │         │
│         │  Products    │    │  (Pickle Files) │         │
│         └──────────────┘    └──────────────────┘         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    RESPONSE                                │
│          Top 10 Relevant Products with Scores              │
└─────────────────────────────────────────────────────────────┘

TECHNOLOGY STACK:
----------------
- FastAPI        → REST API
- spaCy          → NER + POS Tagging  
- scikit-learn   → TF-IDF + Cosine Similarity
- MySQL          → Product Database
- Pandas         → Data Manipulation
"""

# This is just documentation - no actual code