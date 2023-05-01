from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, users, messages, channels


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(routers.test)
app.include_router(users.router)
app.include_router(messages.router)
app.include_router(channels.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World"}