import random
import simulation.global_state as global_state

class Simulator():

    def __init__(self, covid_graph):
        self.covid_graph = covid_graph
        self.person_list = [covid_graph.nodes[x]['value'] for x in covid_graph.nodes()]
        global_state.covid_graph = self.covid_graph
        global_state.cycle_number = 0
        self.output = []

    def scenario(self, scenario_type):
        if scenario_type == 'PERSON':
            person = random.choice(self.person_list)
            person.infect()


    def step(self):
        for person in self.person_list:
            person.iterate()

    def update_people(self):
        for person in self.person_list:
            person.update_state()

    def simulate(self, number_of_steps=100):
        for i in range(number_of_steps):
            self.update_people()
            global_state.cycle_number += 1
            self.add_stats()
            if all([person.current_state != 'INFECTED' for person in self.person_list]):
                print(f'after {i} cycles the infection has stopped')
                break
            self.step()

    def add_stats(self):
        self.output.append(
            (
                len([x for x in self.person_list if x.current_state == 'HEALTHY']),
                len([x for x in self.person_list if x.current_state == 'INFECTED']),
                len([x for x in self.person_list if x.current_state == 'DEAD']),
                len([x for x in self.person_list if x.current_state == 'IMMUNE'])
            )
        )


