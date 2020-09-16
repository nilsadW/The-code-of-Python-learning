#这是一个判断学生成绩是否达标的程序，要求输入学生数量，以及各个学生
#物理、数学、历史三科的成绩，如果总成绩小于 120，程序打印 “failed”，否则打印 “passed”。
n = int(input("Enter the number of students: "))
data = {}
Subjects = ('Physics', 'Maths', 'History')
for i in range(0, n):
    name = input("Enter the name of the student {}: ".format(i + 1))
    marks = []
    for x in Subjects:
        marks.append(int(input("Enter the marks of {}".format(x))))
    data[name] = marks
for x, y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")

