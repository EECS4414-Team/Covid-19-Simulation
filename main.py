from simulation.covid_graph import CovidGraph
from dotenv import load_dotenv

load_dotenv()

def main():
    covid_graph = CovidGraph()
    print(covid_graph.flat_graph.number_of_nodes())
    print(covid_graph.flat_graph.number_of_edges())

if __name__ == '__main__':
    main()
