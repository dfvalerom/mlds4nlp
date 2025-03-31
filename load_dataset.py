import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/dfvalerom/mlds4nlp/refs/heads/main/cb_multi_labeled_balanced.csv")
print(df.head().to_string())
