from datetime import datetime
import sys

sys.path.append('../DataBase/')
from db import Management

database = Management()


def within_time_bound(hours: int) -> bool:
    if hours < 0 or hours > 24:
        return False
    return True


def update(date, work_hr, waste_hr):
    '''
    Updates a single row corresponds to given date to it.

    Parameters
    ----------
    date : str
        Date in string with format yyyy-mm-dd.
    work_hr : str
        Hours spent productive in string
    waste_hr : str
        Hours spent doing un-productive work
    '''
    proceed = ''
    print(database.checkData(date))
    earlier_date, earlier_work, earlier_waste = database.checkData(date)[0]
    print("\nEntry already exists with this date: \n"
        + "Date: {}\nWork Hours: {}\nWaste Hours: {}".format(earlier_date, earlier_work, earlier_waste)
    )
    while(proceed not in ['y', 'n']):
        proceed = input('\nProceed to update(y/n): ').strip().lower()
        if proceed not in ['y', 'n']:
            print('Invalid Input!')
    if proceed == 'y':
        database.updateData([date, work_hr, waste_hr])


def insert():
    try:
        year, month, day = map(int, input('Date (yyyy-mm-dd): ').strip().split('-'))
        date = datetime(year, month, day)
        working = input('Work Hours: ')
        waste = input('Waste Hours: ')
        if not within_time_bound(int(working)) or not within_time_bound(int(waste)) or not within_time_bound(
                int(working)+int(waste)):
            print('Working & Waste Hours should be in the range of 0 to 24 and their sum should not exceed 24 hours.')
            raise
        date = date.strftime('%Y-%m-%d')
    except:
        print('ERROR: Input Values')
        sys.exit(1)
    if database.checkData(date):
        update(date, working, waste)
    else:
        database.insertData([date, working, waste])

if __name__ == '__main__':
    insert()
