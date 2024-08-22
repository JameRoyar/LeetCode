num = int(input("Enter a number: "))
degree = "ABCDE"
score = 0

if num > 100 or num < 0:
    print("Invalid number")

else:
    score = num // 10
    if score < 6 : score = 5
    if score == 10 : score = 9

print("The score is: {}, and the grade is: {}".format(num, degree[9 - score]))
