import numpy as np
import matplotlib.pyplot as plt 
import sys

sys.path.append('../DataBase/')
from db import Management

def analyse():
    database = Management()
    data = database.returnData()[-7:]

    data = np.array(data).T
    X = np.array(data[1:3]).astype('float64')

    plt.plot(data[0], X[0], X[1])
    plt.show()

if __name__ == '__main__':
    analyse()