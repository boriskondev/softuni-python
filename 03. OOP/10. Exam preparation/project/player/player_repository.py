from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.players = []

    @property
    def count(self):
        return len(self.players)

    def add(self, player: Player):
        for current_player in self.players:
            if current_player.username == player.username:
                raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    def remove(self, player_name: str):
        if player_name == "":
            raise ValueError("Player cannot be an empty string!")
        found_player = self.find(player_name)
        self.players.remove(found_player)

    def find(self, username):
        for current_player in self.players:
            if current_player.username == username:
                return current_player