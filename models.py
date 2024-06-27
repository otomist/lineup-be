from pydantic import BaseModel

class Step(BaseModel):
    agentName: str
    x: int
    y: int

class Strategy(BaseModel):
    title: str
    steps: list[Step]
    # def model_dump(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "steps": [step.dict() for step in self.steps]
    #     }