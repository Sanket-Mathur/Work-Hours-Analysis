import sys

sys.path.append('DataBase/')
from db import Management

def setup():
    database = Management()
    database.createTable()
    database.printTable()

    print('Created')

if __name__ == '__main__':
    setup()
