#%%
# import modules
import pandas as pd
from plotly.offline import init_notebook_mode
from plotly.graph_objs import *
import plotly.graph_objects as go

init_notebook_mode(connected=True) 
pd.options.plotting.backend = "plotly"


#%%
# import balance data
nl_balance = pd.read_csv('NL_balance_plotly.csv', index_col=0, parse_dates=True)

#%%
# plot simple timeseries (demand)
nl_balance.loc['2018-03':'TotalLoadValue'].plot()

#%%
#more complicated plot (balance)

df_plot = nl_balance.loc['2015':,:].resample('d').mean()
df_plot = df_plot[['TotalLoadValue', 'net_imports']+[c for c in df_plot if c not in ['TotalLoadValue', 'net_imports']]]
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_plot.index, y=df_plot.TotalLoadValue, fill='none',
                    name='Load',
                    ))
for col in df_plot.iloc[:,1:].columns:
    fig.add_trace(go.Scatter(x=df_plot.index, y=df_plot[col], fill='tonexty',
                        mode='none', # override default markers+lines
                        stackgroup='one',
                        name=col,
                        ))
fig.show()
# %%
