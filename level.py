import json
from game_object import GameObject
from collider import Collider

class Level():
    """
    Stores utility functions that handle level saving and loading.
    """

    @staticmethod
    def save(filePath: str):
        """
        Saves the level to a file.

        Parameters:
            filePath (str):
        """
        with open(filePath,"w") as file:
            data: dict = {}
            data["GameObject"] = GameObject.serialize_all()
            data["Collider"] = Collider.serialize_all(data["GameObject"])
            json.dump(data,file)

    @staticmethod
    def load(filePath: str):
        """
        Loads the level from a file.

        Parameters:
            filePath (str):
        """
        GameObject.destroy_all()
        Collider.destroy_all()
        with open(filePath,"r") as file:
            data = json.load(file)
            GameObject.deserialize_all(data["GameObject"])
            Collider.deserialize_all(data["Collider"])
