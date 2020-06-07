import sqlite3
import pandas as pd

conn = sqlite3.connect('../db.sqlite3')
df = pd.read_csv('../restaurantsa9126b3.csv')

df=df[['id', 'name', 'Cuisines', 'Cost',
       'Currency', 'booking', 'delivery',
       'rating', 'colour', 'text', 'Votes']]


df.columns = df.columns.str.lower()
print(df.columns)

df.to_sql('restuarentapp_restuarent', conn, if_exists='replace', index=False)

