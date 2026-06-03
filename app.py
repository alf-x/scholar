from fastapi import FastAPI
from pydantic import BaseModel

from index_service import get_index
from citation_service import get_citation

app = FastAPI()


class IndexRequest(BaseModel):
    id_scholar: str


class CitationRequest(BaseModel):
    id_scholar: str
    year: int


@app.get("/")
def home():
    return {
        "status": "running"
    }


@app.post("/index")
def index(data: IndexRequest):

    try:

        result = get_index(data.id_scholar)

        return {
            "success": True,
            "data": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


@app.post("/citation")
def citation(data: CitationRequest):

    try:

        result = get_citation(
            data.id_scholar,
            data.year
        )

        return {
            "success": True,
            "data": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }