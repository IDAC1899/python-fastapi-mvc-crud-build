# games.py

from fastapi import APIRouter, HTTPException
from models.game_data import games_db

router = APIRouter()


@router.get("/games")
def get_games():
    # get all games
    return games_db


@router.get("/games/{game_id}")
def get_single_game(game_id: int):
    # get game by id
    for game in games_db['games']:
        if game['id'] == game_id:
            return game
    # if game with the given id is not found
    raise HTTPException(status_code=404, detail="Game not found")


@router.post("/games")
def create_game(game: dict):
    # create a new game
    games_db["games"].append(game)
    return game


@router.put("/games/{game_id}")
def update_game(game_id: int, game: dict):
    # find the game to update
    for existing_game in games_db['games']:
        if existing_game['id'] == game_id:
            # update the existing game's data
            existing_game.update(game)
            return existing_game
    # if game was not found, raise an error
    raise HTTPException(status_code=404, detail="Game not found")


@router.delete("/games/{game_id}")
def delete_game(game_id: int):
    """Delete a game by ID."""
    game = next(game for game in games_db["games"] if game["id"] == game_id)
    games_db["games"].remove(game)
    return game