import pytest
import app
from mvc.controllers import players

@pytest.fixture
def api(monkeypatch):
    test_players = [
        {"id": 1, "name": 'Test Player1', "nationality": 'Test_Nation_1', "stats":{"world_titles": 0, "world_ranking": 21}},
        {"id": 2, "name": 'Test Player2', "nationality": 'Test_Nation_2', "stats":{"world_titles": 5, "world_ranking": 49}},
    ]
    monkeypatch.setattr(players, "snooker_players", test_players)
    api = app.app.test_client()
    return api