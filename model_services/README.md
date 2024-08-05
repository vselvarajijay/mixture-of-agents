# Mixture of Agents

MoA Service designed from the approach referenced here: https://arxiv.org/pdf/2406.04692




```python
from moa import MoA, Agent

agent1 = Agent(model='')
agent2 = Agent(model='')
agent3 = Agent(model='')

moa = MoA(agents=[agent1, agent2, agent3], layers=3)
result = moa.run()

```
