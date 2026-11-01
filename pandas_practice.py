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

# df = pd.DataFrame(
#     {
#         "name": ["Ram", "Sita", "Hari", "Gita"],
#         "marks": [85, 92, 78, 95]
#     },
#     index=[10, 20, 30, 40]
# )
# print(df.iloc[1])
# print(df.iloc[3,1])

# print(df.loc[30])
# print(df.loc[10,"marks"])



# data = {
#     "Name": ["Ram", "Sita", "Hari", "Gita", "Rita"],
#     "Age": [20, np.nan, 22, 21, np.nan],
#     "Marks": [85, 90, np.nan, 75, 95]
# }

# df = pd.DataFrame(data)
# # print(df)
# print(df.isnull())
# print(df.isnull().sum())
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["Marks"]= df["Marks"].fillna(0)
# print(df)

# data = {
#     "Name": ["Ram", "Sita", "Hari", "Ram", "Gita", "Sita"],
#     "Age": [20, 21, np.nan, 20, 22, 21],
#     "Marks": [85, 90, 75, 85, np.nan, 90]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.isnull().sum())
# print(df.duplicated().sum())
# df = df.drop_duplicates()
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
# df= df.reset_index(drop=True)
# print(df)

# data = {
#     "Name": ["Ram", "Sita", "Hari", "Gita", "Rita"],
#     "Marks": [85, 95, 70, 90, 80],
#     "Age": [20, 22, 21, 19, 23]
# }

# df = pd.DataFrame(data)
# print(df.sort_values(by="Marks"))
# sorted_marks = df.sort_values(by="Marks", ascending = False)
# print(df.sort_values(by="Age"))
# print(df.sort_values(
#     by=["Marks","Age"],ascending = [False,True]))
# df = df.sort_values(by="Marks", ascending=False)
# df = df.reset_index(drop= True)
# print(df)



# data = {
#     "Name": ["Ram", "Sita", "Hari", "Gita", "Rita", "Aman", "Nisha"],
#     "Department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance"],
#     "Salary": [50000, 45000, 60000, 55000, 60000, 48000, 55000],
#     "Experience": [3, 5, 4, 6, 2, 3, 4]
# }

# df = pd.DataFrame(data)
# # Sort employees by salary from highest to lowest.
# print(df.sort_values(by = "Salary", ascending=False))
# print("..............................")
# print(df.sort_values(by=["Salary","Experience"],ascending=False))
# print("..............................")
# result = df[df["Department"]== "IT"]
# print(result.sort_values(by="Salary", ascending= False))
# print("..............................")
# top_employees = df[df["Salary"]>=50000]
# top_employees_sorted = top_employees.sort_values(by= ["Salary","Experience"], ascending=False).reset_index(drop=True)
# print("..............................")
# print(top_employees_sorted.head(3))

# import pandas as pd

# data = {
#     "Name": ["Ram", "Sita", "Hari", "Gita", "Rita","Aman", "Nisha", "Kiran", "Puja", "Rohan"],
#     "Department": ["CS", "IT", "CS", "IT", "CS", "IT", "CS", "IT", "CS", "IT"],
#     "Marks": [85, 92, 78, 92, 88, 75, 95, 88, 95, 80],
#     "Attendance": [90, 85, 95, 92, 88, 80, 98, 91, 94, 89]
# }

# df = pd.DataFrame(data)

# CS_dept= df[df["Department"]=="CS"]
# marks_greater_80 = CS_dept[(CS_dept["Marks"] > 80) & (CS_dept["Attendance"]>= 90)]
# print(marks_greater_80)
# print("___________________________________________")
# sorted_data = df.sort_values(by=["Marks","Attendance"], ascending=[False,False])
# print(sorted_data)
# print("___________________________________________")
# top_performer = df[df["Department"]=="IT"]
# top_3_performer = top_performer.sort_values(by=["Marks","Attendance"],ascending=[False,False])
# print(top_3_performer.head(3))
# print("___________________________________________")
# extracted_students = df[(df["Marks"]>=85) & (df["Attendance"]>=90) ]
# selected_students = extracted_students.sort_values(by=["Marks","Attendance"],ascending=False).reset_index(drop=True)
# print(selected_students)
# print(selected_students.head(2))

# data = {
#     "Name": ["Ram", "Sita", "Hari", "Gita", "Rita"],
#     "Math": [80, 90, 65, 95, 70],
#     "Science": [85, 95, 70, 90, 75],
#     "English": [75, 85, 60, 95, 80]
# }

# df = pd.DataFrame(data)
# df["total"]= df["Math"]+df["Science"]+df["English"]
# df["Average"]= df["total"]/3
# df["Result"] = np.where(df["Average"]>=75, "Pass", "Fail")
# print(df)
# print("__________________________________________________")
# df["Math"]=df["Math"]+5
# df["total"]=df["Math"]+df["Science"]+df["English"]
# df["Average"]= df["total"]/3
# df["Result"] = np.where(df["Average"]>=75, "Pass", "Fail")
# print(df)

# data = {
#     "Name": ["Ram", "Sita", "Hari", "Gita", "Rita", "Aman"],
#     "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
#     "Salary": [30000, 45000, 55000, 40000, 60000, 35000],
#     "Experience": [1, 4, 6, 3, 7, 2]
# }

# df = pd.DataFrame(data)
# df["Bonus"]=df["Salary"]*0.1
# df["New_Salary"]= df["Salary"]+df["Bonus"]
# df["Experience_Level"]=np.where(df["Experience"]>=5,"Senior",np.where(df["Experience"]>=2,"Intermediate","Fresher"))

# df["Salary"]=np.where(df["Department"]=="IT",df["Salary"] + (df["Salary"] * 0.05),df["Salary"])

# print(df)
# print("_____________________________________________")

# df["Bonus"]=df["Salary"]*0.1
# df["New_Salary"]= df["Salary"]+df["Bonus"]
# sorted_salary= df.sort_values(by="New_Salary", ascending=False)
# print(sorted_salary)
# print(df[df["New_Salary"]>50000])


# data = {
#     "Name": ["Asha", "Ram", "Sita", "Hari", "Gita", "Rita", "Aman"],
#     "Math": [85, 45, 92, 65, 78, 35, 88],
#     "Science": [90, 55, 88, 70, 82, 40, 95],
#     "English": [80, 60, 95, 75, 72, 50, 85],
#     "Attendance": [95, 75, 98, 85, 90, 60, 96]
# }
# df= pd.DataFrame(data)
# df["Total"]=df["Math"]+df["Science"]+df["English"]
# df["Average"]=df["Total"]/3
# df["Result"]= np.where(df["Average"]>=50,"Pass","Fail")
# df["Grade"]=np.where(df["Average"]>=90,"A",
#                     np.where(df["Average"]>=80,"B",
#                                np.where(df["Average"]>=60,"C","D")))

# df["English"] = np.where(df["Attendance"]>=90, df["English"]+5,df["English"])
# print(df)
# print("_______________________________")
# df["Total"]=df["Math"]+df["Science"]+df["English"]
# df["Average"]=df["Total"]/3
# df["Result"]= np.where(df["Average"]>=50,"Pass","Fail")
# df["Grade"]=np.where(df["Average"]>=90,"A",
#                     np.where(df["Average"]>=80,"B",
#                                np.where(df["Average"]>=60,"C","D")))
# sorted_data = df.sort_values(by="Average", ascending=False)
# students = df[(df["Result"]=="Pass" )& (df["Attendance"]>=90)]
# print(sorted_data)
# print(students)

data = {
    "Name": ["Asha", "Ram", "Sita", "Hari", "Gita", "Aman"],
    "Marks": [92, 45, 78, 35, 85, 60]
}

df = pd.DataFrame(data)
df["Bonus_Marks"]=df["Marks"].apply(lambda x : x+5)
df["Result"]= df["Marks"].apply(lambda x : "Pass" if x >=50 else "Fail")
df["Grade"]= df["Marks"].apply(lambda x : "A" if x >=90  else "B" if x >=75 else "C" if x>=50 else "D")
print(df)