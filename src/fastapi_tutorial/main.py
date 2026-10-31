from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# @app.get("/about")
# def about():
#     return {
#         "Message" : "Welcome to my page"
#     }


# #path parameter


# @app.get("/get_user/{user_id}")
# def get_user(user_id):
#     return {
#         "user_id" : user_id
#     }


# #query parameter and #optional query parameters

# @app.get("/products")
# def get_products(name:str | None = None ):
#     return{
#         "name":name
#     }

# #default value

# @app.get("/get_price")
# def price(price:int=1000):
#     return {
#          "price":price
#     }

# #multiple query parameters
# @app.get("/person")
# def details(name:str|None=None, age:int=1000):
#     return {
#         "name" : name,
#         "age"  : age

#     }


# #post api 
# @app.post("/create-user")
# def create_user(user:dict):
#     return{
#         "message":"User created",
#         "data":user
#     }


#pydantic model

class User(BaseModel):
    name:str
    age:int


@app.post("/create_user")    
def create_user(user:User):
    return{
        "message":"your user is created",
        "data":user
    }





































