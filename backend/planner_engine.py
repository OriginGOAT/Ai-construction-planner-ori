from backend.task_decomposer import decompose
from backend.constraint_engine import validate
from backend.scheduler_engine import optimize
from backend.weather_api import weather
from backend.mitigation_engine import mitigate
from backend.team_allocator import allocate
from backend.productivity import timeline_cost
from backend.monte_carlo import simulate

class PlannerEngine:

    def __init__(self,state):
        self.state=state

    def plan(self,user_input):

        tasks=decompose(self.state.project_type)

        issues=validate(tasks,self.state.resources)

        schedule=optimize(tasks)

        weather_risk=weather(self.state.location)

        mitigation=mitigate(issues)

        team=allocate(self.state.resources.get("workers",0))

        time_cost=timeline_cost(tasks)

        delay=simulate()

        return {
            "tasks":tasks,
            "schedule":schedule,
            "issues":issues,
            "weather":weather_risk,
            "mitigation":mitigation,
            "team":team,
            "timeline":time_cost,
            "delay":delay
        }
