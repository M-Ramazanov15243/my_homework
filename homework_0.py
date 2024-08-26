grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_point = dict()
students_2 = sorted(students)
a = grades[0]
b = sum(a) / len(a)
average_point[students_2[0]] = b

a1 = grades[1]
b1 = sum(a1) / len(a1)
average_point[students_2[1]] = b1

a2 = grades[2]
b2 = sum(a2) / len(a2)
average_point[students_2[2]] = b2

a3 = grades[3]
b3 = sum(a3) / len(a3)
average_point[students_2[3]] = b3

a4 = grades[4]
b4 = sum(a4) / len(a4)
average_point[students_2[4]] = b4

print(average_point)
