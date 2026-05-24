import pandas as pd

# Import datasets as df
df = pd.read_csv("../data/transport_node_train_202308.csv")

# print shape and first 5 rows
print(df.shape)
print(df.head())