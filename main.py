from fastapi import FastAPI  # pylint: disable=import-error
import uvicorn  # pylint: disable=import-error
from library import function_one

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Fast and Simple Wiki API. Call /search or /wiki in url"}


@app.get("/search/{value}")
async def search(value: str):
    """Scrape wiki for provided value"""

    results = function_one.search_wiki({value})
    return {"results": results}


@app.get("/wiki/{value}")
async def wiki(value: str):
    """Get wiki page for provided value"""

    results = function_one.wiki({value})
    return {"results": results}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
