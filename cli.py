import counter
import  os
import datetime
import shutil

from counter.view import main
from counter.sqlite_user.crud import sqlite_dir, exectution_query,\
                                create_table_sqlite, db_files_name

os.system(F'mkdir -p {sqlite_dir}')

# TESTS
start: datetime = datetime.datetime.now()
os.system('pytest tests')
after: datetime = datetime.datetime.now()
print(f'test time -> {after.second - start.second} seconds')

# EXECUTION
print('start ...')

exectution_query(db_files_name[1], create_table_sqlite)

main.App()

try:
    shutil.copy(db_files_name[1], db_files_name[2])
except Exception as err:
    print(F'PIZDEC-> {__file__} in copy database procedure')

print('stop ...')
