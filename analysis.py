import pandas as pd 
df = pd.read_csv("Data.csv")
print("NRows:" len(df))
print("M_Price:", df["price"].mean())
#Print the largest sale
print('Max_Price:', df["Price"].max())