import sys

sys.path.append('DataBase/')
from db import Management

def setup():
    print('Proceeding with the setup will setup a database to store the records')
    e = input('Proceed? (y/n): ').lower()
    if e == 'y':
        database = Management()
        database.createTable()
        print('Created')
    else:
        print('Aborted')

if __name__ == '__main__':
    setup()
