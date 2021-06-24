import os
import pytest

from counter.model.countable import Countable
from counter.model.event_time import Event_Time
from counter.sqlite_user import selection
from counter.sqlite_user.crud import exectution_query, insert_query\
                , db_files_name, create_table_sqlite
from counter.model.deal import Deal, Event_Time, Countable


d1 = Deal(0,Event_Time(2021,3, 15),Countable(3, 5, 15),Deal.balance_type[0],
            'loan', 'zoya viktorovna', 'no return','rub')

d2 = Deal(0,Event_Time(2021,3, 15),Countable(3, 5, 15),Deal.balance_type[1],
            'purchase', 'zoya viktorovna', 'no return','euro')

d3 = Deal(0,Event_Time(2022,3, 15),Countable(3, 5, 15),Deal.balance_type[2],
            'loan', 'ebumba', 'no return','euro')

d4 = Deal(0,Event_Time(2021,3, 15),Countable(3, 5, 15),Deal.balance_type[0],
            'buy', 'zoya viktorovna', 'return','rub')

d5 = Deal(0,Event_Time(2023,5, 15),Countable(3, 5, 15),Deal.balance_type[1],
            'loan', 'sosimba', 'return','usd')

d6 = Deal(0,Event_Time(2024,3, 16),Countable(3, 5, 15),Deal.balance_type[2],
            'purchase', 'zoya viktorovna', 'no return','rub')

d7 = Deal(0,Event_Time(2021,5, 25),Countable(3, 5, 15),Deal.balance_type[0],
            'loan', 'zoya viktorovna', 'return','usd')

d8 = Deal(0,Event_Time(2021,3, 25),Countable(3, 5, 15),Deal.balance_type[1],
            'loan', 'zoya viktorovna', 'no return','rub')

d9 = Deal(0,Event_Time(2021,3, 25),Countable(3, 5, 15),Deal.balance_type[2],
            'loan', 'zoya viktorovna', 'no return','rub')

d10 = Deal(0,Event_Time(2021,3, 15),Countable(3, 5, 15),Deal.balance_type[0],
            'loan', 'zoya viktorovna', 'no return','rub')

query = (d1, d2, d3, d4, d5, d6, d7, d8, d9, d10)

def test_insertion() -> None:
    exectution_query(db_files_name[0], create_table_sqlite)
    for j in query:
        assert( exectution_query(db_files_name[0],insert_query(j)) == True )


def test_all_selection() -> None:
    hren: list = {} 
    hren = selection.selection_query(db_files_name[0])
    assert (len(hren) == 10)

# NEED TO TESTING SET FROM COLUMN

def test_remove_db() -> None:
    os.system(f'rm {db_files_name[0]}')