import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Assignment1/Question2/data/data.csv')

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
sns.histplot(df['math score'], bins=10, kde=True, color='blue')
plt.title('Distribution of Math Scores')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.savefig('Assignment1/Question2/visualizations/math_score_distribution.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='gender', y='writing score', data=df)
plt.title('Writing Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Writing Score')
plt.savefig('Assignment1/Question2/visualizations/writing_scores_by_gender.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='math score', y='reading score', hue='gender', data=df)
plt.title('Scatter Plot of Math vs. Reading Scores')
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.savefig('Assignment1/Question2/visualizations/scatter_math_reading.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='parental level of education', y='math score', data=df, errorbar=None)
plt.title('Average Math Scores by Parental Level of Education')
plt.xlabel('Parental Level of Education')
plt.ylabel('Average Math Score')
plt.xticks(rotation=45)
plt.savefig('Assignment1/Question2/visualizations/avg_math_by_parental_education.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='race/ethnicity', data=df)
plt.title('Count of Students by Race/Ethnicity')
plt.xlabel('Race/Ethnicity')
plt.ylabel('Count')
plt.savefig('Assignment1/Question2/visualizations/count_by_race.png')
plt.show()
