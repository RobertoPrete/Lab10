import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._idMapCountries = {}
        self.countries = DAO.getAllCountries()

        self._nodes = None
        self._edges = None
        self._anno = None
        self._confine = None  # indica attraverso un numero intero il tipo di confine

    @property
    def getAnno(self):
        return self._anno

    def set_anno(self, value):
        self._anno = value

    @property
    def getConfine(self):
        return self._confine

    def set_confine(self, value):
        self._confine = value

    def buildGraph(self, anno):
        self._graph.clear()
        for country in self.countries:
            self._idMapCountries[country.CCode] = country
        self._nodes = DAO.getAllNodes(anno)
        self._graph.add_nodes_from(self._nodes)
        self._edges = DAO.getAllEdges(self._confine, self._anno, self._idMapCountries)
        lista_archi = []
        for edge in self._edges:
            if edge not in lista_archi:
                lista_archi.append(edge)
        for arco in lista_archi:
            self._graph.add_edge(arco.c1, arco.c2)

    def getNumCompConnesse(self):
        return nx.number_connected_components(self._graph)

    def graphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getNumConfinanti(self, nodo):
        return len(list(self._graph.neighbors(nodo)))

    def getNodes(self):
        return self._nodes


