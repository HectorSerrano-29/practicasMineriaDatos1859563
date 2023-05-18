#5.- Prueba de hipótesis.

import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv('nba_game_stats.csv')


df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Team','Date','Home','Opponent','WINorLOSS','TeamPoints','TeamPoints']])
print(df_LIMP)

fig = go.Figure()
fig.add_trace(go.Box(y=df_LIMP.AmountSpent.loc[df_LIMP.Puntos=='TeamPoints'],name="TeamP"))
fig.add_trace(go.Box(y=df_LIMP.AmountSpent.loc[df_LIMP.Puntos=='TeamPoints'],name="OpponentP"))
fig.update_layout(
    title={
        'text': "Cantidad gastada en minorista",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.show()