import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def checkCampiPieni(self):
        anno = self._view.ddAnni.value
        brand = self._view.ddBrand.value
        retailers = self._view.ddRetailers.value
        if anno is None:
            #self._view.txtOut.controls.append(ft.Text("Selezionare un anno", color="red"))
            self._view.create_alert("Selezionare un anno")
            self._view.update_page()
            return False
        if brand is None:
            #self._view.txtOut.controls.append(ft.Text("Selezionare un brand", color="red"))
            self._view.create_alert("Selezionare un brand")
            self._view.update_page()
            return False
        if retailers is None:
            #self._view.txtOut.controls.append(ft.Text("Selezionare un retailer", color="red"))
            self._view.create_alert("Selezionare un retailer")
            self._view.update_page()
            return False
        return True

    def checkFiltri(self):
        if self._view.ddAnni.value == "Nessun filtro" or self._view.ddAnni.value is None:
            anno = None
        else:
            anno = int(self._view.ddAnni.value)
        if self._view.ddBrand.value == "Nessun filtro" or self._view.ddBrand.value is None :
            brand = None
        else:
            brand = self._view.ddBrand.value
        if self._view.ddRetailers.value == "Nessun filtro" or self._view.ddRetailers.value is None:
            retailers_code = None
        else:
            retailers_code = int(self._view.ddRetailers.value)

        return anno, brand, retailers_code



    def handleAnalizzaVendite(self,e):
        self._view.txtOut.controls.clear()
        if not self.checkCampiPieni():
            return
        #self.checkCampiPieni()
        campi = self.checkFiltri()
        anno = campi[0]
        brand = campi[1]
        retailers_code = campi[2]
        top_vendite = self._model.getTopFiveVendite(anno, brand, retailers_code)
        if(len(top_vendite)== 0):
            print("Lista vuota")
            self._view.txtOut.controls.append(ft.Text("Non ci sono vendite disponibili per questi filtri", color="red"))
            self._view.update_page()
            return
        for v in top_vendite:
            self._view.txtOut.controls.append(ft.Text(f"{v['Date']} - {v['Product']} - {v['Retailer_name']} | "
                      f"Quantità: {v['Quantity']} | Prezzo unitario: {v['Unit_sale_price']} | "
                      f"Ricavo: {v['ricavo']:.2f}", color= "blue"))
        self._view.update_page()




    def handleTopVendite(self,e):
        self._view.txtOut.controls.clear()
        if not self.checkCampiPieni():
            return
        #self.checkCampiPieni()
        campi = self.checkFiltri()
        anno = campi[0]
        brand = campi[1]
        retailers_code = campi[2]
        vendite_analisi = self._model.getTopFiveVendite(anno, brand, retailers_code)
        if(len(vendite_analisi)== 0):
            print("Lista vuota")
            self._view.txtOut.controls.append(ft.Text("Non ci sono vendite disponibili per questi filtri", color="red"))
            self._view.update_page()
            return
        ricavi_tot = 0.0
        retailer = set()
        prodotti = set()
        for vendita in vendite_analisi:
            ricavi_tot += int(vendita['ricavo'])
            retailer.add(vendita['Retailer_code'])
            prodotti.add(vendita['Product_number'])
        n_vendite = len(vendite_analisi)
        n_retailer = len(retailer)
        n_prodotti = len(prodotti)
        self._view.txtOut.controls.append(ft.Text(f"Statistiche vendita:\n"
                                                  f"Ricavi totali: {ricavi_tot}\n"
                                                  f"Numero di vendite: {n_vendite}\n"
                                                  f"Numero di retailer coinvolti: {n_retailer}\n"
                                                  f"Numero di prodotti coinvolti: {n_prodotti}\n:", color="blue"))
        self._view.update_page()





    def fillDDAnni(self):
        anni = self._model.getAnniVendite()
        for anno in anni:
            self._view.ddAnni.options.append(ft.dropdown.Option(anno))


    def fillDDBrand(self):
        brand = self._model.getBrandProdotti()
        for b in brand:
            self._view.ddBrand.options.append(ft.dropdown.Option(b))

    def fillDDRetailer(self):
        retailer = self._model.getRetailers()
        for r in retailer:
            self._view.ddRetailers.options.append(
                ft.dropdown.Option(
                    key = str(r.retailer_code),
                    text=r.retailer_name,
                    data=r,
                    on_click=self.read_retailer
                )
            )


    def read_retailer(self,e):
        self._selectedRetailer = e.control.data




