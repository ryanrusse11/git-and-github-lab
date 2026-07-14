import pandas as pd 
df = pd.read_csv("Data.csv")
print("Number of rows:" len(df))
print("Mean price:", df["price"].mean())
#Print the largest sale
print('Largest Sale:', df["Price"].max())