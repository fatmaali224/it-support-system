class Task:
    def __init__(self, description):
        self.description = description


class Agent:
    def __init__(self, name):
        self.name = name


class DiagnosisAgent(Agent):
    def process(self, task):
        desc = task.description.lower()

        if "slow" in desc:
            return "Problem: performance"
        elif "internet" in desc:
            return "Problem: network"
        else:
            return "Problem: unknown"


class SolutionAgent(Agent):
    def process(self, task):
        desc = task.description.lower()

        if "slow" in desc:
            return "Solution: clean files and restart"
        elif "internet" in desc:
            return "Solution: restart router"
        else:
            return "Solution: check system settings"


class TicketAgent(Agent):
    counter = 100

    def process(self, task):
        TicketAgent.counter += 1
        return f"Ticket ID: {TicketAgent.counter}"


class Founder:
    def create_task(self):
        problem = input("Enter your problem: ")
        return Task(problem)

    def process(self, task, agents):
        print("\n--- Processing ---\n")
        results = []

        for agent in agents:
            result = agent.process(task)
            print(f"{agent.name}: {result}")
            results.append(result)

        return results

    def decision(self, results):
        print("\n--- Final Decision ---")
        for r in results:
            if "Solution" in r:
                print("Approved ->", r)


agents = [
    DiagnosisAgent("Diagnosis Agent"),
    SolutionAgent("Solution Agent"),
    TicketAgent("Ticket Agent")
]

founder = Founder()

task = founder.create_task()
results = founder.process(task, agents)
founder.decision(results)