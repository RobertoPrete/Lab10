import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._current_country = None
        self._anno = None
        self._confine = None

    def handleCalcola(self, e):
        self._anno = self._view.get_valore_anno()
        self._confine = 1
        if self._anno is None or self._anno == "" or self._anno < 1816 or self._anno > 2016 or self._anno is str:
            self._view.create_alert("Please enter a year between 1816 and 2016")
            return
        self._model.set_anno(self._anno)
        self._model.set_confine(self._confine)
        self._view.get_ddStato().visible = True
        self._view.get_btnStatiRaggiungibili.visible = True
        self._model.buildGraph(self._view.get_valore_anno())

    def fill_dd_stato(self):
        countries = self._model.countries
        for country in countries:
            self._view._ddStato.options.append(ft.dropdown.Option(key=country.CCode,
                                                                  data=country,
                                                                  on_click=self.read_dd_State))

    def read_dd_State(self, e):
        self._current_country = e.control.data
