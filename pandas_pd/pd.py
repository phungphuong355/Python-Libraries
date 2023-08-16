#! /usr/bin/env python
import numpy as np
import pandas as pd

# DataFrame 1
data = dict(
    car=['BMW', 'Ford', 'Volvo'],
    passings=[3, 7, 2]
)
df = pd.DataFrame(data)
print(df)

# Series 1
a = np.array([1, 7, 2])
df = pd.Series(a)
print(df)
print(df[0])

# Series 2
a = np.array([1, 7, 2])
df = pd.Series(a, index=[x for x in 'abc'])
print(df)

# Series 3
a = dict(
    firstname='Nguyen Van',
    lastname='A',
    ns=2000
)
df = pd.Series(a)
print(df)

# DataFrame 2
dataset = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}
df = pd.DataFrame(dataset)
print(df)
print(df.loc[0])
print(df.iloc[:, 0])
print(df.iloc[:, [0, 1]])

# DataFrame 3
dataset = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}
df = pd.DataFrame(dataset, index=['day1', 'day2', 'day3'])
print(df.head())

# DataFrame 4
data = np.random.randint(0, 10, (5, 4))
row_index = [2022, 2021, 2020, 2019, 2018]
df = pd.DataFrame(data, columns=[x for x in 'abcd'], index=row_index)
print(df.head())
print(df.index.values)
print(df.columns.values)
print(df.values)
print(df.to_numpy())
print(df.describe().T)

# DataFrame 5
data = np.random.randint(0, 10, (5, 4))
row_index = [2022, 2021, 2020, 2019, 2018]
df = pd.DataFrame(data, columns=[x for x in 'abcd'], index=row_index)
df.sort_values(by=['a', 'b'], ascending=True)
print(df)
print(df[0:3])
print(df.loc[:, ['a', 'c']])
print(df.iloc[:, :-1])
print(df.iat[3, 1])
print(df[df['b'] > 2])
print(df[df > 2])

# DataFrame 6
df2 = df.copy()
df2['e'] = [x for x in range(1, 6)]
print(df2[df2['e'].isin([1, 3])])
# help(df.isin)

# Series 4
s1 = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('2022', periods=5))
print(s1)
df['e'] = s1
print(df)

# DataFrame 7
data = np.random.randint(0, 10, (5, 4))
row_index = [2022, 2021, 2020, 2019, 2018]
df = pd.DataFrame(data, columns=[x for x in 'abcd'], index=row_index)
df.at[2022, 'a'] = -1
print(df.iat[0, 2])
print(df)
