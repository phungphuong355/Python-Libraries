#! /usr/bin/env python
import numpy as np
import pandas as pd

Student = dict(
    firstname=["Nguyen Van"]*len("ABCDEF"),
    lastname=[x for x in "ABCDEF"]
)

Data = np.random.randint(0, 10, (6, 3))

df1 = pd.DataFrame(Student)
df2 = pd.DataFrame(Data, columns=['Math', 'Literature', 'English'])

df1['Math'] = df2['Math']
df1['Literature'] = df2['Literature']
df1['English'] = df2['English']

df1['Total'] = df1['Math'] + df1['Literature'] + df1['English']
df1['Average'] = (df1['Math'] + df1['Literature'] + df1['English'])/3
print(df1)
print(df1[df1['Average'] > 5])
print(df1.sort_values(by=['Total', 'Math'], ascending=False).head(3))
