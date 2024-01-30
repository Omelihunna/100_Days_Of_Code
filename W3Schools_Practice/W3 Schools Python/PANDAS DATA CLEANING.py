import pandas as pd

df = pd.read_csv('/Users/User/Downloads/dirtydata.csv')
new_df = df.dropna()
df["Calories"].fillna(130, inplace= True)
#mean
a = df["Calories"].mean()
#median
b = df["Calories"].median()
#mode
c = df["Calories"].mode()
#Data Formatting
df["Date"] = pd.to_datetime(df["Date"])
#Row Removal
d = df.dropna(subset=["Date"])
#Data Correction(Value Replacement)
e = df.loc[7, 'Duration'] = 45
#Data Correction(Conditional Replacement)
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 120
#empty cell removal(affects the orignal data)
#f = df.dropna(inplace=
#Duplicate Checker
g = df.duplicated()
#Dupliacate Removal
h = df.drop_duplicates()
#Normal Plot
df.plot(kind='scatter', x='Duration', y='Calories')
print(new_df)
print(df.to_string())
