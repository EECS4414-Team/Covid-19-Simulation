from simulation.covid_graph import CovidGraph
from simulation.simulator import Simulator
import analysis.grapher as grapher
from dotenv import load_dotenv
import networkx
import random

load_dotenv()

def main():
    random.seed(2149)
    covid_graph = CovidGraph()
    print(covid_graph.flat_graph.number_of_nodes())
    print(covid_graph.flat_graph.number_of_edges())
    print(len(max(networkx.connected_components(covid_graph.flat_graph), key=len)))
    key = list(covid_graph.flat_graph.nodes)[0]

    degrees = [val for name, val in covid_graph.flat_graph.degree]

    simulator = Simulator(covid_graph.flat_graph, covid_graph.hierarchy_graph)
    seed = 174398573985
    for type in ['NONE', 'NULL_MODEL', 'OPTIMIZED', 'OPTIMAL']:
        random.seed(seed)
        print(f'Running simulation for {type}')
        simulator.scenario('PERSON')
        simulator.intervention_scenario(type)
        simulator.simulate(1000)
        grapher.build_graph(simulator.output, type)
        grapher.build_early_infection_graph(simulator.output, type)
        simulator.reset()


if __name__ == '__main__':
    main()
