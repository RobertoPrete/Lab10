from dataclasses import dataclass

from model.country import Country


@dataclass
class Arco:
    dyad: int
    c1: Country
    c2: Country
    year: int

    def __hash__(self):
        return hash(self.dyad)

    def __eq__(self, other):
        return self.dyad == other.dyad

    def __str__(self):
        return f"Confine numero: {self.dyad} tra paese 1: {self.c1.StateNme} e paese 2: {self.c2.StateNme}. Anno: {self.year}"
