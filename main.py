from simulation.covid_graph import CovidGraph
from simulation.simulator import Simulator
import analysis.grapher as grapher
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
    simulator.simulate(10000)
    grapher.build_graph(simulator.output)






if __name__ == '__main__':
    main()
