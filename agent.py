from typing import Any
from model_services import Model
from response import Response



class Expertise:

    pass

class Agent:

    """
    @param model: The model that the agent uses to make decisions
    @param expertise: The expertise the agent has
    """
    def __init__(self, model: Model, expertise: Expertise):
        self.model = model
        self.expertise = expertise


    def run(self) -> Response:
        pass
