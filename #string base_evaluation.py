#string base_evaluation
key = ['A', 'C', 'B', 'D']
student =list[input("Enter your Answers:")]
score = 0
for i in range(len(key)):
    if student[i] == key[i]:
        score = score + 4
    else:
        score = score - 1
print("Exam Score:", score)