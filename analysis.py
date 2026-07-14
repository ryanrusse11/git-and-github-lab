import pandas as pd 
df = pd.read_csv("Data.csv")
print("Number of transactions:" len(df))
print("Mean transaction price:", df["price"].mean())
#Print the largest sale
print('Largest Transaction:', df["Price"].max())