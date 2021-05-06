''' Snooker player model '''

from ..data.players_list import snooker_players 

class Player():
    all = []

    def __init__(self, data):
        self._id = data["id"],
        self._name = data["name"],
        self._nationality = data["nationality"],
        self._stats = data["stats"]
        self._save()

    def _save(self):
        self.all.append(self)

        
    def get_all(self):
        all.append(p for p in snooker_players)
        return all
    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @property
    def nationality(self):
        return self._nationality

    @property
    def stats(self):
        return self._stats