#PYTHON SETS

# students = ["Ram", "Sita", "Hari", "Ram", "Gita", "Sita", "Shyam"]

# student_set = set(students)
# print(student_set)

# print(len(student_set))

# student_set.add("Rita")
# student_set.discard("Hari")
# check = "Ram" in student_set
# print(check)
# print(student_set)

# group_A = {"Python", "Java", "SQL", "C++"}
# group_B = {"Python", "JavaScript", "SQL", "HTML"}
# print(group_A | group_B)
# print(group_A & group_B)
# print(group_A  - group_B)
# print(group_B - group_A)
# print(group_A  ^ group_B)
# print("Python" in group_A)

#Dictionary

# student = {
#     "name": "Sita",
#     "age": 21,
#     "marks": 88,
#     "city": "Pokhara"
# }
# print(student["name"])
# print(student.get("marks"))
# student["age"]=22
# student["grade"]= "A"
# print(student.get("email","None"))
# print(len(student))
# print(student)
# print("marks" in student)

# emp = {
#     "name":"Sita",
#     "age" : 24,
#     "salary" : 35000,
#     "department" : "IT"
# }
# print(emp["name"])
# print(emp.get("salary"))
# emp["salary"]= 45000
# emp["city"]="Pokhara"
# print(emp)

# students = {
#     "Ram": 85,
#     "Sita": 92,
#     "Hari": 76,
#     "Gita": 88,
#     "Rita": 95
# }
# for key,value in students.items():
#     print(key,":",value)
    
# for key,value in students.items():
#     if value >85:
#         print(key,":",value)
    
# highest_marks=0
# top_student = ""
# for name, marks in students.items():
#     if value>highest_marks:
#         highest_marks = marks
#         top_student = name
# print(top_student)
# print(highest_marks)
employees = {
    "Ram": {"salary": 30000, "department": "IT"},
    "Sita": {"salary": 45000, "department": "HR"},
    "Hari": {"salary": 50000, "department": "IT"},
    "Gita": {"salary": 40000, "department": "Finance"}
}
for name, details in employees.items():
    print(name,details["salary"])
    
for name, details in employees.items():
    department = details["department"]
    if department == "IT":
        print(name,department)
        
employees["Sita"]["salary"] = 55000
print(employees)


highest_salary = 0
top_emp =""
for name, details in employees.items():
    salary=details["salary"]
    if salary>highest_salary:
        highest_salary = salary
        top_emp = name
print(highest_salary)
print(top_emp)               
