import random
import os
import simulation.global_state as global_state

class Person():
    STATES = ["HEALTHY", "INFECTED", "IMMUNE", "DEAD"]

    def __init__(self, name):
        self.name = name
         # average death rate * random value between [0, 2*avg]
        self.chance_of_death = float(os.environ.get('VIRUS_DEATH_RATE', '0.2')) * 2 * random.random()
        # likelihood of catching the virus if exposured
        self.chance_to_catch_virus = float(os.environ.get('VIRUS_CATCH_RATE', '0.4')) * 2 * random.random()
        # likelihood of exposing someone else to the virus
        self.chance_to_spread_virus = float(os.environ.get('VIRUS_SPREAD_RATE', '0.3')) * 2 * random.random()
        # how social a person is, as a percentage of neighbors they will see that day
        self.sociability = float(os.environ.get('SOCIABILITY_AVERAGE', '0.4')) * 2 * random.random()
        self.healthy_after_date = -1
        self.not_immune_after = -1
        self.antisocial = False
        self.current_state = 'HEALTHY'
        self.future_state = 'HEALTHY'

    def reset(self):
        self.healthy_after_date = -1
        self.not_immune_after = -1
        self.antisocial = False
        self.current_state = 'HEALTHY'
        self.future_state = 'HEALTHY'


    # iterate through neighbors and perform action
    def iterate(self):
        if self.current_state == 'IMMUNE':
            if self.not_immune_after < global_state.cycle_number:
                self.future_state = 'HEALTHY'
        if self.current_state == 'INFECTED':
            if self.check_if_illness_gone():
                return
            if self.roll_to_die():
                return
            neighbor_list = [global_state.covid_graph.nodes[x]['value'] for x in global_state.covid_graph.neighbors(self.name)]
            for neighbor in neighbor_list:
                if random.random() < (self.sociability if not self.antisocial else self.sociability / 10):
                    self.roll_to_infect(neighbor)


    def check_if_illness_gone(self):
        if self.healthy_after_date < global_state.cycle_number:
            self.future_state = 'IMMUNE'
            self.not_immune_after = global_state.cycle_number + int(random.random() * 2 * int(os.environ.get('IMMUNITY_PERIOD', '180')))
            return True
        return False

    def roll_to_die(self):
        if random.random() < self.chance_of_death / int(os.environ.get('INFECTION_LENGTH', '7')):
            self.current_state = 'DEAD'
            self.future_state = 'DEAD'
            return True
        return False

    def roll_to_infect(self, neighbor):
        if neighbor.current_state != 'HEALTHY':
            return
        if random.random() < self.chance_to_spread_virus:
            # successful roll to spread
            if random.random() < neighbor.chance_to_catch_virus:
                # successfully exposed to viral load
                neighbor.infect()

    def infect(self):
        self.future_state = 'INFECTED'
        self.healthy_after_date = global_state.cycle_number + int(int(os.environ.get('INFECTION_LENGTH', '7')) * random.random())

    def update_state(self):
        self.current_state = self.future_state





