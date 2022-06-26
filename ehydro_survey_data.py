# import numpy as np
import pandas as pd

columns1 = [0, 12, 21]

ehydro1 = pd.read_csv('eHydro_Survey_Data.csv', delimiter=',', usecols=columns1)

print('Номер, район, глобальный номер')

print(ehydro1.iloc[0:10])
