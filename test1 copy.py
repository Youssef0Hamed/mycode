students =[]
id = 0
for h in range(0, 3) :

    name = input("enter your name ")
    id += 1
    # courses = {None} 
    courses = set()

    for i in range(0,2):
        course = input("enter course name ")
        courses.add(course)
    
    student = { 
        "id" : id,
        "name" : name,
        "course" : courses
        }
    students.append(student)

for s in students :
    print(f"ID = {s['id']} , NAME IS {s['name']} , COURSES ARE {s['course']}")

print(type(student))
print(type(courses))