#6.- Regresion Lineal

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('nba_game_stats.csv')


df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Team','Date','Home','Opponent','WINorLOSS','TeamPoints','OpponentPoints']])
print(df_LIMP)

X = df_LIMP['TeamPoints'].values.reshape(-1,1)
Y = df_LIMP['OpponentPoints']

linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.xlabel('PuntuacionT')
plt.ylabel('PuntuacionO')
plt.title('Puntuacion')
plt.show()
plt.close()

df_lr = pd.DataFrame({'OpponentP': df_LIMP['OpponentPoints'], 'TeamP': df_LIMP['TeamPoints']})
df_lr_plot_scatter = df_lr.plot.scatter(x = 'TeamP', y = 'OpponentP')
fig = df_lr_plot_scatter.get_figure()
plt.xlabel('PuntuacionT')
plt.ylabel('PuntuacionO')
plt.title('Puntuacion')
plt.show()
plt.close()