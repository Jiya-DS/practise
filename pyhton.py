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

emp = {
    "name":"Sita",
    "age" : 24,
    "salary" : 35000,
    "department" : "IT"
}
print(emp["name"])
print(emp.get("salary"))
emp["salary"]= 45000
emp["city"]="Pokhara"
print(emp)