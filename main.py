from fastapi import FastAPI
from models import Product

app=FastAPI()

@app.get("/")
def greet ():
    return products


products=[Product(id=1,name="phone",description="budget phone",price=99,quantity=10)]