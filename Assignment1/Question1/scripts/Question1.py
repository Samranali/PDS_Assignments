import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Assignment1/Question1/data/data.csv')

df = pd.DataFrame(data)

print("Data Overview")
print(df.describe())

plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x='Frailty', y='Grip_strength', data=df)
plt.title('Grip Strength by Frailty')
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x='Age', y='Grip_strength', hue='Frailty', data=df, palette='coolwarm')
plt.title('Age vs Grip Strength with Frailty Indicator')
plt.show()

print("\nStatistics for Grip Strength by Frailty")
print(df.groupby('Frailty')['Grip_strength'].describe())

df.to_csv('Assignment1/Question1/processed_data/processed_frailty_data.csv', index=False)
