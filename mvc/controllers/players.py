''' Snooker players Controller '''

from werkzeug.exceptions import BadRequest

from ..data.players_list import snooker_players

def index(req):
    return [p for p in snooker_players], 200

def show(req, id):
    return find_by_id(id), 200

def create(req):
    new_player = req.get_json()
    new_player["id"] = sorted([p["id"] for p in snooker_players])[-1] + 1
    # len(snooker_players)-1
    snooker_players.append(new_player)
    return new_player, 201

''' Helpers '''

def find_by_id(id):
    try:
        return next(player for player in snooker_players if player["id"] == id)
    except:
        raise BadRequest(f"We do not have records for that player!")