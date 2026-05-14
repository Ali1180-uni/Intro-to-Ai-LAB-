# # Lab 13 - Class Tasks 

# import pandas as pd

# # Load CSV File
# data = pd.read_csv(r"D:\4th Sem\Intro AI\cars.csv")

# # Show first 5 rows
# print(data.head())

# # Show full info
# print(data.info())

# # Show shape
# print("Rows and Columns:", data.shape)

# from sklearn.datasets import load_iris
# import pandas as pd

# # Load dataset
# iris = load_iris()

# # Convert to DataFrame
# df = pd.DataFrame(iris.data, columns=iris.feature_names)

# # Add target column
# df['target'] = iris.target

# print(df.head())

# print("Target Names:", iris.target_names)

# Home Activity 


# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import LabelEncoder

# # Dataset
# data = {
#     "Province": ["Punjab", "Sindh", "KPK", "Balochistan"],
#     "Population": [120, 50, None, 12],
#     "Literacy": [64, 58, 55, None],
#     "Region": ["East", "South", "North", "West"]
# }

# df = pd.DataFrame(data)

# # Fill missing values with median
# df["Population"].fillna(df["Population"].median(), inplace=True)
# df["Literacy"].fillna(df["Literacy"].median(), inplace=True)

# print(df)

# # Label Encoding
# le = LabelEncoder()
# df["Region_Label"] = le.fit_transform(df["Region"])

# # One Hot Encoding
# onehot = pd.get_dummies(df["Region"])
# print(onehot)

# # Scatter Plot
# plt.scatter(df["Population"], df["Literacy"])

# for i in range(len(df)):
#     plt.text(df["Population"][i], df["Literacy"][i], df["Province"][i])

# plt.xlabel("Population")
# plt.ylabel("Literacy Rate")
# plt.title("Province Analysis")
# plt.show()


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Random Data
# np.random.seed(1)

# df = pd.DataFrame({
#     "ID": range(1,101),
#     "Math": np.random.randint(40,100,100),
#     "Science": np.random.randint(40,100,100),
#     "English": np.random.randint(40,100,100),
#     "Grade": np.random.choice(["A","B","C"],100)
# })

# # Missing Values
# df.loc[5,"Math"] = np.nan
# df["Math"].fillna(df["Math"].mean(), inplace=True)

# # Histogram
# plt.hist(df["Math"], bins=10, edgecolor="black")
# plt.title("Math Scores")
# plt.show()

# # Total Score
# df["Total"] = df["Math"] + df["Science"] + df["English"]

# # Boxplot
# plt.boxplot(df["Total"])
# plt.title("Total Scores Outliers")
# plt.show()

# print(df.head())

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import LabelEncoder

# data = {
#     "Name": ["Ahsan", "Hira", "Bilal", "Zara", "Salman", "Mahnoor"],
#     "Age": [25, 27, 35, 29, None, 40],
#     "Salary": [50000, None, 75000, 2000000, 60000, 90000],
#     "Department": ["IT", "Finance", "IT", "HR", "Finance", "IT"]
# }

# df = pd.DataFrame(data)

# # Fill Missing Values
# df["Age"].fillna(df["Age"].mean(), inplace=True)
# df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# # Encode Department
# le = LabelEncoder()
# df["Dept_Code"] = le.fit_transform(df["Department"])

# print(df)

# # Boxplot for Salary
# plt.boxplot(df["Salary"])
# plt.title("Salary Outliers")
# plt.show()