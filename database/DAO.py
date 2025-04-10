from database.DB_connect import DBConnect
from model.GoRetailers import GoRetailers


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnniVendite():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT DISTINCT YEAR(date) as year 
                    FROM go_daily_sales g
                    ORDER BY year"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row[0])

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getBrandProdotti():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT  DISTINCT gp.Product_brand
                   FROM go_products gp"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row[0])

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getRetailers():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT 
                Retailer_code AS retailer_code,
                Retailer_name AS retailer_name,
                Type AS type,
                Country AS country
            FROM go_retailers
        """
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(GoRetailers(**row))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getTopFiveVendite(anno, brand, retailer_code):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)


        query = """SELECT 
                gds.`Date`, gds.Unit_sale_price, gds.Quantity,
                gp.Product_number, gp.Product , gp.Product_brand,
                gr.Retailer_code, gr.Retailer_name,
                gds.Unit_sale_price * gds.Quantity AS ricavo
            FROM go_daily_sales gds
            JOIN go_products gp ON gds.Product_number = gp.Product_number
            JOIN go_retailers gr ON gds.Retailer_code = gr.Retailer_code
            WHERE gp.Product_brand = COALESCE(%s, gp.Product_brand)
              AND YEAR(gds.`Date`) = COALESCE(%s, YEAR(gds.`Date`))
              AND gr.Retailer_code = COALESCE(%s, gr.Retailer_code)
            ORDER BY ricavo DESC
            LIMIT 5"""
        cursor.execute(query, (brand,anno, retailer_code))

        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()

        return res


    @staticmethod
    def getVenditeAnalisi(anno, brand, retailer_code):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query ="""SELECT gds.Quantity* gds.Unit_sale_price as ricavo, 
                           gds.Product_number, gds.Retailer_code
                    FROM go_daily_sales gds 
                    JOIN go_products gp ON gp.Product_number = gds.Product_number
                    JOIN go_retailers gr ON gr.Retailer_code = gds.Retailer_code
                     WHERE gp.Product_brand = COALESCE(%s, gp.Product_brand)
                   AND YEAR(gds.`Date`) = COALESCE(%s, YEAR(gds.`Date`))
                   AND gr.Retailer_code = COALESCE(%s, gr.Retailer_code)"""



        cursor.execute(query,(brand, anno, retailer_code))

        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()

        return res





if __name__ == '__main__':
    #top_vendite = DAO.getTopFiveVendite(2017,'Star',1309 )
    #print(top_vendite)
    vendite = DAO.getVenditeAnalisi(2017,'Star',1309)
    print(vendite)
    tot = 0.0
    retailer = set()
    prodotti = set()
    for vendita in vendite:
        tot += float(vendita['Ricavo'])
        retailer.add(vendita['Retailer_code'])
        prodotti.add(vendita['Product_number'])
    print(tot)
    print(len(retailer))
    print(len(prodotti))



