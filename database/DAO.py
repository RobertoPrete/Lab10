from database.DB_connect import DBConnect
from model.country import Country


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select * from country c """
        cursor.execute(query)
        for row in cursor:
            result.append(Country(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select c2.*
                    from contiguity c , country c2 
                    where c.state1no = c2.CCode and c.`year`<= %s
                    group by c2.CCode"""
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Country(**row))
        cursor.close()
        conn.close()
        return result

