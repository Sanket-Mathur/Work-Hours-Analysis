import matplotlib.pyplot as plt 
from db import Management

database = Management()
data = database.returnData()

print(data)