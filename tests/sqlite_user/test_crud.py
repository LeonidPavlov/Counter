import os

from counter.sqlite_user.crud import delete_by_id_query, exectution_query,\
                        db_files_name, create_table_sqlite, insert_query,\
                            column_number
from counter.model.deal import Deal

testing_create_table_sqlite = F"""
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
test_column_number: dict = { 'DEAL_ID': 0,
                        'YEAR': 1, 'MONTH': 2, 'DAY':3,
                        'HOURS': 4,'MINUTES': 5,
                        'BALANCE': 6, 'TYPE': 7, 'SOURCE': 8,
                        'CATEGORY': 9, 'PRODUCT': 10,
                        'COST': 11, 'AMOUNT': 12, 'TOTAL': 13}

def test_col_number() -> None:
    test_keys = list(test_column_number.keys())
    real_keys = list(column_number.keys())
    for j in range( len(test_column_number) ):
        assert (test_keys[j] == real_keys[j])        

def test_col_number_values() -> None:
    test_keys = list(test_column_number.keys())
    real_keys = list(column_number.keys())
    for j in range( len(column_number)):
        assert(column_number[real_keys[j]] \
                == test_column_number[test_keys[j]])

def test_create_database() -> None:
    assert(exectution_query(db_files_name[0], create_table_sqlite) == True)

def test_integrity_create_table_string() -> None:
    assert(testing_create_table_sqlite == create_table_sqlite)

def test_create_query() -> None:
    for j in range(5):
        assert exectution_query(db_files_name[0], insert_query(Deal())) == True

def test_delete_by_id() -> None:
    for j in range(1, 4):
        assert exectution_query(db_files_name[0], delete_by_id_query(j)) == True

def test_resources_delete() -> None: 
    os.system(f'rm {db_files_name[0]}')

