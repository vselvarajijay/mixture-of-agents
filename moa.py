
from agent import Agent
from response import Response

class MoA:


    def __init__(self, layers=0, agents: [Agent] = []):
        self.layers = layers
        self.agents = agents


    def run(self):

        for layer in range(self.layers):
            for agent in self.agents:
                agent.run()

        return prompt