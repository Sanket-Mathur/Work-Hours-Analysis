import numpy as np
import matplotlib.pyplot as plt 
import sys

sys.path.append('../DataBase/')
from db import Management

def transform_date_format(date):
    '''
    Remove the year from date and return month-day

    Parameter
    ---------
    date : str
        It should be in format `yyyy-mm-dd`

    Return
    ------
    new_date : str
        Return in format `mm-dd`
    '''
    new_date = '-'.join(date.split('-')[1:])
    return new_date

def analyse():
    database = Management()
    data = database.returnData()[-7:]

    data = np.array(data).T
    data[0] = np.array(list(map(transform_date_format, data[0])))
    X = np.array(data[1:3]).astype('float64')

    plt.plot(data[0], X[0], X[1])
    plt.show()

if __name__ == '__main__':
    analyse()