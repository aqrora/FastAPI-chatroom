from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from .routers import test
from routers import test

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test.router)


@app.get("/")
def root():
    return {"message": "Hello World"}