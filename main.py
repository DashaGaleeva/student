f = open('students.txt')
f.readline()
students = []
class Student:
  number = 0
  name = ''
  titleProjectId = 0
  Class = ''
  score = 0
for i in range(len(f.readlines())):
  students.append(Student())
  a = list(map(str,f.readline().split(',')))
  students[i].number = int(a[0])
  students[i].name = a[1]
  students[i].titleProjectId = int(a[2])
  students[i].Class = a[3]
  if a[4] == 'None':
      a[4] = 0
      students[i].score = int(a[4])
f.close()
s = Student()
for i in range(1,len(students)):
  s.number = students[i].number
  s.name = students[i].name
  s.titleProjectId = students[i].titleProjectId
  s.Class = students[i].Class
  s.score = students[i].score
  t = students[i].score
  j = i - 1
  while j >= 0 and t < students[i].score:
    students[j+1] = students[j]
    j -= 1
  students[j+1].numder = s.number
  students[j+1].name = s.name
  students[j+1].titleProjectId = s.titleProjectId
  students[j+1].Class = s.Class
  students[j+1].score = s.score
print('10 класс:')
k = 0
for i in range(len(students)):
  if students[i].Class[:2] == "10":
    k += 1
    print(k, "место:", students [i].name)
# 2
q = int(input())
for i in range(len(students)):
  if students[i].titleProjectId == q.titleProjectId:
    print("Проект №", q)
    print("Автор:", students[i].name)

