import pandas as pd
import os
filepath = os.path.dirname(__file__)
df = pd.read_excel(os.path.join(filepath, 'files/BOM file for Data processing.xlsx'), sheet_name='Source')
grouped = df.groupby('Item Name')
with pd.ExcelWriter('output.xlsx') as writer:
  for name, group in grouped:
    m = group.groupby('Level')
    for name2, group2 in m:
      group2.to_excel(writer, sheet_name=name + name2)
