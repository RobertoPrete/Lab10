import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self.countries = DAO.getAllCountries()
        self._idMapCountries = {}
        for country in self.countries:
            self._idMapCountries[country.CCode] = country
        self._nodes = None
        self._edges = None

    def buildGraph(self, anno):
        self._graph.clear()
        self._nodes = DAO.getAllNodes(anno)
        self._graph.add_nodes_from(self._nodes)

