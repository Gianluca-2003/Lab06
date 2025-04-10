from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAnniVendite(self):
        return DAO.getAnniVendite()

    def getBrandProdotti(self):
        return DAO.getBrandProdotti()

    def getRetailers(self):
        return DAO.getRetailers()

    def getTopFiveVendite(self, anno, brand, retailer_code):
        return DAO.getTopFiveVendite(anno, brand, retailer_code)

    def getVenditeAnalisi(self, anno, brand, retailer_code):
        return DAO.getVenditeAnalisi(anno, brand, retailer_code)