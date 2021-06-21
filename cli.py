import counter
import  os
import datetime

start: datetime = datetime.datetime.now()
os.system('pytest tests')
after: datetime = datetime.datetime.now()
print(f'test time -> {after.second - start.second} seconds')
print('start ...')                    
os.system('python3 counter')
print('stop ...')
