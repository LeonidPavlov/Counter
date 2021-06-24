import sqlite3

from counter.sqlite_user.crud import db_files_name
from counter.aux.error_handling import ACHTUNG

def selection_query(file:str = db_files_name[1], 
                    sql_query:str = 'SELECT * FROM DEALS') -> list:
    try:
        conn = sqlite3.connect(file)
        if conn != None:
            cursor = conn.cursor()
            cursor.execute(sql_query)
            result = cursor.fetchall()
            conn.close()
            return result
    except (sqlite3.Error, Exception) as err:
        ACHTUNG(err, __file__, 'execute query method')
    finally:
        conn.close()

def set_from_column(column_number:int = 0) -> set:
    list_of_tuples:list = selection_query(db_files_name[0])
    list_from_column:list = []
    for item in list_of_tuples:
        list_from_column.append( item[column_number] )
    return set(list_from_column)
