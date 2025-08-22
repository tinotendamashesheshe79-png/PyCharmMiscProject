##SCHOOL GRADE
PASSING_GRADE= 60
student_name="tinotenda"
math_score=85
english_score=72
average=(english_score+math_score)/2
print("Student Results")
print("Name of student:",student_name)
print("English Score:",english_score)
print("Math Score:",math_score)
print("Average grade :",average)
if average >= PASSING_GRADE:
    print("Pass")
else:
    print("Fail")