from fastapi import APIRouter
from models.game_data import games_db as games_db
router = APIRouter()


@router.get("/games")
def get_games():
	"""Retrieve all games."""
	return games_db


@router.post("/games")
def create_game(game: dict):
	"""Create a new game."""
	games_db["games"].append(game)
	return game


@router.put("/games/{game_id}")
def update_game(game_id: int, game: dict):
	"""Update an existing game."""
	game = next(game for game in games_db["games"] if game["id"] == game_id)
	game.update(game)
	return game


@router.delete("/games/{game_id}")
def delete_game(game_id: int):
	"""Delete a game by ID."""
	game = next(game for game in games_db["games"] if game["id"] == game_id)
	games_db["games"].remove(game)
	return game


@router.get("/games/{game_id}")
def get_game(game_id: int):
	"""Retrieve a game by ID."""
	return next(game for game in games_db["games"] if game["id"] == game_id)
