import pandas as pd

df = pd.read_csv("train.csv")

print(df[["Name", "Age", "Embarked"]][(df.Embarked == "C")])


# filtered = df[(df.Embarked == "C")]
# print(filtered[["Name", "Age", "Embarked"]])



