# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/price/{ticker}")
def get_price(ticker: str):
    return {"ticker": ticker, "price": 123.45}