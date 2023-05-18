#2.- Limpieza de datos

import pandas as pd

df = pd.read_csv('nba_game_stats.csv')


df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Team','Date','Home','Opponent','WINorLOSS','TeamPoints','OpponentPoints']])
print(df_LIMP)