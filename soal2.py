import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

content = pd.read_csv('mtcars.csv', sep = ',')
content.head()
for col in content.columns:
    content.loc[content['mpg'] > 30, 'mpg_name'] = 'Hard'
    content.loc[(content['mpg'] >= 20) & (content['mpg'] <= 30), 'mpg_name'] = 'Medium'
    content.loc[content['mpg'] < 20, 'mpg_name'] = 'Low'

    print(content)

y_columns = ['mpg']
content.plot(x='Cars', y=y_columns, kind="bar")
content.plot(x='Cars', y=y_columns, kind="scatter")
plt.title('Data Majalah Trend Motor US')
plt.ylabel('MPG')
plt.show()
