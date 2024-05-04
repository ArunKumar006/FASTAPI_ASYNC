from fastapi import FastAPI,APIRouter
from fastapi.responses import Response

app = FastAPI()

router = APIRouter()

@router.get("/")
def home():
    return Response({"page":"home"},status_code=200)