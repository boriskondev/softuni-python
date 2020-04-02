from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, username, health):
        self.username = username
        self.health = health
        self.card_repository = 0  # Should be added when the class in created
        self.is_dead = bool

    # Do I need to have @abstractmethod here?
    @property
    def username(self):
        return self.__username

    # Do I need to have @abstractmethod here?
    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Player's username cannot be an empty string.")
        self.__username = value

    # Do I need to have @abstractmethod here?
    @property
    def health(self):
        return self.__health

    # Do I need to have @abstractmethod here?
    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero. ")
        self.__health = value

'''
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value
'''