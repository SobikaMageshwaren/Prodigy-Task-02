⛴️ Data Cleaning & Exploratory Data Analysis (EDA)
This project demonstrates data cleaning and exploratory data analysis (EDA) on the famous Titanic dataset from Kaggle. The goal of this project is to explore the relationships between variables, identify patterns, and gain insights into the survival factors during the Titanic disaster.

📂 Dataset
The dataset used for this project is the Titanic train dataset from Kaggle. It includes various features such as age, gender, passenger class, fare, and more.

🔧 Prerequisites
Ensure you have the following Python libraries installed to run the project:

Pandas: Data manipulation and analysis
Matplotlib: Data visualization
Seaborn: Statistical data visualization
You can install the necessary libraries using pip:

pip install pandas matplotlib seaborn

🧹 Data Cleaning
Data cleaning is a crucial step in preparing the dataset for analysis. Here’s what we did:
Filled missing values in the Age and Embarked columns with the median and mode, respectively.
Dropped the Cabin column due to a high percentage of missing values.
Checked for any remaining missing data after the cleaning process.

📊 Exploratory Data Analysis (EDA)
1. Univariate Analysis
Age Distribution: Visualized the distribution of passengers' ages with a histogram and KDE plot.
Fare Distribution: Analyzed the distribution of ticket fares.
Passenger Class Distribution: Count plot showing the distribution of passengers across different classes.
Gender Distribution: Visualized the gender breakdown in the dataset.

2. Bivariate Analysis
Survival Rate by Passenger Class: Bar plot showing the survival rate for each class.
Survival Rate by Gender: Bar plot highlighting survival rates between males and females.
Survival Rate by Age: Stacked histogram showing survival rates across different age groups.

4. Multivariate Analysis
Survival Rate by Gender and Passenger Class: Bar plot that breaks down survival rates by gender within each passenger class.
Survival Rate by Age and Passenger Class: Violin plot displaying the distribution of age across different classes, split by survival status.

📈 Visualizations
We utilized Matplotlib and Seaborn to create insightful visualizations. These visualizations help in identifying patterns and trends in the data:

Bar Plots: For categorical variable analysis.
Histograms: For continuous variable distribution.
Violin Plots: To visualize the distribution of data across different categories.

🚀 Usage
To run this project:

Ensure the Titanic dataset (train.csv) is available in your working directory.
Run the Python script, and it will generate the visualizations in separate windows.

python titanic_eda.py

🛠 Tech Stack
Python
Pandas
Matplotlib
Seaborn

💡 Insights
Through this project, we gained key insights into the factors that influenced survival rates on the Titanic, such as gender, passenger class, and age. These analyses highlight the importance of exploratory data analysis in understanding the nuances of a dataset.

🎯 Conclusion
This project showcases the power of data cleaning and EDA in uncovering meaningful patterns in historical data. Whether you're a data enthusiast or a Titanic history buff, this analysis sheds light on the tragedy from a data-driven perspective.
