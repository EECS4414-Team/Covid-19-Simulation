import os
from common.helpers import random_name
from simulation.person import Person
import networkx
import random


class CovidGraph():
    def __init__(self):
        self.hierarchy_graph = CountryGraph()
        self.flat_graph = self.hierarchy_graph.flattened()


class CountryGraph():
    def __init__(self):
        self.cities = self.generate_cities()

    def generate_cities(self):
        city_count = int(os.environ.get("CITY_COUNT", 5))
        graph = networkx.Graph()
        for _ in range(city_count):
            graph.add_node(random_name(), value=CityGraph())

        return graph

    def flattened(self):
        return_graph = networkx.Graph()
        for sub_graph in self.cities.nodes():
            return_graph = merge_graphs(return_graph, self.cities.nodes[sub_graph]['value'].flattened(), int(os.environ.get('CITY_EDGE_CHANCE')) / 10_000)

        return return_graph



class CityGraph():
    def __init__(self):
        self.neighborhoods = self.generate_neighborhoods()

    def generate_neighborhoods(self):
        neighborhood_count = int(os.environ.get("NEIGHBORHOOD_COUNT", 10))
        graph = networkx.Graph()
        for _ in range(neighborhood_count):
            graph.add_node(random_name(), value=NeighborhoodGraph())

        return graph

    def flattened(self):
        return_graph = networkx.Graph()
        for sub_graph in self.neighborhoods.nodes():
            return_graph = merge_graphs(return_graph, self.neighborhoods.nodes[sub_graph]['value'].flattened(), int(os.environ.get('NEIGHBORHOOD_EDGE_CHANCE')) / 10_000)

        return return_graph


class NeighborhoodGraph():
    def __init__(self):
        self.households = self.generate_households()

    def generate_households(self):
        household_count = int(os.environ.get("HOUSEHOLD_COUNT", 30))
        graph = networkx.Graph()
        for _ in range(household_count):
            graph.add_node(random_name(), value=HouseholdGraph())

        return graph

    def flattened(self):
        return_graph = networkx.Graph()
        for sub_graph in self.households.nodes():
            return_graph = merge_graphs(return_graph, self.households.nodes[sub_graph]['value'].flattened(), int(os.environ.get('HOUSEHOLD_EDGE_CHANCE')) / 10_000)

        return return_graph


class HouseholdGraph():
    def __init__(self):
        self.people = self.generate_people()

    def generate_people(self):
        person_count = int(os.environ.get("PERSON_COUNT", 5))
        household_graph = networkx.Graph()
        for _ in range(person_count):
            name = random_name()
            household_graph.add_node(name, value=Person(name))

        return household_graph

    def flattened(self):
        ret = self.people.copy()
        for node1 in ret.nodes():
            for node2 in ret.nodes():
                if node1 != node2:
                    ret.add_edge(node1, node2)

        return ret

def merge_graphs(main_graph, graph_to_add, edge_chance):
    ret = main_graph.copy()
    ret.add_nodes_from(graph_to_add.nodes())
    ret.add_edges_from(graph_to_add.edges())
    for node in graph_to_add:
        ret.nodes[node]['value'] = graph_to_add.nodes[node]['value']
    for node1 in graph_to_add.nodes():
        for node2 in main_graph.nodes():
            if random.random() < edge_chance:
                ret.add_edge(node1, node2)
    return ret




