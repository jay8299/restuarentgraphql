import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/vijaykumar/Desktop/graphql_django/graphapp/db.sqlite3')
df2 = pd.read_csv('/Users/vijaykumar/Desktop/graphql_django/restaurant_addc9a1430.csv')
df = pd.read_csv('/Users/vijaykumar/Desktop/graphql_django/restaurantsa9126b3.csv')

df=df[['id', 'name', 'Cuisines', 'Cost',
       'Currency', 'booking', 'delivery',
       'rating', 'colour', 'text', 'Votes']]


df.columns = df.columns.str.lower()
print(df.columns)

df.to_sql('restuarentapp_restuarent', conn, if_exists='replace', index=False)

