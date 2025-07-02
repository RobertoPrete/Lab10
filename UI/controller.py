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
        try:
            # self._anno = int(self._view.get_valore_anno())
            self._anno = int(self._view._txtAnno.value)
        except ValueError:
            self._view.create_alert("Please enter a year between 1816 and 2016")
        self._confine = 1
        if self._anno is None or self._anno == "" or self._anno < 1816 or self._anno > 2016:
            self._view.create_alert("Please enter a year between 1816 and 2016")
            return
        self._model.set_anno(self._anno)
        self._model.set_confine(self._confine)
        # self._view.get_ddStato().visible = True
        self._view._ddStato.visible = True
        # self._view.get_btnStatiRaggiungibili.visible = True
        self._view._btnStatiRaggiungibili.visible = True
        self._view.update_page()
        self._model.buildGraph(self._anno)

    def fill_dd_stato(self):
        countries = self._model.countries
        for country in countries:
            self._view.get_ddStato.options.append(ft.dropdown.Option(key=country.CCode,
                                                                     data=country,
                                                                     on_click=self.read_dd_State))

    def read_dd_State(self, e):
        self._current_country = e.control.data
