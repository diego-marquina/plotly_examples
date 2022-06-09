#%%
#import modules
import plotly.express as px

#%%
#simple plotly example
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()