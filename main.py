from fastapi import FastAPI
from controllers.games import router as GamesRouter

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'welcome to game world!'}


app.include_router(GamesRouter, prefix="/api")

