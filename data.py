import pandas as pd
import plotly.express as px
#data=[8,9,56,23,3]
#df=pd.DataFrame(data)
df=pd.read_csv('data.csv')
fig=px.bar(df,x='Country',y='InternetUsers')
#print (df)
fig.show()
