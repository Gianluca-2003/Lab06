import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Analisi vendite"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddAnni = None
        self.ddBrand = None
        self.ddRetailers = None
        self.analizzaVenditeBtn = None
        self.topVenditeBtn = None
        self.txtOut = None



    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddAnni = ft.Dropdown(label="Anno",
                                  width=self._page.width*0.20,
                                  options=[ft.dropdown.Option("Nessun filtro")])
        self._controller.fillDDAnni()

        self.ddBrand = ft.Dropdown(label="Brand",
                                   width=self._page.width*0.20,
                                   options=[ft.dropdown.Option("Nessun filtro")])
        self._controller.fillDDBrand()

        self.ddRetailers = ft.Dropdown(label="Retailer",width=self._page.width*0.55,
                                       options=[ft.dropdown.Option("Nessun filtro")])

        self._controller.fillDDRetailer()


        row1 = ft.Row([self.ddAnni, self.ddBrand, self.ddRetailers])
        #self._page.add(row1)
        self.analizzaVenditeBtn = ft.ElevatedButton(text="Analizza vendite",
                                                    on_click=self._controller.handleAnalizzaVendite)

        self.topVenditeBtn = ft.ElevatedButton(text="Top vendite",
                                               on_click=self._controller.handleTopVendite)

        row2 = ft.Row([self.analizzaVenditeBtn, self.topVenditeBtn], alignment=ft.MainAxisAlignment.CENTER)

        self.txtOut = ft.ListView()


        self._page.add(row1,row2, self.txtOut)


        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
