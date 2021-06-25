import sqlite3
import shutil

from counter.model.countable import Countable
from counter.model.deal import Deal
from counter.model.event_time import Event_Time
from counter.aux.error_handling import ACHTUNG
from counter.model.index import Table_Name, Fields as f

sqlite_dir = 'sqlite3_databases'
db_files_name = (F'{sqlite_dir}/test.db', F'{sqlite_dir}/sqlite.db',
                         F'{sqlite_dir}/copy.db')

create_table_sqlite = F"""
    CREATE TABLE IF NOT EXISTS {Table_Name.deals.value}(
        {f.id.value} INTEGER PRIMARY KEY,
        {f.year.value} INTEGER NOT NULL,
        {f.month.value} TEXT NOT NULL,
        {f.day.value} INTEEGER NOT NULL,
        {f.hours.value} INTEGER NOT NULL,
        {f.minutes.value} INTEGER NOT NULL,
        {f.balance.value} TEXT NOT NULL,
        {f.type.value} TEXT NOT NULL,
        {f.source.value} TEXT NOT NULL,
        {f.category.value} TEXT NOT NULL,
        {f.product.value} TEXT NOT NULL,
        {f.cost.value} REAL NOT NULL,
        {f.amount.value} REAL NOT NULL,
        {f.total.value} REAL NOT NULL
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
                        INSERT INTO {Table_Name.deals.value} 
                            ({f.year.value}, {f.month.value}, 
                            {f.day.value}, {f.hours.value}, {f.minutes.value},
                            {f.balance.value}, {f.type.value}, 
                            {f.source.value}, {f.category.value}, 
                            {f.product.value},{f.cost.value}, 
                            {f.amount.value}, {f.total.value})
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
    return F'DELETE FROM {Table_Name.deals.value} WHERE {f.id.value}={id}'

if __name__ == '__main__':
    print (create_table_sqlite)