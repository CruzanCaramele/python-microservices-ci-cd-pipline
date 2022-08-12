import uvicorn
from fastapi import FastAPI
from src.logic import wiki as wikipage, wiki_search


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia Here we go!!!. Call /search or /wiki endpoints"}


@app.get("/wiki/{text}")
async def wiki(text: str):
    """Wikipedia page"""
    result = wikipage(text)
    return {"result": result}


@app.get("/search/{phrase}")
async def search(phrase: str):
    """Page to search in wikipedia"""
    result = wiki_search(phrase)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="127.0.0.1")
