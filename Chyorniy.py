def find_best_student(student_names, student_scores):
    if not student_names or not student_scores:
        return None
    max_score = 0
    max_index = 0
    i = 0
    while i < len(student_scores):
        score = student_scores[i]
        if score > max_score:
           max_score = score
           max_index = i
        i = i + 1
    return student_names[max_index]
names1 = ["Alice", "Bob", "Charlie", "David"]
scores1 = [88, 92, 99, 95]
names2 = ["Eve", "Frank", "Grace"]
scores2 = [95, 85, 95]
names3 = []
scores3 = []

print("Top student is: ", find_best_student(names1,scores1))
print("Top student in a tie is: " , find_best_student(names2,scores2))
print("Result for empty lists: ", find_best_student(names3,scores3))



