#4. Your practice task
# Without looking at my code, create this endpoint:

# GET /products/{product_id}?discount=10

# Requirements:
# - product_id should be an integer path parameter.
# - discount should be an optional integer query parameter.
# - If discount is not provided, its value should be 0.
# Write the endpoint and send it to me. I’ll check your logic.

from fastapi import FastAPI

app = FastAPI()
@app.get("/products/{product_id}")
def products_details(product_id:int,discount:int=0):
    return {
        "product_id":product_id,
        "discount":discount
    }


# Create this endpoint:

# GET /products?name=laptop&min_price=500

# Requirements:
# - name is an optional string.
# - min_price is an optional integer.
# - If either parameter is missing, its value should be None.
# Write the code yourself. I'll check it next.

@app.get("/products_details")
def details(name:str|None=None,min_price:int|None=None):
    return {
        "name":name,
        "min_price":min_price
    }