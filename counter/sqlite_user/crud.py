import sqlite3
import shutil

from counter.model.countable import Countable
from counter.model.deal import Deal
from counter.model.event_time import Event_Time
from counter.aux.error_handling import ACHTUNG

sqlite_dir = 'sqlite3_databases'
db_files_name = (F'{sqlite_dir}/test.db', F'{sqlite_dir}/sqlite.db',
                         F'{sqlite_dir}/copy.db')

column_number: dict = { 'DEAL_ID': 0,
                        'YEAR': 1, 'MONTH': 2, 'DAY':3,
                        'HOURS': 4,'MINUTES': 5,
                        'BALANCE': 6, 'TYPE': 7, 'SOURCE': 8,
                        'CATEGORY': 9, 'PRODUCT': 10,
                        'COST': 11, 'AMOUNT': 12, 'TOTAL': 13}

create_table_sqlite = F"""
    CREATE TABLE IF NOT EXISTS DEALS(
        DEAL_ID INTEGER PRIMARY KEY,
        YEAR INTEGER NOT NULL,
        MONTH TEXT NOT NULL,
        DAY INTEEGER NOT NULL,
        HOURS INTEGER NOT NULL,
        MINUTES INTEGER NOT NULL,
        BALANCE TEXT NOT NULL,
        TYPE TEXT NOT NULL,
        SOURCE TEXT NOT NULL,
        CATEGORY TEXT NOT NULL,
        PRODUCT TEXT NOT NULL,
        COST REAL NOT NULL,
        AMOUNT REAL NOT NULL,
        TOTAL REAL NOT NULL
    );
"""

def exectution_query(file:str = db_files_name[1],
                     sql_query:str = '') -> bool:
    try:
        truth:bool = False
        conn = sqlite3.connect(file)
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(sql_query)
            conn.commit()
            conn.close()
            return True
    except (sqlite3.Error, Exception) as err:
        ACHTUNG(err, __file__, 'execute query method')
        return False
    finally:
        conn.close()


def insert_query(deal: Deal = Deal()) -> str:
    return F"""
                        INSERT INTO DEALS (YEAR, MONTH, DAY, HOURS, MINUTES,
                            BALANCE, TYPE, SOURCE, CATEGORY, PRODUCT,
                            COST, AMOUNT, TOTAL)
                            VALUES 
                            (
                                {deal.event_time().event_year()},
                                {deal.event_time().event_month()},
                                {deal.event_time().event_day()},
                                {deal.event_time().event_hour()},
                                {deal.event_time().event_minute()},
                                \"{deal.balance()}\",
                                \"{deal.type()}\",
                                \"{deal.source()}\",
                                \"{deal.category()}\",
                                \"{deal.product()}\",
                                {deal.countable().cost()},
                                {deal.countable().amount()},
                                {deal.countable().total()}
                            );
                        """

def delete_by_id_query(id:int = 1) -> str:
    return F'DELETE FROM DEALS WHERE DEAL_ID={id}'
