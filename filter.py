from preprocessing import df
def filter_products(entities):
    result=df.copy()
    if 'product' in entities:
        result=result[result['category'].astype(str).str.lower()==entities['product'].lower()]
    if 'color' in entities:
        result=result[result['color'].astype(str).str.lower()==entities['color'].lower()]
    if 'style' in entities:
        result=result[result['style'].astype(str).str.lower()==entities['style'].lower()]
    if 'brand' in entities:
        result=result[result['brand'].astype(str).str.lower()==entities['brand'].lower()]
    if 'use_case' in entities:
        result=result[result['use_case'].astype(str).str.lower()==entities['use_case'].lower()]
    if 'min_price' in entities:
        result=result[result['price']>=entities['min_price']]
    if 'max_price' in entities:
        result=result[result['price']<=entities['max_price']]
    return result
if __name__=="__main__":
    entities={'product':'shoes','color':'black','max_price':5000 }
    result=filter_products(entities)
    print(result[['product_id','product_name','description','price','category','brand','color','style','use_case']])