import pandas as pd
df = pd.read_csv("m1.csv")
df.head()
df.dtypes
df = df.dropna()
df.dtypes
df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]
df.head()
df.columns
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.head()
df.reset_index(drop=True,inplace=True)
df.head()
df.reset_index(drop=True,inplace=True)
df.to_csv("data shot.csv")
df.dtypes