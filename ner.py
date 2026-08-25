import spacy
import re
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

def extraction(query):
    doc = nlp(query)
    entity = {}
    query = query.lower()
    
    min_price_match = re.search(r'(?:above|over|more than|greater than|minimum|min)\s*[₹$€]?\s*(\d{3,6})', query)
    if min_price_match:
        entity['min_price'] = int(min_price_match.group(1))
        
    max_price_match = re.search(r'(?:under|below|less than|maximum|max)\s*[₹$€]?\s*(\d{3,6})', query)
    if max_price_match:
        entity['max_price'] = int(max_price_match.group(1))
        
    product_types = ['shoes', 'jacket', 'shirt', 'pants', 't-shirt', 'jeans', 'watch', 'bag']
    colors = ['black', 'white', 'red', 'blue', 'green', 'yellow', 'brown', 'grey', 'orange']
    styles = ['formal', 'casual', 'sports', 'running', 'party', 'office', 'wedding']
    brands = ['nike', 'adidas', 'puma', 'levis', 'tommy', 'zara', 'h&m']

    for ent in doc.ents:
        if ent.label_ == 'MONEY':
            price_text = re.sub(r'[^\d]', '', ent.text)
            if price_text:
                entity['max_price'] = int(price_text)
        elif ent.label_ == 'PRODUCT':
            entity['product'] = ent.text.lower()

    for token in doc:
        word = token.text.lower()
        if word in colors and 'color' not in entity:
            entity['color'] = word
        elif word in styles and 'style' not in entity:
            entity['style'] = word
        elif word in product_types and 'product' not in entity:
            entity['product'] = word
        elif word in brands and 'brand' not in entity:
            entity['brand'] = word
            
    return entity
if __name__ == "__main__":
    query = "I need comfortable brown formal shoes for office below 4000"
    result = extraction(query)
    print("Extracted Entities:", result)