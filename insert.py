from db import Management
from datetime import datetime
import sys

def insert():
    database = Management()
    try:
        year, month, day = map(int, input('Date (yyyy-mm-dd): ').strip().split('-'))
        date = datetime(year, month, day)
        working = input('Work Hours: ')
        waste = input('Waste Hours: ')
    except:
        print('ERROR: Input Values')
        sys.exit(1)
    database.insertData([str(date.strftime('%Y-%m-%d')), working, waste])

if __name__ == '__main__':
    insert()
