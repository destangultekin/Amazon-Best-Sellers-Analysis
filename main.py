import pandas as pd

df = pd.read_csv("bestsellers.csv")

print(df.columns)
print(df.head())
print(df.info())
df.drop_duplicates(inplace=True)
print(df["Author"].value_counts().head())
print(df.groupby("Genre")["Price"].mean())
print(df[df["User Rating"] == 4.9])
print(df["Price"].max())
print(df[df["Price"] == df["Price"].max()])

df.to_csv("cleaned_bestsellers.csv", index=False)