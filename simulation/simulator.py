import random
import simulation.global_state as global_state

class Simulator():

    def __init__(self, covid_graph):
        self.covid_graph = covid_graph
        self.person_list = [covid_graph.nodes[x]['value'] for x in covid_graph.nodes()]
        global_state.covid_graph = self.covid_graph
        global_state.cycle_number = 0

    def scenario(self, scenario_type):
        if scenario_type == 'PERSON':
            person = random.choice(self.person_list)
            person.current_state = 'INFECTED'
            person.healthy_after_date = 10


    def step(self):
        for person in self.person_list:
            person.iterate()

    def update_people(self):
        for person in self.person_list:
            person.update_state()

    def simulate(self, number_of_steps=100):
        for i in range(number_of_steps):
            global_state.cycle_number += 1
            self.step()
            self.update_people()


