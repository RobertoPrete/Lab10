import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        if self._view._txtAnno.value is None or self._view._txtAnno.value == "" or self._view._txtAnno.value < 1816 or self._view._txtAnno.value > 2016 or self._view._txtAnno.value is str:
            self._view.create_alert("Please enter a year between 1816 and 2016")
            return
        self._model.buildGraph(anno)
