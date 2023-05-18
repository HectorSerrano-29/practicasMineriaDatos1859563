#3.- Analisis de Datos

import pandas as pd

df = pd.read_csv('nba_game_stats.csv')


df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Team','Date','Home','Opponent','WINorLOSS','TeamPoints','OpponentPoints']])
print(df_LIMP)

mean_df = df_LIMP['OpponentPoints'].mean()
print(mean_df)
#Se manda el promedio del OpponentPoints

mean_df = df_LIMP['TeamPoints'].mean()
print(mean_df)
#Se manda el promedio del TeamPoints

media = df["OpponentPoints"].mean()
mediana = df["OpponentPoints"].median()
moda = df["OpponentPoints"].mode()
#Se imprime la Media, Moda y Mediana de OpponentPoints

print("""
    Media OpponentPoints: %d
    Mediana OpponentPoints: %d
    Moda OpponentPoints: %d
""" % (media,mediana,moda))

media = df["TeamPoints"].mean()
mediana = df["TeamPoints"].median()
moda = df["TeamPoints"].mode()
#Se imprime la Media, Moda y Mediana de TeamPoints

print("""
    Media TeamPoints: %d
    Mediana TeamPoints: %d
    Moda TeamPoints: %d
""" % (media,mediana,moda))