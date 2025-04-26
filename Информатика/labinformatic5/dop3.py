import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('dop2.csv', sep=';')

df_long_formatted = df.melt(id_vars=['<DATE>'], value_vars=['<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>'],
                    var_name='Type', value_name='Numbers')
print(df_long_formatted)
plt.figure(figsize=(12, 6))
sns.boxplot(x='<DATE>', y='Numbers', hue='Type', data=df_long_formatted)
plt.xlabel("")
plt.ylabel("")
plt.grid(axis="y", linestyle="--", alpha=0.7)
# plt.show()

