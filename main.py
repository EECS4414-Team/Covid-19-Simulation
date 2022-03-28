from simulation.covid_graph import CovidGraph
from simulation.simulator import Simulator
from dotenv import load_dotenv
import networkx

load_dotenv()

def main():
    covid_graph = CovidGraph()
    print(covid_graph.flat_graph.number_of_nodes())
    print(covid_graph.flat_graph.number_of_edges())
    print(len(max(networkx.connected_components(covid_graph.flat_graph), key=len)))
    key = list(covid_graph.flat_graph.nodes)[0]


    simulator = Simulator(covid_graph.flat_graph)
    simulator.scenario('PERSON')
    simulator.simulate()

    print(
        len(
            [x for x in simulator.person_list if x.current_state == 'HEALTHY']
        )
    )

    print(
        len(
            [x for x in simulator.person_list if x.current_state == 'INFECTED']
        )
    )

    print(
        len(
            [x for x in simulator.person_list if x.current_state == 'DEAD']
        )
    )

    print(
        len(
            [x for x in simulator.person_list if x.current_state == 'IMMUNE']
        )
    )






if __name__ == '__main__':
    main()
