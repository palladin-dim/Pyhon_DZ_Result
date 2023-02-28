import pandas as pd
import numpy as np
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# преобразуем столбец в числовые метки
label = pd.factorize(data['whoAmI'])[0]

# создадим матрицу нулей и заполним ее one-hot кодами
one_hot = np.zeros((len(label), len(np.unique(label))))
one_hot[np.arange(len(label)), label] = 1

# создадим новый DataFrame из one-hot матрицы и установим правильные названия столбцов
one_hot_df = pd.DataFrame(one_hot, columns=np.unique(data['whoAmI']))

# объединим исходный DataFrame с one-hot DataFrame
data = pd.concat([data, one_hot_df], axis=1)

# удалим исходный столбец "whoAmI"
data = data.drop('whoAmI', axis=1)

print(data.head())