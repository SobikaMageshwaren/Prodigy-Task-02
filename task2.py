import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic train dataset
train_df = pd.read_csv('train.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(train_df.head())

# Check for missing values
print("\nMissing values in the dataset:")
missing_values = train_df.isnull().sum()
print(missing_values)

# Fill missing values
train_df['Age'].fillna(train_df['Age'].median(), inplace=True)
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)

# Drop the Cabin column due to many missing values
train_df.drop(columns=['Cabin'], inplace=True)

# Display the first few rows after cleaning
print("\nFirst few rows after cleaning:")
print(train_df.head())

# Univariate Analysis

# Distribution of Age
plt.figure(figsize=(8, 6))
sns.histplot(train_df['Age'], bins=30, kde=True, color='blue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Distribution of Fare
plt.figure(figsize=(8, 6))
sns.histplot(train_df['Fare'], bins=30, kde=True, color='green')
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# Count of Passenger Classes
plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', data=train_df, palette='viridis')
plt.title('Passenger Class Distribution')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()

# Count of Gender
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', data=train_df, palette='viridis')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Bivariate Analysis

# Survival Rate by Passenger Class
plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=train_df, ci=None, palette='viridis')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

# Survival Rate by Gender
plt.figure(figsize=(8, 6))
sns.barplot(x='Sex', y='Survived', data=train_df, ci=None, palette='viridis')
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.show()

# Survival Rate by Age
plt.figure(figsize=(8, 6))
sns.histplot(data=train_df, x='Age', hue='Survived', multiple='stack', kde=True)
plt.title('Survival Rate by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Multivariate Analysis

# Survival Rate by Gender and Passenger Class
plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=train_df, ci=None, palette='viridis')
plt.title('Survival Rate by Gender and Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.legend(title='Gender')
plt.show()

# Survival Rate by Age and Passenger Class
plt.figure(figsize=(10, 8))
sns.violinplot(x='Pclass', y='Age', hue='Survived', data=train_df, split=True, palette='viridis')
plt.title('Survival Rate by Age and Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.legend(title='Survived')
plt.show()
