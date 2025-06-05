import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")
sns.set(style='whitegrid')

df = pd.read_csv('titanic.csv')

print(df.info())
print(df.describe())
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(['Cabin', 'Ticket', 'Name'], axis=1, inplace=True)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

plt.figure(figsize=(15, 8))
plt.subplot(2, 2, 1)
sns.countplot(x='Survived', data=df)
plt.subplot(2, 2, 2)
sns.countplot(x='Sex', data=df)
plt.subplot(2, 2, 3)
plt.hist(df['Age'], bins=30, edgecolor='black')
plt.subplot(2, 2, 4)
sns.histplot(df['Fare'], kde=True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 8))
plt.subplot(2, 2, 1)
sns.barplot(x='Sex', y='Survived', data=df)
plt.subplot(2, 2, 2)
sns.barplot(x='Pclass', y='Survived', data=df)
plt.subplot(2, 2, 3)
sns.violinplot(x='Survived', y='Age', data=df)
plt.subplot(2, 2, 4)
sns.boxplot(x='Survived', y='Fare', data=df)
plt.tight_layout()
plt.show()

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

plt.figure(figsize=(6, 4))
sns.barplot(x='FamilySize', y='Survived', data=df)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

print()
print("Key Observations:")
print("1. Females had significantly higher survival rates.")
print("2. Passengers in 1st class were more likely to survive.")
print("3. Children and younger individuals had better outcomes.")
print("4. Fare and family size seem to influence survival.")
