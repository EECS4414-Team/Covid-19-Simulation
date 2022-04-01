import random
import simulation.global_state as global_state

class Simulator():

    intervention_types = ['NONE', 'NULL_MODEL', 'OPTIMIZED']

    def __init__(self, covid_graph):
        self.covid_graph = covid_graph
        self.person_list = [covid_graph.nodes[x]['value'] for x in covid_graph.nodes()]
        self.person_dict = {person.name: person for person in self.person_list}
        global_state.covid_graph = self.covid_graph
        global_state.cycle_number = 0
        self.output = []
        self.intervention_type = 'NULL'
        self.intervention_status = False

    def reset(self):
        global_state.covid_graph = self.covid_graph
        global_state.cycle_number = 0
        for person in self.person_list:
            person.reset()

        self.output = []
        self.intervention_type = 'NULL'
        self.intervention_status = False




    def scenario(self, scenario_type):
        if scenario_type == 'PERSON':
            person = random.choice(self.person_list)
            person.infect()

    def intervention_scenario(self, type):
        self.intervention_type = type


    def step(self):
        for person in self.person_list:
            person.iterate()

    def update_people(self):
        for person in self.person_list:
            person.update_state()

    def simulate(self, number_of_steps=100):
        print('beginning simulation')
        one_tenth = number_of_steps // 10
        for i in range(number_of_steps):
            if i % one_tenth == 0:
                print(f'current step number {i}')
            self.check_for_intervention()
            self.update_people()
            global_state.cycle_number += 1
            self.add_stats()
            if all([person.current_state != 'INFECTED' for person in self.person_list]):
                print(f'after {i} cycles the infection has stopped')
                break
            self.step()

    def check_for_intervention(self):
        num_infected = len([person for person in self.person_list if person.current_state == 'INFECTED' or person.future_state == 'INFECTED'])
        print(f'{num_infected}', end='\r')
        if  num_infected > 100:
            if self.intervention_status == False:
                self.social_intervention()
                self.intervention_status = True

        if num_infected <= 100:
            if self.intervention_status == True:
                self.ease_social_intervention()
                self.intervention_status = False


    def social_intervention(self):
        if self.intervention_type == 'NONE':
            # do nothing
            return
        elif self.intervention_type == 'NULL_MODEL':
            for person in self.person_list:
                person.antisocial == True
        elif self.intervention_type == 'OPTIMIZED':
            top_100 = sorted(list(global_state.covid_graph.degree), key=lambda x: x[1])[:100]
            for person, _ in top_100:
                self.person_dict[person].antisocial = True

    def ease_social_intervention(self):
        if self.intervention_type == 'NONE':
            # do nothing
            return
        elif self.intervention_type == 'NULL_MODEL':
            for person in self.person_list:
                person.antisocial == False
        elif self.intervention_type == 'OPTIMIZED':
            top_100 = sorted(list(global_state.covid_graph.degree), key=lambda x: x[1])[:100]
            for person, _ in top_100:
                self.person_dict[person].antisocial = False




    def add_stats(self):
        self.output.append(
            (
                len([x for x in self.person_list if x.current_state == 'HEALTHY']),
                len([x for x in self.person_list if x.current_state == 'INFECTED']),
                len([x for x in self.person_list if x.current_state == 'DEAD']),
                len([x for x in self.person_list if x.current_state == 'IMMUNE'])
            )
        )


