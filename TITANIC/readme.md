# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)

This project performs a comprehensive Exploratory Data Analysis (EDA) on the famous **Titanic dataset** from the Kaggle competition: [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic).

The aim is to uncover insights about the survival patterns of passengers and visualize important trends in the data.

---

## 📁 Dataset

The dataset contains details of passengers such as:

- **PassengerId**: ID given to each traveler
- **Pclass**: Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)
- **Name**, **Sex**, **Age**
- **SibSp**, **Parch**: Family relations aboard
- **Ticket**, **Fare**, **Cabin**
- **Embarked**: Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)
- **Survived**: 0 = No, 1 = Yes (target variable)

You can download it from:
[https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)

---

## 📊 Key Tasks Performed

- **Loading & inspecting** data
- **Handling missing values**
- **Encoding categorical variables**
- **Univariate and bivariate analysis**
- **Feature engineering** (e.g. `FamilySize`)
- **Data visualization** using `Seaborn` and `Matplotlib`
- **Correlation analysis** and heatmap

---

## 🧪 Requirements

To run this project, install the following Python libraries:

```bash
pip install pandas numpy seaborn matplotlib
