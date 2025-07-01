import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._countries = DAO.getAllCountries()
        self._idMapCountries = {}
        for country in self._countries:
            self._idMapCountries[country.CCode] = country
        self._nodes = None
        self._edges = None

    def buildGraph(self, anno):
        self._nodes = DAO.getAllNodes(anno)
