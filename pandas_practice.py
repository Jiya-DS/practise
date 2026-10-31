import pandas as pd
import numpy as np
# marks = pd.Series(
#     [85, 92, 78, 95, 67],
#     index = ["Ram","Sita", "Hari", "Gita", "Shyam"])

# print(marks)
# print(marks["Sita"])
# print(marks.size)
# print(marks.dtype)

# marks = pd.Series(
#     [85, 92, 78, 95, 67],
#     index=["Ram", "Sita", "Hari", "Gita", "Shyam"]
# )
# print(marks.mean())
# print(marks.max())
# print(marks.idxmax())
# print(marks.min())
# print(marks[marks>80])
# result = marks+5
# print(result)
# result2 =marks[marks<(marks.mean())]
# print(result2)

#dataframe

# data ={
#     "name":["Ram","Sita","Hari","Gita","Shyam"],
#     "age": [20,21,19,20,22],
#     "marks":[85,92,78,95,67]
#     }
# df = pd.DataFrame(data)
# print(df)
# print(df.head(3))
# print(df.tail(2))
# print(df.shape)
# print(df.size)
# print(df.columns)
# print(df.dtypes)

# print(df["name"])
# print(df[["name","marks"]])
# print(df.iloc[2])
# print(df.iloc[0:4])
# print(df.loc[3,"marks"])
# print(df[df["marks"]>85])
# print(df[df["age"]>20])
# print(df[(df["age"]>=20) & (df["marks"]>80)])

# print("Average:",df["marks"].mean())
# highest_marks = df["marks"].idxmax()
# print("highest mark student:",df.loc[highest_marks,"name"])
# lowest_marks = df["marks"].idxmin()
# print("lowest marks student:",df.loc[lowest_marks,"name"])
# above_avg = df[df["marks"]> df["marks"].mean()]
# print("student scoring above average:", above_avg)
# print("total marks of all student :",df["marks"].sum())
# print("statistical summary:",df.describe())
# df["result"] = np.where(df["marks"]>=80 ,"Pass", "Fail")
# print(df)

df = pd.DataFrame(
    {
        "name": ["Ram", "Sita", "Hari", "Gita"],
        "marks": [85, 92, 78, 95]
    },
    index=[10, 20, 30, 40]
)
print(df.iloc[1])
print(df.iloc[3,1])

print(df.loc[30])
print(df.loc[10,"marks"])