# -*- coding: utf-8 -*-
"""ML_Lec02_HW.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LSuMheGRSN2eOhvzQSc5bG9D9a9rLafd

# Задачи к Лекции 2

__Исходные данные__

Дан файл **"mlbootcamp5_train.csv"**. В нем содержатся данные об опросе 70000 пациентов с целью определения наличия заболеваний сердечно-сосудистой системы (ССЗ). Данные в файле промаркированы и если у человека имееются ССЗ, то значение **cardio** будет равно 1, в противном случае - 0. Описание и значения полей представлены во второй лекции.

__Загрузка файла__
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
file_path = '/content/drive/MyDrive/mlbootcamp5_train.csv'
df = pd.read_csv(file_path)

# Commented out IPython magic to ensure Python compatibility.

# %matplotlib inline
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/content/drive/MyDrive/mlbootcamp5_train.csv',
                 sep=";",
                 index_col="id")
df.head()

df[["age", "height", "weight", "ap_hi", "ap_lo"]].hist()
plt.tight_layout() #—ф-я библиотеки Matplotlib, которая автоматически настраивает параметры графиков, чтобы они точно вписывались в область рисунка
plt.show()

for i, col in enumerate(["age", "height", "weight", "ap_hi", "ap_lo"]):
    plt.subplot(231 + i) #выводит несколько графиков в 2 строки, 3 столбца, начиная с 1
    plt.title(col)
    sns.boxplot(df[col])
plt.tight_layout()
plt.show()

# смотрим, что может повлиять на ошибочный результат, смотрим выбросы

data = df[(df["ap_hi"] >= 50) & (df["ap_hi"] <= 200) & (df["ap_lo"] >= 50) & (df["ap_lo"] <= 200) & (df["height"] >= 140) & (df["height"] <= 200) & (df["weight"] >= 40) & (df["weight"] <= 130)]
data[data["cardio"] == 1][["age", "height", "weight", "ap_hi", "ap_lo"]].hist(bins=20)
plt.tight_layout()
plt.show()
#удаление атулаеров

"""## Задачи

**1. Построить наивный байесовский классификатор для количественных полей age, height, weight, ap_hi, ap_lo. Исправить данные, если это необходимо. Привести матрицу неточностей и сравнить со значением полученным в ходе лекции. Попытаться объяснить разницу.**
"""

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import itertools
class_names = ["Здоров", "Болен"]
def plot_confusion_matrix(cm, classes, normalize=False, title='Матрица неточностей', cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    fmt = '.4f' if normalize else 'd'
    thresh = cm.min() + (cm.max() - cm.min()) * 2 / 3.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    plt.ylabel('Истина')
    plt.xlabel('Предсказание')
    plt.tight_layout()

train = data[["age", "height", "weight", "ap_hi", "ap_lo"]]
target = data["cardio"]

gnb = GaussianNB()
model = gnb.fit(train, target)
predict = model.predict(train)# Прогнозирование значений для тестовых данных
acc = accuracy_score(target, predict)
cnf = confusion_matrix(target, predict)

print("точность = ", acc)
plot_confusion_matrix(cnf, class_names, normalize = True)
plt.show()

"""Модель лучше справляется с классификацией здоровых людей (высокая полнота), но хуже с классификацией больных.
Высокий уровень ложных отрицательных результатов (FN) может быть критичным в медицинских приложениях, так как это означает, что модель пропускает больных людей, классифицируя их как здоровых.
Высокий уровень ложных положительных результатов (FP) также может быть проблемой, так как это означает, что модель ошибочно классифицирует здоровых людей как больных.

**Комментарии:** Ваши комментарии здесь.

**2. Написать свой наивный байесовский классификатор для категориальных полей cholesterol, gluc. Привести матрицу неточностей и сравнить со значениями из задачи 1 (нельзя использовать готовое решение из sklearn) (не обязательно)**
"""

train = data[["cholesterol", "gluc"]]
target = data["cardio"]

gnb = GaussianNB()
model = gnb.fit(train, target)
predict = model.predict(train)# Прогнозирование значений для тестовых данных
acc = accuracy_score(target, predict)
cnf = confusion_matrix(target, predict)

print("точность = ", acc)
plot_confusion_matrix(cnf, class_names, normalize = True)
plt.show()

"""Аналогично предыдущему.

**Комментарии:** Ваши комментарии здесь.

**3. Построить наивный байесовский классификатор для бинарных полей gender, smoke, alco, active. Привести матрицу неточностей и сравнить с предыдущими значениями.**
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Выбор бинарных полей
train = data[["gender", "smoke", "alco", "active"]]
target = data["cardio"] # Предположим, что 'cardio' - это целевая переменная

gnb = GaussianNB()
model = gnb.fit(train, target)
predict = model.predict(train)# Прогнозирование значений для тестовых данных
acc = accuracy_score(target, predict)
cnf = confusion_matrix(target, predict)

print("точность = ", acc)
plot_confusion_matrix(cnf, class_names, normalize = True)
plt.show()

"""**Комментарии:** Ваши комментарии здесь.

Много определяет больных за здоровых (FP) и здоровых за больных (FN).

**4. К этому моменту у вас есть три независимых классификатора: по количественным полям, категориальным и бинарным. Придумать, как их объединить в один единый классификатор, который учитывает все эти поля. Привести матрицу неточностей для него и сравнить с предыдущими значениями. Попытаться объяснить разницу.**
"""

# A lot of code here

"""**Комментарии:** Ваши комментарии здесь.

**5. (Не обязательно) Теперь мы умеем делать классификацию в рамках наивного предположения об независимости всех признаков. Сейчас же нужно попробовать учесть взаимосвязь между признаками через условные вероятности. Построить классификатор с учетом такой связи. Сравнить результат с ранее полученными значениями.**
"""

# A lot of code here

"""**Комментарии:** Ваши комментарии здесь."""

