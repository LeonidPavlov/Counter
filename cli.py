import counter
import  os
import datetime
import shutil

from counter.view.main_gui import App
from counter.sqlite_user.crud import sqlite_dir, exectution_query,\
                                create_table_sqlite, db_files_name
from counter.aux.error_handling import ACHTUNG

os.system(F'mkdir -p {sqlite_dir}')

# TESTS
start: datetime = datetime.datetime.now()
os.system('pytest tests')
after: datetime = datetime.datetime.now()
print(f'test time -> {after.second - start.second} seconds')

# EXECUTION

if exectution_query(db_files_name[1], create_table_sqlite):
    print('created database ...')

print('starting gui ...')
App().start()

try:
    shutil.copy(db_files_name[1], db_files_name[2])
    print('copied database file ...')
except Exception as err:
    ACHTUNG(err,__file__,'copy database')

print('stop ...')
