import pandas as pd

df1 = pd.read_csv('houses.csv')
df2 = pd.read_csv('apartments.csv')

combined_df = pd.concat([df1, df2])
combined_df = combined_df.reset_index(drop=True)
combined_df.to_csv('combined.csv', index=False)