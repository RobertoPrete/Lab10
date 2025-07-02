from database.DB_connect import DBConnect


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        from model.country import Country
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
        from model.country import Country
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

    @staticmethod
    def getAllEdges(codice_confine, anno, idMapCountries):
        from model.arco import Arco
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select dyad, state1no , state1ab , c2.StateNme, state2no , state2ab , c3.StateNme, year
                    from contiguity c
                    inner join country c2 on c.state1no = c2.CCode 
                    inner join country c3 on c.state2no = c3.CCode
                    where c.conttype=%s 
                    and `year` <= %s
                    group by c.dyad, c.state1no, c.state2no
                    order by c.dyad, c.state1no, c.state2no"""
        cursor.execute(query, (codice_confine, anno,))
        for row in cursor:
            result.append(Arco(row["dyad"], idMapCountries[row["state1no"]], idMapCountries[row["state2no"]], row["year"]))
        cursor.close()
        conn.close()
        return result


if __name__ == "__main__":
    pass
