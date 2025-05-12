import math
import random
import string
import time
import datetime
import pandas as pd
import numpy as np

print(math.sqrt(16))  

print ("random number between 1 and 10 is : ", random.randint(1, 10))
print ("random number between 1 and 100 is : ", random.randint(1, 100))
today = datetime.date.today()
print("Today's date is:", today)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)