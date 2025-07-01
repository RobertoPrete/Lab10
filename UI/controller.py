import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._current_country = None

    def handleCalcola(self, e):
        if self._view._txtAnno.value is None or self._view._txtAnno.value == "" or self._view._txtAnno.value < 1816 or self._view._txtAnno.value > 2016 or self._view._txtAnno.value is str:
            self._view.create_alert("Please enter a year between 1816 and 2016")
            return
        self._view._ddStato.visible = True
        self._view._btnStatiRaggiungibili.visible = True
        self._model.buildGraph(self._view._txtAnno.value)

    def fill_dd_stato(self):
        countries = self._model.countries
        for country in countries:
            self._view._ddStato.options.append(ft.dropdown.Option(key=country.CCode,
                                                                  data=country,
                                                                  on_click=self.read_dd_State))

    def read_dd_State(self, e):
        self._current_country = e.control.data
