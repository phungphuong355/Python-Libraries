#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('./Datasets/exams.csv')
df.info()

# Lọc dữ liệu rác nếu có (1 người thi sẽ có các thông tin sau: giới tính, nhóm, cấp độ và 3 cột điểm
print(df.isnull().sum())

# Tính điểm trung bình của 3 môn: toán, đọc và viết (cột 6, 7, 8)
average = round((df.iloc[:, 5] + df.iloc[:, 6] + df.iloc[:, 7])/3, 2)
df['average'] = average

# Tính tỉ lệ nam nữ trong tập dữ liệu và hiển thị biểu đồ dạng pie (cột 1)
male_rate = len(df[df['gender'] == 'male']['gender'])/len(df['gender'])
female_rate = 1 - male_rate
plt.pie(np.array([male_rate, female_rate]), labels=['male', 'female'])
plt.title("Tỉ lệ nam nữ")
plt.legend()
plt.show()

# Tính số lượng người thi theo từng nhóm (cột 2) và hiển thị biểu đồ dạng thanh đứng
sns.countplot(x=df['race/ethnicity'].sort_values())
for i, v in enumerate(df['race/ethnicity'].value_counts().sort_index()):
    plt.text(x=i, y=v + 5, s=v, ha='center')
plt.show()

# Tính số lượng người thi theo từng cấp độ (cột 3) và hiển thị biểu đồ dạng thanh đứng
sns.countplot(x=df['parental level of education'].sort_values())
for i, v in enumerate(df['parental level of education'].value_counts().sort_index()):
    plt.text(x=i, y=v + 5, s=v, ha='center')
plt.show()

# Hiển thị các biểu đồ phân bố cho 3 loại điểm toán, đọc và viết trên cùng 1 biểu đồ.
plt.subplot(3, 1, 1)
plt.hist(df['math score'], color='r')
plt.title("Math Score")

plt.subplot(3, 1, 2)
plt.hist(df['reading score'], color='b')
plt.title("Reading Score")

plt.subplot(3, 1, 3)
plt.hist(df['writing score'], color='y')
plt.title("Writing Score")
plt.show()

# Xác định 10 người thi có điểm tổng cao nhất.
df['Total'] = df['math score'] + df['reading score'] + df['writing score']
print(df.sort_values(by=['Total'], ascending=False).head(10))
