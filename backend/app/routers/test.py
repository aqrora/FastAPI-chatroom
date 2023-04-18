from fastapi import APIRouter
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/test",
    tags=['test']
)


@router.get('/test_endpoint')
def test():
    return {"status": "ok"}