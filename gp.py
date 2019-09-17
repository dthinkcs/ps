credits = [22, 22, 22, 23, 23, 23, 21, 14]
n = int(input("Number Of Semesters: "))
assert 0 < n <= 8
print("Enter gpa for every Semester: ")
gpa = list(map(float, input().strip().split(" ")))
tot = 0
for i in range(n):
    tot += credits[i] * gpa[i]
print(tot / sum(credits[:n]))
