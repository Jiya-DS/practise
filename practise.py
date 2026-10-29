import numpy as np
# # marks= np.array([
# #     [80, 75, 90],
# #     [65, 70, 85],
# #     [95, 88, 92]
# # ])
# # # Prints the total marks of each student.
# # for row in marks:
# #     total=0
# #     avg=0
# #     for num in row:
# #         total = total+num
# #         avg=total/len(row)
# #     print("Total:",total)
# #     print("Average:",avg)

# # highest = marks[0][0]

# # for row in marks:
# #     for num in row:
# #         if num>highest :
# #             highest=num
# # print("highest individual marks:",highest)
        
# # count=0
# # for row in marks:
# #     for num in row:
# #         if num>80:
# #             count= count+1
# # print("Marks greater than 80:",count)
    
    
# #Each row represents one day, and each column represents one product.   
# sales = np.array([
#     [10, 15, 20],
#     [25, 10, 30],
#     [20, 35, 15],
#     [30, 25, 40]
# ])

# daily_total = np.sum(sales, axis=1)
# print("Total sales for each day:", daily_total)

# product_sales = np.sum(sales, axis=0)
# print("total sales for each product:",product_sales)

# highest_sales=np.argmax(daily_total)
# print("day with highest total sales:",highest_sales+1)

# # First, you already calculated:
# # daily_total = np.sum(sales, axis=1)
# # This gives:
# # [45 65 70 95]
# # Now find the position of the highest total:
# # highest_sales = np.argmax(daily_total)print("Day with highest total sales:", highest_sales + 1)
# # Output:
# # Day with highest total sales: 4
# # Why +1?
# # Because Python indexing starts at 0.
# # Index 3 represents Day 4.


# for i in range(len(daily_total)):
#     print("Day",i+1,":",daily_total[i])
    
    



# arr = np.array([5,10,15,20,25,30,35])


# # Print the third element.
# # Print the last three elements.
# # Print every second element.
# # Reverse the array.
# print(arr[2])
# print(arr[4:])
# print(arr[1:6:2])
# print(arr[::-1])

# data = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# # 1. Print 50 using indexing.
# # 2. Print the entire second row.
# # 3. Print the entire third column.
# # 4. Extract this subarray:
# # [[50 60]
# #  [80 90]]

# print(data[1,1])
# print(data[1,:])
# print(data[:,2])
# print(data[1:3,1:3])


# salaries = np.array([25000, 40000, 55000, 30000, 70000, 45000])
# print("salaries greater than 40000:",salaries[salaries>40000])
# print("Print salaries between 30000 and 60000, including both")
# print(salaries[(salaries>=30000) & (salaries <=60000)])
# print("Print salaries less than 30000 OR greater than 60000.")
# print(salaries[(salaries<30000)|(salaries>60000)])
# print("Using np.where(), replace salaries below 40000 with low and all others with High")
# result = np.where(salaries<40000 , "Low", "High")
# print(result)

# marks = np.array([
#     [85, 70, 90],
#     [45, 60, 55],
#     [95, 88, 92],
#     [30, 40, 35]
# ])

# print(marks[marks>80])
# print(marks[marks[:,0]>80])
# print(marks[(marks>=50) & (marks<=90)])
# print(marks[marks[:,2]<50])

#broadcasting
# prices = np.array([100, 200, 300, 400])

# print( prices + 50)
# print(prices*2)
# print(prices-10)
# # print(np.shape(prices))
# print(prices.shape)

# marks = np.array([
#     [60, 70, 80],
#     [75, 85, 90],
#     [50, 65, 70]
# ])

# print(marks+5)
# each_sub=np.array(
#     [10,5,2]
# )
# print(marks + each_sub)

# each_std =np.array([
#     [5],
#     [10],
#     [15]
# ])

# result= marks + each_std
# print(result)

import numpy as np

# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])
# result = np.concatenate((a,b))
# print(result)

# result2 =np.hstack((a,b))
# print(result2)

# result3 = np.vstack((a,b))
# print(result3)
# print(result3.shape)
# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# b = np.array([
#     [7, 8, 9],
#     [10, 11, 12]
# ])

# result1 = np.concatenate((a,b),axis=0)
# print(result1)
# result2 = np.concatenate((a,b),axis=1)
# print(result2)
# result3 = np.vstack((a,b))
# print(result3)
# result4 =np.hstack((a,b))
# print(result4)
# print(result1.shape)

# print(result2.shape)


#random number 
# rng= np.random.default_rng(42)
# arr1= rng.integers(10,51,size=5)
# print(arr1)
# print(arr1.shape)

# arr2 = rng.random((3,3))
# print(arr2)
# print(arr2.shape)

# arr3=rng.normal(loc=100, scale=15, size= 5)
# print(arr3)
# print(arr3.shape)

# students = np.array([101, 102, 103, 104, 105, 106, 107, 108])
# rng = np.random.default_rng(10)
# result1= rng.choice(students,size=3,replace = False)
# print(result1)

# rng.shuffle(students)
# print(students)


#handling the missing value

# marks = np.array([85, np.nan, 90, 75, np.nan, 95, 80])
# print(marks)

# print(np.isnan(marks))
# arr = np.isnan(marks).sum()
# print(arr)

# clean_data = marks[~np.isnan(marks)]
# print(clean_data)

# print(np.mean(clean_data))

# scores = np.array([70, np.nan, 85, 90, np.nan, 95])
# avg =np.nanmean(scores)

# result = np.where(np.isnan(scores), avg, scores)
# print(result)

# print(np.max(result))
# print(np.min(result))

# 1. Print all even numbers.
# 2. Calculate the sum of odd numbers.
# 3. Count numbers greater than 40.

# numbers = [12, 25, 30, 45, 50, 65, 80]
# even_no =[ ]
# odd_no =[]
# total= 0
# for i in numbers:
#     if i%2==0:
#         even_no.append(i)
#     else:
#         odd_no.append(i)
#         total= total+i
# print(even_no)
# print(odd_no)
# print("Sum of Odd no:",total)

# count= 0
# for i in numbers:
#     if i >40:
#         count = count+1
# print(" total no greater than 40 :", count)

# Create a list containing squares of even numbers.
# Create a list of numbers divisible by 3 and greater than 10
# numbers = [3, 6, 9, 12, 15, 18, 21]
# sq_no = [i*i for i in numbers if i%2==0]
# print(" squares of even numbers.",sq_no)

# result =[ i for i in numbers if i%3 ==0 and i >10]
# print(" numbers divisible by 3 and greater than 10",result)

# Calculate the sum of each row.
# Calculate the mean of each column.
# Find the maximum value.
# Reshape the array into (1, 9).


# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# sum = np.sum(arr,axis=1)
# print("sum of each row ",sum)

# mean =np.mean(arr,axis= 0 )
# print("mean of each column:", mean)

# maximum = arr[0][0]

# for row in arr:
#     for num in row:
#         if  num > maximum:
#             maximum = num
# print("maximum", maximum)

# new_arr = arr.reshape(1,9)
# print(new_arr)

# 1. Count the missing values.
# 2. Calculate the mean while ignoring NaN.
# 3. Replace missing values with the mean.
# 4. Find the highest and lowest scores after replacement.
# scores = np.array([65, np.nan, 80, 90, np.nan, 75, 95])

# print(np.isnan(scores).sum())

# Mean= np.nanmean(scores)

# new_scores = np.where(np.isnan(scores), Mean, scores )
# print(new_scores)

# print("Highest scores:", np.max(new_scores))
# print("Lowest scores:", np.min(new_scores))

# Extract marks greater than 75.
# Replace marks below 40 with 40.
# Count students scoring 60 or above.
# Calculate the average of the updated array.
# Find the index of the highest mark.

# marks = np.array([45, 78, 90, 32, 85, 60, 95, 40])

# mark_greater75= []
# for i in marks:
#     if i > 75:
#         mark_greater75.append(i)
# print(mark_greater75)
# result = np.maximum(marks,40)
# print(result)

# count = 0
# for i in marks:
#     if i >60:
#         count = count+1
# print(count)

# print("Average of updated array:", np.mean(result))

# print(np.argmax(result))


# students = [
#     ["A", 85, 90, 78],
#     ["B", 65, 70, 60],
#     ["C", 95, 88, 92],
#     ["D", 45, 55, 50]
# ]

# # Calculate the total marks of each student.
# # Calculate the average marks of each student.
# # Find the student with the highest total marks.
# # Print the names of students whose average is greater than 75
# highest = 0
# top_students = ""
# top_studentss =[]
# for student in students:
#     name = student[0]
#     marks=student[1:]
#     total = sum(marks)
#     avg = total/len(marks)
#     print(f"Total of student {name} :{total}")
#     print("Average:", avg)
#     if total >highest:
#         highest = total
#         top_students= name
#     if avg >75:
#        top_studentss.append(name)
    


# print(f"student with the highest total marks is {name}:{highest} ")
# print("name of student who score above 75 are: ",  top_studentss)


# marks = np.array([
#     [85, 70, 90],
#     [60, 45, 75],
#     [95, 88, 92],
#     [40, 55, 65]
# ])
# # Calculate the average marks of each student using axis.
# # Find the highest mark in each subject.
# # Count how many marks are greater than or equal to 75.
# # Replace all marks below 50 with 50 using np.where().
# # Find the index of the student with the highest average.
# average = np.mean(marks, axis=1)
# print("average marks :", average)
# highest = np.max(marks, axis=0)
# print("Highest marks in each subject:",highest)
# count= 0
# for row in marks:
#     for num in  row:
#         if num >= 75:
#             count+=1
              
# print("marks are greater than or equal to 75:",count)
# new_mrks=np.where(marks<50 , 50 , marks)
# print(new_mrks)

# print(np.argmax(average))



# 1. Calculate the total sales of each shop.
# 2. Calculate the average sales of each month.
# 3. Find the shop with the highest total sales.
# 4. Count how many sales values are greater than 150.
# 5. Increase all sales below 120 to 120 using np.where().
# 6. Find the maximum sales value in each shop.
# Bonus Challenge 🔥: Find the shop with the lowest average sales.
# sales = np.array([
#     [120, 150, 180],
#     [200, 170, 160],
#     [90, 110, 130],
#     [250, 220, 210]
# ])
# total_sales= np.sum(sales, axis= 1)
# print("total sales:", total_sales)

# average_sales = np.mean(sales, axis =0)
# print("Average sales of each month:", average_sales)
 
# highest_sales= np.argmax(total_sales)
# print("shop with the highest sales:",highest_sales)

# count = np.sum(sales >150)

# print("total sales greater than 150:",count)

# new_sales= np.where(sales<120, 120, sales)
# print(new_sales)

# maximum_sale = np.max(sales,axis= 1)
# print("maximum sale in each shop:", maximum_sale)

# lowest_avg_sale = np.mean(sales , axis =1)

# print("shop with the lowest average sale :", np.argmin(lowest_avg_sale))






# Find the sum of each column.
# Calculate the average of each row.
# Count how many elements are between 40 and 80 (inclusive).
# Replace all values below 50 with the average of the entire array using np.where().
# Find the index of the row with the highest sum.
# Extract all elements greater than 60 using Boolean indexing.
# data = np.array([
#     [25, 40, 55, 70],
#     [80, 35, 60, 90],
#     [45, 75, 85, 30]
# ])

# total = np.sum(data, axis= 0)
# print(total)

# average = np.mean(data, axis= 1)
# print(average)


# count = np.sum((data>=40) & (data <=80))
# print(count)



# row_total = np.sum(data, axis=1)
# highest_sum = np.argmax(row_total)
# print(highest_sum)

# result = data[data>60]
# print(result)

# avg = np.mean(data)
# count= np.sum(data>avg)
# print(count)
# new_data=np.where(data<50, avg, data)
# print(new_data)

# sales = np.array([
#     [120, 150, np.nan],
#     [90, 200, 180],
#     [250, np.nan, 220],
#     [100, 130, 160]
# ])

# count = np.isnan(sales).sum()
# print(count)

# Average = np.nanmean(sales)
# new_sales = np.where(np.isnan(sales), Average, sales)
# print(new_sales)

# total_sales = np.sum(new_sales,axis=1)
# print(total_sales)

# highest_sales_idx= np.argmax(total_sales)
# print(highest_sales_idx)

# count = np.sum(new_sales>150)
# print(count)


#Numpy Function
# arr = np.array([10, 20, 10, 30, 20, 40, 30, 50, 10])

# print(np.unique(arr))

# values, count = np.unique(arr, return_counts=True)
# print(values)
# print(count)

# marks = np.array([75, 92, 60, 88, 95, 70])
# ascending=np.sort(marks)
# print("ascending:", ascending)

# descending = np.sort(marks)[::-1]
# print(descending)

# sorted_idx = np.argsort(marks)
# print(sorted_idx)

# scores = np.array([15, 45, 67, 105, 120, 30, 85])

# new_scores = np.clip(scores, 40,100)
# print(new_scores)

# print(scores)


# scores = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# print("25th percentile:",np.percentile(scores,25))
# print("50th percentile :",np.percentile(scores,50))
# print("75th percentile :",np.percentile(scores,75))

# data = np.array([25, 40, 25, 60, 75, 40, 90, 110, 15, 75, 60])

# value,count = np.unique(data, return_counts=True)
# print("Unique values:",value)
# print("frequency of unique value:", count)

# sorted_data = np.sort(data)
# print(sorted_data)

# new_data = np.clip(data, 30, 100)
# print(new_data)

# print("Median :", np.percentile(data, 50))

# sorted_idx = np.argsort(data)
# print(sorted_idx)



# Numpy  with ML

#matrix multiplication
# import numpy as np

# X = np.array([
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ])

# weights = np.array([5, 3])
# prediction = np.dot(X,weights)
# prediction2 = X@weights
# print(prediction)
# print(prediction2)

# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90],
#     [100, 110, 120]
# ])
# print("original array shape :",np.shape(arr))
# Trans = arr.T
# print("Transposed:",Trans)
# print("shape of transposed :",np.shape(Trans))



# 1. Calculate the determinant of A.
# 2. Find the inverse of A.
# 3. Solve A @ x = b using np.linalg.solve().
# A = np.array([
#     [4, 2],
#     [1, 3]
# ])

# b = np.array([10, 8])
# determinnant = np.linalg.det(A)
# print(determinnant)

# inverse = np.linalg.inv(A)
# print(inverse)


# result = np.linalg.solve(A, b)
# print(result)


# X = np.array([
#     [3, 4],
#     [5, 6],
#     [7, 8]
# ])

# weights = np.array([4, 3])
# bias = 5
# prediction = np.dot(X,weights)
# print(prediction)
# prediction2 = X@weights
# print(prediction2)

# new_prediction1 = prediction+bias
# print(new_prediction1)

# new_prediction2 = prediction2 +bias
# print(new_prediction2)

# marks = np.array([45, 78, 90, 32, 67, 88, 25, 95, 60])

# new_marks =marks [marks>70]
# print(new_marks)

# count = np.sum(marks<40)
# print(count)

# result = np.where (marks<40, 40, marks)
# print(result)

# average = np.mean(result)
# print(average)

# print(np.argmax(result))

# marks = np.array([
#     [85, 90, 78],
#     [70, 88, 92],
#     [95, 80, 85],
#     [60, 75, 70]
# ])
# print(np.shape(marks))

# total_marks = np.sum(marks, axis=1)
# print(total_marks)

# avg_marks = np.mean(marks, axis= 0)
# print(avg_marks)

# highest_marks = np.max(marks, axis= 0)
# print(highest_marks)

# print(np.argmax(total_marks))

# scores = np.array([75, np.nan, 90, 85, np.nan, 95, 80])
# print(np.isnan(scores).sum())
# mean_ig_nan = np.nanmean(scores)
# new_scores = np.where(np.isnan(scores), mean_ig_nan, scores)

# print(new_scores)
# print(np.max(new_scores))
# print(np.min(new_scores))

# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

# new_arr =arr.reshape(3,4)
# print(new_arr)
# print(np.shape(new_arr))
# print(new_arr.flatten())
# print("transpose;",new_arr.T)
# print(np.split(arr,3))

# X = np.array([
#     [2, 4],
#     [3, 5],
tudent = ("Sita", 21, 90, 85, 90, 95)

print(student.count(90))
print(student.index(85))
name,age,mark1,mark2,mark3,mark4 =student
print(name)
print(age)

student_list = list(student)

student_list[1]= 22
student = tuple(student_list)
print(student)#     [5, 7],
#     [6, 8]
# ])

# weights = np.array([4, 3])
# bias = 10

# actual = np.array([30, 38, 50, 60])

# print(np.shape(X))
# prediction1 = np.dot(X, weights) + bias
# prediction2 = X@ weights +bias

# print(prediction2)
# print(prediction1)

# diff = actual - prediction1
# MAE = np.mean(np.abs(diff))

# print (MAE)


#TUPLE
# marks = (75, 85, 90, 65, 95, 80)
# print(marks[0])
# print(marks[-1])
# print(marks[1:5])
# print(marks[::-1])
# print(len(marks))

s