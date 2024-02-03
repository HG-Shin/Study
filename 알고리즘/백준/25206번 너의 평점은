grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade_score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
total_grade = 0
total_sum = 0

for i in range(20):
    a, b, c = input().split()
    b = float(b)
    if c == 'P':
        continue
    total_grade += b * grade_score[grade.index(c)]
    total_sum += b

print(total_grade/total_sum)