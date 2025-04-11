import pandas as pd
file_path = '/content/drive/MyDrive/athlete_events.csv'
df = pd.read_csv(file_path)

%matplotlib inline
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns

#z = zipfile.ZipFile("../data/athlete_events.zip")
#df = pd.read_csv(z.open("athlete_events.csv"))
df = df.dropna(subset=['Medal', "Age", "Height", "Weight"])
df.head()

df.groupby(['Sex'])['Medal'].value_counts()

#медали     #группировка страны-золотые медали   #сортировка            #вывести первое
df.query("Medal == 'Gold'").groupby(['Team'])['Medal'].count().sort_values(ascending=False).index[0]

pd.crosstab(df['Sex'], df['Sport'], margins=True)

print(df[(df['Sex'] == 'F') & (df['Sport'] == 'Ice Hockey')]['Age'].mean())
print(df[(df['Sex'] == 'F') & (df['Sport'] == 'Ice Hockey')]['Age'].std())

df[(df['Sex'] == 'F') & (df['Medal'] == 'Bronze')].groupby('Team').size().sort_values(ascending=False).index[0] 
#одновременный фильтр в датафрейм с выбором женщин и бронз медалей; далее подсчет количества медалей в каждой команде, сортировка в порядке убывания и вывод 1го элемента

medal_count = df.groupby(['Team', 'Medal']).size().reset_index(name='Count') #reset_index заменяет индекс датафрейма на обычный индекс, состоящий из целых чисел 1.
top_3_countries = medal_count.groupby('Team').sum()['Count'].sort_values(ascending=False)[:3] #топ стран по количеству медалей
filtered_df = medal_count[medal_count['Team'].isin(top_3_countries.index)] #топ стран по количеству медалей c распределением по номиналу
filtered_df

filtered_df.pivot(index='Team', columns='Medal', values='Count').plot(kind='bar')
plt.show()

silver_men_df = df[(df['Sex'] == 'M') & (df['Medal'] == 'Silver')]
# Строим график плотности распределения веса
sns.kdeplot(data=silver_men_df['Weight'], shade=True, label='Мужчины с серебряной медалью') #Функция kdeplot из библиотеки Seaborn используется для построения графика плотности распределения вероятностей. Она показывает, насколько часто встречаются значения в определенном диапазоне, сглаживая исходные данные с помощью ядра плотности.
# Добавляем метки и заголовок
plt.xlabel('Вес (кг)')
plt.ylabel('Плотность')
plt.title('Распределение веса мужчин, получивших серебряную медаль')
# Показываем график
plt.show()


sns.set(style="whitegrid") #установка стиля графика
ax = sns.boxplot(x='Medal', y='Age', data=df) #на Х - медаль, на у - Возраст
plt.ylim(0, None) #граница от 0 до автоматической отметки
plt.show()

dfUSA = df[df.Team == 'United States'] #новый датафрейм с фильтром из оригинального датафрейма по комнаде США
sns.pairplot(df[['Age', 'Weight', 'Height']]) #парный график по трем параметрам
plt.show() #прямая зависимость роста и веса (стремится к прямой линии)